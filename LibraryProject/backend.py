# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 20:35:11 2017

@author: ghisl
"""

import sqlite3
# Create a connection for the database

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    # create a table in the database
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer,isbn integer)")
    conn.commit()
    conn.close()


def insert(title,author,year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    # NULL will take care of the id key in the table book
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()
    
def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall() # we getting the data, rather commit a change 
    conn.close()
    return rows # show all the rows in the table book

def search(title = "",author = "",year = "",isbn = ""):
    # "" are there in case the user wants to only one parameter or more
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))
    rows = cur.fetchall() # we getting the data, rather commit a change 
    conn.close()
    return rows # show all the rows in the table book

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    # create a table in the database
    cur.execute("DELETE FROM book WHERE id = ?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    # create a table in the database
    # make sure id is last in the brackets because python follows the set order
    cur.execute("UPDATE book SET title = ?,author = ?,year = ?,isbn = ? WHERE id = ?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()


# We make sure that all these functions are active once we call them after the backend.py is imported
connect()
#insert("The Sun","John Smith",2010,1345689)
#delete(2)
print(view())
update(4,"The moon","John Smooth",1988,8976546)
print(view())
print(search(author = "John Smith"))