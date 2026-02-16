import sys
import platform

def smoke(target="world"):
    return f"🔥 Smoker running on {target}"

def info():
    from .core import is_termux
    return {
        "name": "Smoker",
        "version": "0.1",
        "author": "Valter",
        "python": sys.version.split()[0],
        "platform": platform.system(),
        "termux": is_termux()
    }

def is_termux():
    return "com.termux" in sys.prefix.lower()
  
