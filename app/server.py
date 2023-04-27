import json
from http.server import HTTPServer, BaseHTTPRequestHandler


class StockfishRouter(BaseHTTPRequestHandler):

    def do_GET(self):
        body = {
            'message': 'Hello World!'
        }

        self.do_send_json_response(200, body)

    def do_send_json_response(self, code, body):
        self.send_response(code)
        if body:
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(json.dumps(body), "utf-8"))
        else:
            self.end_headers()

    def do_send_error(self, code, message):
        self.do_send_json_response(code, message)


def start_server():
    server = HTTPServer(("0.0.0.0", 8080), StockfishRouter)
    try:
        print(f"Starting on {server.server_address}...")
        server.serve_forever()
    except KeyboardInterrupt:
        pass
