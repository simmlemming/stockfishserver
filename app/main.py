from server import start_server
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser('')
    parser.add_argument('--stockfish-bin', dest='stockfish_bin', required=True)

    args = parser.parse_args()

    if args.stockfish_bin == "fake":
        from fake_stockfish import Stockfish
    else:
        from stockfish import Stockfish

    start_server(Stockfish(args.stockfish_bin))
