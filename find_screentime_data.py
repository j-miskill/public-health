import sqlite3
import os
import sys

db = os.getenv("DB")
print("looking for: ", f"../../{db}")
if os.path.exists(f"../../{db}"):
    print("DB exists where we think it does")

print()
print("Attempting to connect to DB")

connection = sqlite3.connect(f"./../{db}")

cursor = connection.cursor()

try:
    query = "show tables"
    cursor.execute(query)
    response = cursor.fetchall()
    print(response)
except Exception as e:
    print("query did not work for following reason:", e)

connection.close()

print("Closed")
