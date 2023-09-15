import sqlite3, random
from models import Person


def getNewId():
    return random.getrandbits(28)

# people = [
#     {
#         'name': 'Sidney',
#         'track': 'Backend',
#         'age': 22
#     },
#     {
#         'name': 'Mark',
#         'track': 'Frontend',
#         'age': 25
#     },
#     {
#         'name': 'Chris',
#         'track': 'Mobile',
#         'age': 21
#     },
# ]

def connect():
    conn = sqlite3.connect('people.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS people (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, track TEXT, age INTEGER)")
    conn.commit()
    conn.close()
    # for i in people:
    #     p = Person(i['name'], i['track'], i['age'])
    #     insert(p)

def insert(per):
    conn = sqlite3.connect('people.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO people (name, track, age) VALUES (?,?,?)", (
        per.name,
        per.track,
        per.age
    ))
    conn.commit()
    conn.close()

def view(personid):
    conn = sqlite3.connect('people.db')
    cur = conn.cursor()
    cur.execute("SELECT name, track, age FROM people WHERE id = ?", (personid,))
    person = cur.fetchone()
    conn.close()
    return person

def check(name):
    conn = sqlite3.connect('people.db')
    cur = conn.cursor()
    cur.execute("SELECT id, name, track, age FROM people WHERE name = ?", (name,))
    person = cur.fetchone()
    conn.close()
    return person
    
def update(name, track, age, personid):
    conn = sqlite3.connect('people.db')
    cur = conn.cursor()
    cur.execute("UPDATE people SET name=?, track=?, age=? WHERE id=?", (name, track, age, personid))
    conn.commit()
    conn.close()

def delete(personid):
    conn = sqlite3.connect('people.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM people WHERE id=?", (personid,))
    conn.commit()
    conn.close()

def getid(person):
    conn = sqlite3.connect('people.db')
    cur = conn.cursor()
    cur.execute("SELECT id FROM people WHERE name=?", (person,))
    result = cur.fetchone()
    conn.close()
    return result


# def deleteAll():
#     conn = sqlite3.connect('people.db')
#     cur = conn.cursor()
#     cur.execute("DELETE FROM people")
#     conn.commit()
#     conn.close()
