from config import filmyfly
from db import setup_tables
from scraper import Scrape

def main():
    setup_tables()
    scraper = Scrape(filmyfly)
    scraper.scrape()
    print("[INFO] Scraping and database storage completed successfully.")

if __name__ == "__main__":
    main()
