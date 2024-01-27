import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from termcolor import colored


class StockfishRouter(BaseHTTPRequestHandler):

    def do_POST(self):
        if self.path != '/call':
            self.do_send_text_error(500, f"Invalid path.")
            return

        request_body = self.read_body()
        print("")
        print(colored(f"> {request_body}", "light_green"))

        if not request_body:
            self.do_send_text_error(500, f"Cannot read request body: {str(request_body)}.")
            return

        if "method" not in request_body:
            self.do_send_text_error(500, f"'method' not found.")
            return

        sf_method_name = request_body["method"]
        sf_method = getattr(sf, sf_method_name, None)

        if not sf_method:
            self.do_send_text_error(500, f"Invalid method: '{str(sf_method_name)}'.")
            return

        args = request_body.get("args", {})
        # print(f"stockfish.{sf_method_name}(), args = {args}")
        try:
            body = sf_method(*args)
        except Exception as e:
            print(colored(f"stockfish error = {str(e)}", "red"))
            self.do_send_text_error(500, str(e))
            raise e

        print(colored(f"< {body}", "light_grey"))
        self.do_send_text_response(200, str(body))

    def read_body(self):
        if self.headers.get("Content-Type") == "application/json":
            length = int(self.headers.get("Content-Length"))
            return json.loads(self.rfile.read(length).decode("utf-8"))
        return None

    def do_send_text_error(self, code, message):
        self.do_send_text_response(code, message)
        # self.send_error(code, message)

    def do_send_text_response(self, code, body):
        self.send_response(code)
        if body:
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(bytes(body, "utf-8"))
        else:
            self.end_headers()


sf = None


def start_server(stockfish):
    global sf
    sf = stockfish

    server = HTTPServer(("0.0.0.0", 8080), StockfishRouter)
    try:
        print(colored(f"Starting on {server.server_address}...", "light_green"))

        parameters = stockfish.get_parameters()
        print(colored(json.dumps(parameters, indent=4), "dark_grey"))
        server.serve_forever()
    except KeyboardInterrupt:
        pass
