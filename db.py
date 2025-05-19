import sqlite3

conn = sqlite3.connect("films.db")
cursor = conn.cursor()

def setup_tables():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT UNIQUE,  -- Prevent duplicate titles
        image_url TEXT
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS movie_links (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        movie_id INTEGER,
        quality TEXT,
        video_url TEXT UNIQUE,  -- Prevent duplicate video_urls
        FOREIGN KEY(movie_id) REFERENCES movies(id)
    )
    """)
    conn.commit()

def insert_movie(title, image_url):
    # Check if movie with same title already exists
    cursor.execute("SELECT id FROM movies WHERE title = ?", (title,))
    existing = cursor.fetchone()
    if existing:
        return existing[0]  # Return existing movie's ID
    else:
        cursor.execute("INSERT INTO movies (title, image_url) VALUES (?, ?)", (title, image_url))
        conn.commit()
        return cursor.lastrowid

def insert_video_link(movie_id, quality, video_url):
    cursor.execute("INSERT INTO movie_links (movie_id, quality, video_url) VALUES (?, ?, ?)",
                   (movie_id, quality, video_url))
    conn.commit()
