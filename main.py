#!/usr/bin/env python3
"""Houseplant Out-of-Office entry: writes one short auto-reply to /output/entry.txt.

The reply is a fixed text: a thirsty houseplant whose roots have filed a
complaint with the windowsill. No input is read, no network is used, and the
output is deterministic.
"""
import os

ENTRY = "Away until someone remembers the watering can. My roots have filed a complaint with the windowsill."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
