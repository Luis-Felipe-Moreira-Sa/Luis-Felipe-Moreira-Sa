import sqlite3

hotelDB = sqlite3.connect('hotelDB.db')

cursor = hotelDB.cursor()

tabela = input("Nome da tabela: ")
cursor.execute(f'''
    SELECT * FROM {tabela}
''')
hotelDB.commit()
print(cursor.fetchall())
