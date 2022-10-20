import sqlite3

hotelDB = sqlite3.connect('hotelDB.db')

cursor = hotelDB.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Responsavel(
        cpfResponsavel VARCHAR(17) NOT NULL,
        nome VARCHAR(45) NOT NULL,
        PRIMARY KEY (cpfResponsavel)
    );
''')

# cursor.execute('''
#     INSERT INTO Responsavel(cpfResponsavel, nome)
#     VALUES("07429224300", "Felipe Moreira")
# ''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Cliente(
        idCliente INTEGER,
        cpfCliente VARCHAR(17) NOT NULL,
        nomeCliente VARCHAR(45) NOT NULL,
        telefone VARCHAR(20) NOT NULL,
        dataNascimento VARCHAR(20) NOT NULL,
        valorConsumo DOUBLE,
        PRIMARY KEY (idCliente)
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Quartos(
        numeroQuarto INTEGER NOT NULL,
        tipo INTEGER NOT NULL,
        diaria DOUBLE NOT NULL,
        estado VARCHAR(10),
        PRIMARY KEY(numeroQuarto)
    );
''')

# UPDATE Customers
# SET ContactName = 'Alfred Schmidt', City= 'Frankfurt'
# WHERE CustomerID = 1;

# try:
#     cursor.execute('''
#         INSERT INTO Quartos(numeroQuarto, tipo, diaria, estado)
#         VALUES("101", "Simples", 200.0, "DESOCUPADO")
#         VALUES("102", "Simples", 200.0, "DESOCUPADO")
#         VALUES("201", "Duplo", 230.0, "DESOCUPADO")
#         VALUES("202", "Duplo", 230.0, "OCUPADO")
#         VALUES("301", "Casal", 250.0, "DESOCUPADO")
#         VALUES("302", "Casal", 250.0, "DESOCUPADO")
#         VALUES("401", "Luxo", 300.0, "DESOCUPADO")
#         VALUES("402", "Luxo", 300.0, "DESOCUPADO")
#     ''')
# except:
#     pass

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Estadia(
        idEstadia INTEGER,
        cpfResponsavel VARCHAR(20) NOT NULL,
        cpfCliente VARCHAR(20) NOT NULL,
        numeroQuarto INT NOT NULL,
        dataEstadia DATE NOT NULL,
        dataDesocupa DATE NOT NULL,
        PRIMARY KEY (idEstadia)
        FOREIGN KEY (cpfResponsavel) REFERENCES Responsavel(cpfResponsavel),
        FOREIGN KEY (cpfCliente) REFERENCES Cliente(cpfCliente)
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Tabelamento(
        idTabelamento INTEGER,
        nome VARCHAR(30) NOT NULL,
        preco DOUBLE NOT NULL,
        PRIMARY KEY(idTabelamento)
    );
''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS Consumo(
        idConsumo INTEGER,
        dataConsumo DATETIME,
        idTabelamento INTEGER NOT NULL,
        cpfCliente VARCHAR(20) NOT NULL,
        PRIMARY KEY (idConsumo)
        FOREIGN KEY(idTabelamento) REFERENCES Tabelamento(idTabelamento)
    );
''')

hotelDB.commit()
# cursor.execute("SET SQL_MODE=@OLD_SQL_MODE;")
# cursor.execute("SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;")
# cursor.execute("SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;")
