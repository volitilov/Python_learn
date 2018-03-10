import sqlite3

# ::::::::::::::::::::::::::::::::::::::::::::::::

conn = sqlite3.connect('test_db.db')
curs = conn.cursor()
# curs.execute(''' CREATE TABLE zoo
# 	(critter VARCHAR(20) PRIMARY KEY,
# 	count INT,
# 	damages FLOAT)''')

curs.execute('INSERT INTO zoo VALUES("duck", 5, 0.0)')
curs.execute('INSERT INTO zoo VALUES("bear", 2, 1000.0)')

ins = 'INSERT INTO zoo (critter, count, damages) VALUES(?, ?, ?)'
curs.execute(ins, ('weasel', 1, 2000.0))

curs.execute('SELECT * FROM zoo')
rows = curs.fetchall()
print(rows)
# [('duck', 5, 0.0), ('bear', 2, 1000.0), ('weasel', 1, 2000.0)]


curs.execute('SELECT * from zoo ORDER BY count')
rows = curs.fetchall()
print(rows)
# [('weasel', 1, 2000.0), ('bear', 2, 1000.0), ('duck', 5, 0.0)]

curs.execute('''SELECT * FROM zoo WHERE
	damages = (SELECT MAX(damages) FROM zoo)''')
res = curs.fetchall()
print(res)
# [('weasel', 1, 2000.0)]

curs.close()
conn.close()