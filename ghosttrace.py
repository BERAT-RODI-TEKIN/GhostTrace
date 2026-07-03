#!/usr/bin/env python3
"""
GhostTrace v1.0 — OSINT Username Hunter
github.com/YourUsername/GhostTrace
"""

import json
import argparse
import time
import os
import sys
from pathlib import Path
from modules.display import (
    print_banner, print_info, print_summary, typing_effect, CYAN, RESET, BRIGHT, WHITE
)
from modules.checker import run_checks

BASE_DIR      = Path(__file__).parent
PLATFORMS_FILE = BASE_DIR / "data" / "platforms.json"
RESULTS_DIR   = BASE_DIR / "results"
RESULTS_DIR.mkdir(exist_ok=True)


def load_platforms():
    with open(PLATFORMS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["platforms"]


def save_results(username: str, results: list) -> str:
    found = [r for r in results if r["status"] == "found"]
    out_path = RESULTS_DIR / f"{username}.txt"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f"GhostTrace v1.0 — Results for: {username}\n")
        f.write("=" * 50 + "\n\n")
        for r in found:
            f.write(f"[+] {r['platform']:<22}  {r['url']}\n")
        f.write(f"\nTotal found: {len(found)}\n")
    return str(out_path)


def parse_args():
    parser = argparse.ArgumentParser(
        prog="ghosttrace",
        description="👻 GhostTrace — OSINT Username Hunter",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "username",
        nargs="?",
        help="Username to search"
    )
    parser.add_argument(
        "-u", "--username",
        dest="username_flag",
        metavar="USERNAME",
        help="Username to search (alternative)"
    )
    parser.add_argument(
        "-t", "--threads",
        type=int,
        default=20,
        metavar="N",
        help="Number of threads (default: 20)"
    )
    parser.add_argument(
        "--no-save",
        action="store_true",
        help="Do not save results to file"
    )
    return parser.parse_args()


def main():
    print_banner()

    args   = parse_args()
    username = args.username or args.username_flag

    if not username:
        typing_effect(f"  {CYAN}Enter a username to hunt:{RESET} ", delay=0.02)
        username = input(f"  {WHITE}{BRIGHT}>>>{RESET} ").strip()

    if not username:
        print_info("No username provided. Exiting.")
        sys.exit(1)

    platforms = load_platforms()
    total     = len(platforms)

    print_info(f"Target   : {CYAN}{BRIGHT}{username}{RESET}")
    print_info(f"Platforms: {total}")
    print_info(f"Threads  : {args.threads}")
    print(f"\n  {'─'*51}\n")

    start   = time.time()
    results = run_checks(platforms, username, threads=args.threads)
    elapsed = time.time() - start

    found_count = sum(1 for r in results if r["status"] == "found")
    out_file    = None

    if not args.no_save and found_count > 0:
        out_file = save_results(username, results)

    print_summary(username, found_count, total, elapsed, out_file)


if __name__ == "__main__":
    main()
