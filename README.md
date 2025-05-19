```bash
python main.py
```

- Automatically fetches movie data and stores it in `films.db`.
- Supports multiple quality links per movie.

---

## Database Schema

### movies
 ________________________
| id | title | image_url |
|----|-------|-----------|

### movie_links
 _____________________________________
| id | movie_id | quality | video_url |
|----|----------|---------|-----------|

---

## Requirements

- Python 3.10 or newer
- Modules:
  - requests
  - beautifulsoup4
  - sqlite3
  - python-dotenv
  - urllib.parse

(Install via `requirements.txt`)

---

## Future Enhancements

- [ ] Add pagination and multiple-page scraping
- [ ] Enhanced error handling and logging
- [ ] Proxy/user-agent rotation for stealth scraping
- [ ] Admin panel or frontend integration (Flask or PHP)
- [ ] Schedule scraping tasks (cronjobs or Windows tasks)

---

## License

This project is licensed under the [MIT License](./LICENSE)

---

**Created with passion by Shadow Coder (Akash)**
