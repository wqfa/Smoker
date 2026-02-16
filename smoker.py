#!/usr/bin/env python3
"""
🔥 Smoker
Lightweight Python utility – Termux Friendly
"""

__version__ = "0.1.0"
__author__ = "Smoker"

import argparse
import sys
import platform
import time


# =====================
# Core Functions
# =====================

def smoke(target="world"):
    return f"🔥 Smoker is running on {target}"

def info():
    return {
        "name": "Smoker",
        "version": __version__,
        "author": __author__,
        "python": sys.version.split()[0],
        "platform": platform.system(),
        "termux": is_termux()
    }

def is_termux():
    return "com.termux" in sys.prefix.lower()

def banner():
    return r"""
   ███████╗███╗   ███╗ ██████╗ ██╗  ██╗███████╗██████╗
   ██╔════╝████╗ ████║██╔═══██╗██║ ██╔╝██╔════╝██╔══██╗
   ███████╗██╔████╔██║██║   ██║█████╔╝ █████╗  ██████╔╝
   ╚════██║██║╚██╔╝██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
   ███████║██║ ╚═╝ ██║╚██████╔╝██║  ██╗███████╗██║  ██║
   ╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
"""


# =====================
# CLI
# =====================

def cli():
    parser = argparse.ArgumentParser(
        prog="smoker",
        description="🔥 Smoker – Termux Friendly Python Tool"
    )

    parser.add_argument(
        "-t", "--target",
        help="Target name",
        default="world"
    )

    parser.add_argument(
        "--info",
        action="store_true",
        help="Show tool information"
    )

    parser.add_argument(
        "--banner",
        action="store_true",
        help="Show Smoker banner"
    )

    parser.add_argument(
        "--loop",
        type=int,
        help="Loop execution (seconds)"
    )

    args = parser.parse_args()

    if args.banner:
        print(banner())
        return

    if args.info:
        data = info()
        for k, v in data.items():
            print(f"{k}: {v}")
        return

    if args.loop:
        try:
            while True:
                print(smoke(args.target))
                time.sleep(args.loop)
        except KeyboardInterrupt:
            print("\n⛔ Stopped.")
            return

    print(smoke(args.target))


# =====================
# Entry Point
# =====================

if __name__ == "__main__":
    cli()
  
