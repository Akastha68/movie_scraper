import os
from dotenv import load_dotenv

load_dotenv("film.env")

filmyfly = os.getenv("filmyfly")
if not filmyfly:
    raise ValueError("Environment variable 'filmyfly' not found!")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}
