import sqlite3


class DataManipulation():
    def __init__(self):
        pass

    def insertButtonCustom(self):
        pass

    def updateButtonCustom(self):
        pass


conn = sqlite3.connect('data.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE ButtonCustom (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        sourceSample TEXT NOT NULL,
    );
""")

conn.close()