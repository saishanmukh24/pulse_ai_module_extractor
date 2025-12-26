import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def crawl_docs(start_url: str, max_pages: int = 50):
    visited_urls = set()
    collected_pages = {}

    domain = urlparse(start_url).netloc
    to_visit = [start_url]

    while to_visit and len(visited_urls) < max_pages:
        current_url = to_visit.pop()

        if current_url in visited_urls:
            continue

        try:
            response = requests.get(current_url, timeout=10)
            if response.status_code != 200:
                continue

            visited_urls.add(current_url)
            soup = BeautifulSoup(response.text, "lxml")
            collected_pages[current_url] = soup

            for anchor in soup.find_all("a", href=True):
                link = urljoin(current_url, anchor["href"])
                parsed = urlparse(link)

                if parsed.netloc == domain and link not in visited_urls:
                    to_visit.append(link)

        except Exception:
            continue

    return collected_pages
