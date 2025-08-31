import requests
import re
import random
import time
import argparse
from requests.structures import CaseInsensitiveDict

# List of user agents
USER_AGENTS = [
    # Windows Chrome
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    # Windows Firefox
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
    # Mac Safari
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Safari/605.1.15",
    # Linux Chrome
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    # Linux Firefox
    "Mozilla/5.0 (X11; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0",
    # Edge Windows
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
]

BASE_URL = "http://www.insecam.org/en"

# Show ASCII art banner.
BANNER = r"""
 ___                                    
|_ _|_ __  ___  ___  ___ __ _ _ __ ___  
 | || '_ \/ __|/ _ \/ __/ _` | '_ ` _ \ 
 | || | | \__ \  __/ (_| (_| | | | | | |
|___|_| |_|___/\___|\___\__,_|_| |_| |_|

Access Insecure Security Cameras in 20+ countries.

    Author: Ninja-Yubaraj
    Github: https://github.com/Ninja-Yubaraj/Insecam
"""

def get_headers():
    # Return headers with a random User-Agent.
    return CaseInsensitiveDict({
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Connection": "keep-alive"
    })


def fetch_countries():
    # Fetch and return the list of countries with camera counts.
    url = f"{BASE_URL}/jsoncountries/"
    response = requests.get(url, headers=get_headers())
    response.raise_for_status()
    return response.json().get("countries", {})


def display_countries(countries, cols=3):
    # Display countries in a compact multi-column format.
    items = []
    for code, data in countries.items():
        items.append(f"{code:<3} {data['country']:<20} ({data['count']})")

    # Group items into rows
    for i in range(0, len(items), cols):
        print("    ".join(items[i:i + cols]))


def fetch_country_pages(country_code):
    # Fetch the total number of pages for a given country.
    url = f"{BASE_URL}/bycountry/{country_code}"
    response = requests.get(url, headers=get_headers())
    if response.status_code != 200:
        return 0
    pages = re.findall(r'pagenavigator\("\?page=", (\d+)', response.text)
    return int(pages[0]) if pages else 0


def fetch_camera_ips(country_code, pages):
    # Fetch all camera IPs for a given country and number of pages.
    all_ips = set()
    for page in range(pages):
        url = f"{BASE_URL}/bycountry/{country_code}/?page={page}"
        response = requests.get(url, headers=get_headers())
        ips = re.findall(r"http://\d+\.\d+\.\d+\.\d+:\d+", response.text)
        all_ips.update(ips)
    return sorted(all_ips)


def main():
    parser = argparse.ArgumentParser(
        description=f"{BANNER}\nUse this tool to fetch insecure camera IPs from Insecam.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("-C", "--country-code", help="Country code (e.g., US, IN, JP)")
    parser.add_argument("-q", "--quiet", action="store_true", help="Quiet mode (only show IPs)")
    args = parser.parse_args()

    if not args.quiet:
        print(BANNER)
        time.sleep(0.25) # small pause for effect

    try:
        countries = fetch_countries()
        if not countries:
            print("No countries found.")
            return

        # If country code not given, display list
        if not args.country_code:
            if not args.quiet:
                print("\nAvailable Countries:\n")
                display_countries(countries, cols=3)
            print("\nUse -C <CODE> to fetch IPs from a specific country.")
            return

        country_code = args.country_code.strip().upper()
        if country_code not in countries:
            print("Invalid country code.")
            return

        # Get total pages
        pages = fetch_country_pages(country_code)
        if pages == 0:
            print("No cameras found for this country.")
            return

        # Fetch camera IPs
        ips = fetch_camera_ips(country_code, pages)

        if not args.quiet:
            print(f"\nFound {len(ips)} cameras in {countries[country_code]['country']}:\n")

        for ip in ips:
            print(ip)

    except requests.RequestException as e:
        print(f"Network error: {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
