from ast import Return
import sqlite3

def connect():
    conn = sqlite3.connect("servers.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS server (id INTEGER PRIMARY KEY, name text)")
    cur.execute("CREATE TABLE IF NOT EXISTS maps (id INTEGER, name text)")
    conn.commit()
    conn.close()


def insert(name):
    conn = sqlite3.connect("servers.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO server VALUES (NULL,?)", (name,))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("servers.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM server")
    rows = cur.fetchall()
    conn.close()
    return rows

def view_2():
    conn = sqlite3.connect("servers.db")
    table = conn.execute("SELECT * FROM server")
    for i in table:
        print(i)
    conn.close()

def search(title="", director="", year="", rating=""):
    conn = sqlite3.connect("servers.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM server WHERE title=? OR director=? or year=? or rating=?", (title, director, year, rating))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("servers.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM server WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update(id, title, director, year, rating):
    conn = sqlite3.connect("servers.db")
    cur = conn.cursor()
    cur.execute("UPDATE server SET title=?, director=?, year=?, rating=? WHERE id=?", (title, director, year, rating, id))
    conn.commit()
    conn.close()

def selection(id):
    conn = sqlite3.connect("servers.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM server WHERE id=?", (id,))
    rows = cur.fetchall()
    conn.close()
    return rows

connect()
# update()
# delete(7)
# insert("")
# view_2()
# print()
print(view())
# print(selection(1))
