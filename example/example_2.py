import concurrent.futures
import time

import requests
from bs4 import BeautifulSoup


def main(url):
    print(f"Scraping {url}...")

    res = requests.get(url, timeout=5)

    if res.status_code == 200:
        soup = BeautifulSoup(res.text, "html.parser")
        first_desc = soup.select_one("p").text
        print(first_desc)
    else:
        print(res.status_code)


if __name__ == "__main__":

    urls = ["https://example.com", "https://example.org", "https://example.net", "https://example.com",
            "https://example.org", "https://example.net", "https://example.com", "https://example.org", "https://example.net"]

    print("---------- first method (for) ----------")
    startTime = time.time()
    for url in urls:
        main(url)
    endTime = time.time() - startTime
    print("for time >> ", endTime)

    print("--------- seconds method (concurrent) ---------")
    startTime = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # map -> iterable
        r = list(executor.map(main, urls))
    endTime = time.time() - startTime
    print("concurrent time >> ", endTime)
