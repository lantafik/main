import sqlite3

def sql_add_date(name, age, user_tg_id, female):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO users (name, age, user_tg_id, sex) VALUES (?, ?, ?, ?)', (name, age, user_tg_id, female))

    connection.commit()
    connection.close()

def text(text):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO users (text) VALUES (?)', (text))

    connection.commit()
    connection.close()

def clear_db():
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute('DROP TABLE users')
    cursor.execute('''CREATE TABLE users(
    name VARCHAR,
    user_id INTEGER,
    age INTEGER,
    user_tg_id INTEGER,
    sex INTEGER,
    text VARCHAR
    )
    ''')

    connection.commit()
    connection.close()
clear_db()