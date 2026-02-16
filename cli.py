import argparse
import time
from .core import smoke, info
from .banner import banner

def cli():
    parser = argparse.ArgumentParser(
        prog="smoker",
        description="🔥 Smoker – modular Termux friendly tool"
    )

    parser.add_argument("-t", "--target", default="world", help="Target name")
    parser.add_argument("--info", action="store_true", help="Show info")
    parser.add_argument("--banner", action="store_true", help="Show banner")
    parser.add_argument("--loop", type=int, help="Loop output (seconds)")

    args = parser.parse_args()

    if args.banner:
        print(banner())
        return

    if args.info:
        for k, v in info().items():
            print(f"{k}: {v}")
        return

    if args.loop:
        try:
            while True:
                print(smoke(args.target))
                time.sleep(args.loop)
        except KeyboardInterrupt:
            print("\n⛔ Stopped")
            return

    print(smoke(args.target))
  
