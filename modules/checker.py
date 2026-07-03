import requests
import concurrent.futures
from modules.display import print_found, print_not_found, print_error, print_checking

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}
TIMEOUT = 8


def check_platform(platform: dict, username: str) -> dict:
    name     = platform["name"]
    url      = platform["url"].format(username)
    method   = platform.get("check", "status_code")
    expected = platform.get("expected", 200)

    print_checking(name)
    try:
        r = requests.get(url, headers=HEADERS, timeout=TIMEOUT, allow_redirects=True)

        if method == "status_code":
            found = r.status_code == expected
        elif method == "not_found_text":
            found = expected.lower() not in r.text.lower()
        else:
            found = False

        if found:
            print_found(name, url)
            return {"platform": name, "url": url, "status": "found"}
        else:
            print_not_found(name)
            return {"platform": name, "url": url, "status": "not_found"}

    except requests.exceptions.RequestException:
        print_error(name)
        return {"platform": name, "url": url, "status": "error"}


def run_checks(platforms: list, username: str, threads: int = 20) -> list:
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {
            executor.submit(check_platform, p, username): p for p in platforms
        }
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())
    return results
