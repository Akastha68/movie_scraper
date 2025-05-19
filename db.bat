import sqlite3

conn = sqlite3.connect("films.db")
cursor = conn.cursor()

def setup_tables():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        image_url TEXT
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS movie_links (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        movie_id INTEGER,
        quality TEXT,
        video_url TEXT,
        FOREIGN KEY(movie_id) REFERENCES movies(id)
    )
    """)
    conn.commit()

def insert_movie(title, image_url):
    cursor.execute("INSERT INTO movies (title, image_url) VALUES (?, ?)", (title, image_url))
    conn.commit()
    return cursor.lastrowid

def insert_video_link(movie_id, quality, video_url):
    cursor.execute("INSERT INTO movie_links (movie_id, quality, video_url) VALUES (?, ?, ?)",
                   (movie_id, quality, video_url))
    conn.commit()
