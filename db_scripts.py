import sqlite3

db_name = "blog.db"
connectioin = None
cursor = None

def open():
    global connectioin,cursor
    connectioin = sqlite3.connect(db_name)
    cursor = connectioin.cursor()

def close():
    cursor.close()
    connectioin.close()