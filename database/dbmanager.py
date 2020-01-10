import sqlite3
import hashlib
import random


class DatabaseManager(object):
    def __init__(self):
        self.conn = sqlite3.connect('example-pwd.db')
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute("SELECT * FROM user")
        except sqlite3.OperationalError:
            # Create table
            self.cursor.execute('''CREATE TABLE user
                          (id INTEGER AUTO_INCREMENT,
                           username TEXT NOT NULL,
                           password TEXT NOT NULL,
                           salt TEXT NOT NULL,
                           PRIMARY KEY (id))''')

    def save_new_username_correct(self, username, password):
        salt = str(random.random())
        digest = salt + password
        for i in range(1000):
            digest = hashlib.sha256(digest.encode('utf-8')).hexdigest()

        self.cursor.execute("INSERT INTO user VALUES (NULL,?,?,?)",
                            (username, digest, salt))
        self.conn.commit()

    def check_for_username_correct(self, username, password):
        salt = self.cursor.execute("SELECT salt FROM user WHERE username=?",
                                   (username,)).fetchall()[0][0]
        digest = str(salt) + password
        for i in range(1000):
            digest = hashlib.sha256(digest.encode('utf-8')).hexdigest()
        rows = self.cursor.execute("SELECT * FROM user WHERE username=?",
                                   "and password=?",
                                   (username, digest))
        self.conn.commit()
        results = rows.fetchall()

        if results:
            return True
        else:
            return False

    def close(self):
        self.conn.close()

    def clean_up(self):
        self.cursor.execute('''DROP TABLE user''')
