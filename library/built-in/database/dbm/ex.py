import dbm

# :::::::::::::::::::::::::::::::::::::::::::::::::::

db = dbm.open('test_db', 'c')
db['color'] = 'yellow'
db['base'] = 'postgresql'

# print(len(db)) # 2
# print(db['base']) # b'postgresql'

db.close()