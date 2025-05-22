from config import filmyfly
from db import setup_tables
from scraper import Scrape
from urllib.parse import urljoin
import time

def main():
    setup_tables()
    i=11
    while (i<=82):
        url = filmyfly+str(i)
        print(f"[INFO] Scraping started on {url}")
        scraper = Scrape(url)
        scraper.scrape()
        print("[INFO] Scraping and database storage completed successfully.")
        i+=1
if __name__ == "__main__":
    main()
