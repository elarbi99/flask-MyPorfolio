import sqlite3 as sql
from os import path
ROOT=path.dirname(path.relpath((__file__)))

def create_data(names,comment):
    con=sql.connect(path.join(ROOT,'user.db'))
    cur=con.cursor()
    cur.execute('insert into testimonial (names,comment) values(?, ?)', (names, comment))
    con.commit()
    con.close()


def get_data():
     con=sql.connect(path.join(ROOT,'user.db'))
     cur=con.cursor()
     cur.execute('select * from testimonial')
     testimonial=cur.fetchall()
     return testimonial