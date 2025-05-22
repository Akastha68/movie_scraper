import threading
import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
from config import filmyfly, HEADERS
from db import insert_movie, insert_video_link


db_lock = threading.Lock()
class Scrape:
    def __init__(self, base_url):
        self.base_url = base_url

    def _get_soup(self, url):
        try:
            res = requests.get(url, headers=HEADERS, timeout=10)
            res.raise_for_status()
            return bs(res.content, "html.parser")
        except requests.RequestException as e:
            print(f"[ERROR] Failed to fetch {url}: {e}")
            return None

    def scrape(self):
        home_soup = self._get_soup(self.base_url)
        if not home_soup:
            return

        td_tags = home_soup.find_all("td")
        for td in td_tags:
            a_tag = td.find("a", href=True)
            if not a_tag:
                continue

            href = a_tag["href"]
            image_tag = a_tag.find("img", src=True)
            image_url = urljoin(self.base_url, image_tag["src"]) if image_tag else None
            detail_url = urljoin(self.base_url, href)

            detail_soup = self._get_soup(detail_url)
            if not detail_soup:
                continue

            title_tag = detail_soup.find("title")
            movie_title = title_tag.text.strip() if title_tag else "Unknown Title"
            with db_lock:
                movie_id = insert_movie(movie_title, image_url)

            download_tag = detail_soup.find("a", class_="dl")
            if not download_tag:
                continue

            intermediate_url = download_tag.get("href")
            if not intermediate_url:
                continue

            intermediate_url = urljoin(detail_url, intermediate_url)
            deep_soup = self._get_soup(intermediate_url)
            if not deep_soup:
                continue

            video_blocks = deep_soup.find_all("div", class_="dlink")
            for block in video_blocks:
                quality = block.get_text(strip=True)
                video_link_tag = block.find("a", href=True)
                if video_link_tag:
                    new1_url = video_link_tag["href"]
                    new1 = self._get_soup(new1_url)
                    if new1 and new1.a:
                        video_url = new1.a.get("href")
                        with db_lock:
                             insert_video_link(movie_id, quality, video_url)
