import mysql.connector

dbconfig = {
  'host': '127.0.0.1',
  'user': 'personapi',
  'password': '',
  'database': 'personapiDB',
}

conn = mysql.connector.connect(**dbconfig)
cursor = conn.curson()

cursor.execute(
  """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    track VARCHAR(32) NOT NULL,
    age INT NOT NULL
);
"""
)
conn.commit()

def create_person(name, track, age):
  cursor.execute("INSERT INTO users (name, track, age) VALUES (%s, %s, %s)", (name, track, age))
  conn.commit()
  