import sqlite3

con = sqlite3.connect('Example1.db')

cur = con.cursor()

cur.execute('''create table student (sno integer,sname text)''')

con.close()