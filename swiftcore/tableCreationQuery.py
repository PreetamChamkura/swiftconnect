import sqlite3

conn = sqlite3.connect('swiftie.db')
cursor = conn.cursor()

# create user table with all fields mandatory, username and email are unique
cursor.execute("""
CREATE TABLE IF NOT EXISTS user(
	username TEXT PRIMARY KEY,
	password TEXT NOT NULL,
	email TEXT NOT NULL UNIQUE
	)	
""")

#create a playlist table
cursor.execute("""
CREATE TABLE IF NOT EXISTS playlist (
	playlist_id INTEGER PRIMARY KEY,
	username TEXT,
	FOREIGN KEY (username) REFERENCES user(username)
	)
""")

#create a tour table
cursor.execute("""
CREATE TABLE IF NOT EXISTS tour (
	tour_id INTEGER PRIMARY KEY AUTOINCREMENT,
	location TEXT NOT NULL,
	era TEXT,
	time TEXT,
	date TEXT,
	username TEXT,
	playlist_id INTEGER,
	FOREIGN KEY (username) REFERENCES user(username),
	FOREIGN KEY (playlist_id) REFERENCES playlist(playlist_id)
	)
""")

#create a outfit table
cursor.execute("""
CREATE TABLE IF NOT EXISTS outfit (
	outfit_id INTEGER PRIMARY KEY,
	image_url TEXT
	)
""")

#create a MerchWishlist Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS merch_wishlist(
	wishlist_id INTEGER PRIMARY KEY,
	username TEXT,
	FOREIGN KEY (username) REFERENCES user(username)
	)
""")

#create a song table
cursor.execute("""
CREATE TABLE IF NOT EXISTS song (
	song_id INTEGER PRIMARY KEY,
	title TEXT NOT NULL,
	album TEXT,
	era TEXT
	)
""")

#SpecialSong table creation
cursor.execute("""
CREATE TABLE IF NOT EXISTS special_song (
	special_song_id INTEGER PRIMARY KEY,
	song_id INTEGER,
	FOREIGN KEY (song_id) REFERENCES song(song_id)
	)
""")

#create tour outfit table
cursor.execute("""
CREATE TABLE IF NOT EXISTS tour_outfit (
	tour_id INTEGER,
	outfit_id INTEGER,
    FOREIGN KEY (tour_id) REFERENCES tour(tour_id),
	FOREIGN KEY (outfit_id) REFERENCES outfit(outfit_id)
	)
""")

#create playlist_song table
cursor.execute("""
CREATE TABLE IF NOT EXISTS playlist_song (
	playlist_id INTEGER,
	song_id INTEGER,
	FOREIGN KEY (playlist_id) REFERENCES playlist(playlist_id),
	FOREIGN KEY (song_id) REFERENCES song(song_id)
	)
""")

#creates tour special song table
cursor.execute("""
CREATE TABLE IF NOT EXISTS tour_special_song(
	tour_id INTEGER,
	song_id INTEGER,
	FOREIGN KEY (tour_id) REFERENCES tour(tour_id),
	FOREIGN KEY (song_id) REFERENCES song(song_id)
	)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS merch (
    merch_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    image_url TEXT
)
""")


conn.commit()
conn.close()

print("Table creation successful")
