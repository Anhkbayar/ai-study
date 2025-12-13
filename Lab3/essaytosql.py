import mysql.connector
from collections import Counter
import re

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "anka",
    database = "wordcount"
)

if db.is_connected():
    print("Holbogdson")

cursor = db.cursor()
# print("Utga")
# text = input()

with open("essay.txt", "r", encoding="utf-8") as f:
    text = f.read()

words = re.findall(r"\w+", text.lower())    
word_count = Counter(words)

query = "INSERT INTO essaywords(word, count) VALUES (%s, %s)"
for word, count in word_count.items():
    cursor.execute(query, (word, count))

db.commit()

print(cursor.rowcount, "rows")