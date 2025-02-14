import sqlite3
import os
import sys

tmp = " "

fname = os.getenv("fname")
db = os.getenv("db")

os.chdir("../../../../..")


print("looking for: ", fname)
if os.path.exists(fname):
    print("DB exists where we think it does")

print()
print("Attempting to connect to DB")

connection = sqlite3.connect(fname + db)

cursor = connection.cursor()

try:
    query = ".tables"
    cursor.execute(query)
    tables = cursor.fetchall()
    print()
except Exception as e:
    print("query did not work for following reason:", e)

connection.close()

print("Closed")
