import sqlite3

user_input = input()

cursor = sqlite3.connect("test.db").cursor()

cursor.execute(
    "SELECT * FROM users WHERE id=" + user_input
)