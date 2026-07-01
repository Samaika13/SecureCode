query = "SELECT * FROM users"

name = input()

sql = (
    "SELECT * FROM users "
    + name
)

cursor.execute(sql)