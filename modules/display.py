import sys
import time
from colorama import Fore, Back, Style, init

init(autoreset=True)

CYAN    = Fore.CYAN
GREEN   = Fore.GREEN
RED     = Fore.RED
YELLOW  = Fore.YELLOW
WHITE   = Fore.WHITE
MAGENTA = Fore.MAGENTA
RESET   = Style.RESET_ALL
BRIGHT  = Style.BRIGHT
DIM     = Style.DIM

BANNER = f"""
{CYAN}{BRIGHT}
  ██████  ██░ ██  ▒█████    ██████ ▄▄▄█████▓ ██▀███   ▄▄▄       ▄████▄  ▓█████ 
▒██    ▒ ▓██░ ██▒▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▒▓██ ▒ ██▒▒████▄    ▒██▀ ▀█  ▓█   ▀ 
░ ▓██▄   ▒██▀▀██░▒██░  ██▒░ ▓██▄   ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▒███   
  ▒   ██▒░▓█ ░██ ▒██   ██░  ▒   ██▒░ ▓██▓ ░ ▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▒▓█  ▄ 
▒██████▒▒░▓█▒░██▓░ ████▓▒░▒██████▒▒  ▒██▒ ░ ░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░░▒████▒
▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░░░ ▒░ ░
░ ░▒  ░ ░ ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░▒  ░ ░    ░      ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒    ░ ░  ░
░  ░  ░   ░  ░░ ░░ ░ ░ ▒  ░  ░  ░    ░        ░░   ░   ░   ▒   ░           ░   
      ░   ░  ░  ░    ░ ░        ░               ░           ░  ░░ ░         ░  ░
                                                                  ░              
{RESET}"""

BANNER_SMALL = f"""
{CYAN}{BRIGHT}
   ______  __               __  ______                    
  / ____/ / /_  ____  _____/ /_/_  __/________ _________  
 / / __  / __ \/ __ \/ ___/ __// / / ___/ __ `/ ___/ _ \ 
/ /_/ / / / / / /_/ (__  ) /_ / / / /  / /_/ / /__/  __/ 
\____/ /_/ /_/\____/____/\__//_/ /_/   \__,_/\___/\___/  
{RESET}"""

def print_banner():
    print(BANNER_SMALL)
    print(f"{CYAN}{'─'*55}{RESET}")
    print(f"{CYAN}  👻  OSINT Username Hunter  {DIM}v1.0{RESET}")
    print(f"{DIM}{CYAN}  by YourUsername  |  github.com/YourUsername/GhostTrace{RESET}")
    print(f"{CYAN}{'─'*55}{RESET}\n")

def print_found(platform, url):
    print(f"  {GREEN}{BRIGHT}[+]{RESET}  {WHITE}{BRIGHT}{platform:<22}{RESET}  {CYAN}{url}{RESET}")

def print_not_found(platform):
    print(f"  {RED}[-]{RESET}  {DIM}{platform}{RESET}")

def print_error(platform):
    print(f"  {YELLOW}[!]{RESET}  {DIM}{platform} (error){RESET}")

def print_checking(platform):
    print(f"  {CYAN}[~]{RESET}  Checking {platform}...", end="\r")

def print_info(msg):
    print(f"\n  {CYAN}[*]{RESET}  {msg}")

def print_summary(username, found, total, elapsed, out_file=None):
    print(f"\n{CYAN}{'─'*55}{RESET}")
    print(f"  {WHITE}{BRIGHT}Target   :{RESET}  {CYAN}{username}{RESET}")
    print(f"  {WHITE}{BRIGHT}Found    :{RESET}  {GREEN}{BRIGHT}{found}{RESET}")
    print(f"  {WHITE}{BRIGHT}Checked  :{RESET}  {total}")
    print(f"  {WHITE}{BRIGHT}Time     :{RESET}  {elapsed:.2f}s")
    if out_file:
        print(f"  {WHITE}{BRIGHT}Saved    :{RESET}  {CYAN}{out_file}{RESET}")
    print(f"{CYAN}{'─'*55}{RESET}\n")

def typing_effect(text, delay=0.03):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()
