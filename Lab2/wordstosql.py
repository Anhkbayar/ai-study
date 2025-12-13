import mysql.connector
from collections import Counter

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "anka",
    database = "wordcount"
)

if db.is_connected():
    print("Holbogdson")

cursor = db.cursor()

with open("words.txt", "r", encoding="utf-8") as f:
    text = f.read()
    
words = text.split("\n")
word_count = Counter(words)

query = "INSERT INTO words(word, count) VALUES (%s, %s)"
for word, count in word_count.items():
    cursor.execute(query, (word, count))
    
db.commit()

print(cursor.rowcount, "rows")