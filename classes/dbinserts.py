import sqlite3

hotelDB = sqlite3.connect('hotelDB.db')

cursor = hotelDB.cursor()

cursor.execute('''
    INSERT INTO Responsavel(cpfResponsavel, nome)
    VALUES("07429224300", "Felipe Moreira")
''')

# cursor.execute('''
#     INSERT INTO Cliente(cpfCliente, nomeCliente, telefone, dataNascimento, valorConsumo)
#     VALUES('07429224300', 'Luis Felipe', '89981066633', 'dataNascimento', 20.0)
# ''')

cursor.execute('''
        INSERT INTO Quartos(numeroQuarto, tipo, diaria, estado)
        VALUES
        (101, "Simples", 200.0, "DESOCUPADO"),
        (102, "Simples", 200.0, "DESOCUPADO"),
        (201, "Duplo", 230.0, "DESOCUPADO"),
        (202, "Duplo", 230.0, "DESOCUPADO"),
        (301, "Casal", 250.0, "DESOCUPADO"),
        (302, "Casal", 250.0, "DESOCUPADO"),
        (401, "Luxo", 300.0, "DESOCUPADO"),
        (402, "Luxo", 300.0, "DESOCUPADO");
    ''')

cursor.execute('''
    INSERT INTO Tabelamento(nome, preco)
    VALUES("Agua Mineral", 3.8),
    ("Burguer", 12.0),
    ("Garrafa Vinho", 190),
    ("Coca lata", 6);
''')

hotelDB.commit()