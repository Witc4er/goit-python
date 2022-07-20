import sqlite3


def create_db():
    with open('./hw_create_db.sql', 'r') as f:
        sql = f.read()

    with sqlite3.connect('./hw.db') as conn:
        curs = conn.cursor()
        curs.executescript(sql)


if __name__ == '__main__':
    create_db()