from ui import app
import argparse
import logging
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Minidetector web UI')    
    parser.add_argument("--debug", const=True, default=False, nargs='?', help="enable debug logging")
    args = parser.parse_args()
    logging.root.setLevel(logging.DEBUG if args.debug else logging.INFO)
    app.run()