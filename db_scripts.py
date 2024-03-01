import sqlite3

db_name = "blog.db"
connection = None
cursor = None

def open():
    global connectioin,cursor
    connectioin = sqlite3.connect(db_name)
    cursor = connectioin.cursor()

def new_func():
    return db_name

def close():
    cursor.close()
    connectioin.close()

def getUser():
    open()
    cursor.execute('''SELECT * FROM user''')
    user = cursor.fetchone()
    close()
    return user

def getIdByCategory(category_name):
    open()
    cursor.execute(''' SELECT  category_id
                       FROM category
                       WHERE category_name = (?) 
                       ''', [category_name])
    category_id = cursor.fetchone()[0]
    return category_id

def getPostsByCategory(category_name):
    open()
    cursor.execute(''' SELECT * FROM post, category
                       WHERE category_name = (?)
                       AND post.category_id = category.category_id
                       ORDER BY post_datetime DESC 
                       ''', [category_name])
    posts = cursor.fetchall()
    close()
    return posts

def addPost(category_id, post_text):
    open()
    cursor.execute('''INSERT INTO post (category_id, post_text)
                      VALUES ((?), (?)))''', [category_id, post_text])
    connection.commit()
    close()