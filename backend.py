from ast import Return
import sqlite3

def connect():
    conn = sqlite3.connect("movies.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS movie (id INTEGER PRIMARY KEY, title text, director text, year integer, rating text)")
    conn.commit()
    conn.close()


def insert(title, director, year, rating):
    conn = sqlite3.connect("movies.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO movie VALUES (NULL,?,?,?,?)", (title, director, year, rating))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("movies.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM movie")
    rows = cur.fetchall()
    conn.close()
    return rows

def view_2():
    conn = sqlite3.connect("movies.db")
    table = conn.execute("SELECT * FROM movie")
    for i in table:
        print(i)
    conn.close()

def search(title="", director="", year="", rating=""):
    conn = sqlite3.connect("movies.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM movie WHERE title=? OR director=? or year=? or rating=?", (title, director, year, rating))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("movies.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM movie WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update(id, title, director, year, rating):
    conn = sqlite3.connect("movies.db")
    cur = conn.cursor()
    cur.execute("UPDATE movie SET title=?, director=?, year=?, rating=? WHERE id=?", (title, director, year, rating, id))
    conn.commit()
    conn.close()

def selection(id):
    conn = sqlite3.connect("movies.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM movie WHERE id=?", (id,))
    rows = cur.fetchall()
    conn.close()
    return rows

connect()
# update()
# delete(7)
# insert()
# view_2()
# print()
# print(view())
# print(selection(1))
