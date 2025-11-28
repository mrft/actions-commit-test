#!/usr/bin/env python3
"""Print current datetime to stdout."""
from datetime import datetime

if __name__ == "__main__":
    print(datetime.now().isoformat())
