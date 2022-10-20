from datetime import datetime
import sqlite3
import datetime
import sys
import os


# def st_dataBr():
#     dataSplit = mesDiaAno()
#     dia = dataSplit[1]
#     mes = dataSplit[0]
#     ano = dataSplit[2]
#     dataEstadia = f"{dia}/{mes}/{ano}"


def dataPassada(input_data_finaliza):
    
    # Convertendo input para datetime.datetime
    data_fim_estadia = datetime.strptime(input_data_finaliza, "%d/%m/%y")
    
    # apenas para demonstração atribui um valor 'hard-coded' para data_modificao
    data_modificacao = datetime.now()
    hora = int(data_modificacao.hour)
    if hora >= 12:
        datetime.timedelta(days=1)

    if data_modificacao <= data_fim_estadia:
        print('data_modificacao está entre o período selecionado')
    else:
        print('data_modificacao está fora do período selecionado')


def pushTabela(tabela):
    # tabela = input("Nome da tabela: ")
    cursor.execute(f'''
        SELECT * FROM {tabela}
    ''')
    hotelDB.commit()
    for dado in cursor.fetchall():
        print("\t", dado)


def pushTabelaColuna(tabela, coluna, atributo):
    # tabela = input("Nome da tabela: ")
    # coluna = input("Nome da coluna")
    cursor.execute(f'''
        SELECT * FROM {tabela}
        WHERE {coluna} = '{atributo}'
    ''')
    hotelDB.commit()
    print(cursor.fetchall())


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


hotelDB = sqlite3.connect('hotelDB.db')

cursor = hotelDB.cursor()


class Tabelas:
    tabela = ''
    linha = ''
    def push(self): 
        print(self.tabela)
        cursor.execute(f'''
            SELECT * FROM {self.tabela}
        ''')
        hotelDB.commit()
        return cursor.fetchall()
    
    def pushTabela(self):
        cursor.execute(f'''
            SELECT * FROM {self.tabela}
        ''')
        hotelDB.commit()
        print(cursor.fetchall())


class Responsavel(Tabelas):
    def login(self, cpfResponsavel):
        self.tabela = 'Responsavel'
        push = self.push()
        for resp in push:
            if(cpfResponsavel == resp[0]):
                ("Restrition Satisfation/")
                return True, resp[1]
        # (cpfs)
        return False, ""
        
        # else:
        #     cursor.execute(f'''
        #     INSERT INTO Responsavel(cpfResponsavel, nome)
        #     VALUES('{cpfResponsavel}', '{nome}');
        # ''')
        cursor.execute("SELECT * FROM Responsavel")
        hotelDB.commit()


class Consumo(Tabelas):
    dataConsumo = ""
    idTabelamento = ""
    cpfCliente = ""
    def __init__(self, dataConsumo, idTabelamento, cpfCliente):
        self.tabela = "Consumo"
        cursor.execute(f'''
            INSERT INTO {self.tabela}(dataConsumo, idTabelamento, cpfCliente)
            VALUES('{dataConsumo}', '{idTabelamento}', '{cpfCliente}');
        ''')
        hotelDB.commit()


class Cliente(Tabelas):
    cpfCliente = ""
    nomeCliente = ""
    telefone = ""
    dataNascimento = ""
    valorConsumo = 0.0
    tabela = 'Cliente'
    linha = 'valorConsumo'
    def login(self, cpfCliente) -> None:
        self.tabela = 'Cliente'
        dados = self.push()
        for resp in dados:
            if(cpfCliente == resp[1]):
                self.cpfCliente = cpfCliente
                self.nomeCliente = resp[2]
                self.telefone = resp[3]
                self.dataNascimento = resp[4]
                self.valorConsumo = resp[5]        
                return True
        return False


    def cadastrar(self, cpfCliente, nomeCliente, telefone, dataNascimento, valorConsumo) -> None:
        self.cpfCliente = cpfCliente
        self.nomeCliente = nomeCliente
        self.telefone = telefone
        self.dataNascimento = dataNascimento
        self.valorConsumo = float(valorConsumo)
        self.tabela = 'Cliente'
        self.linha = 'valorConsumo'
        print("Cpf Cliente: ", cpfCliente)
        cursor.execute(f'''
            INSERT INTO {self.tabela}(cpfCliente, nomeCliente, telefone, dataNascimento, valorConsumo)
            VALUES('{cpfCliente}', '{nomeCliente}', '{telefone}', '{dataNascimento}', '{valorConsumo}');
        ''')
        # cursor.execute("SELECT * FROM Cliente")
        hotelDB.commit()
        # (cursor.fetchall())

    def changeDice(self, atributo):
        # print(f'''
        #     UPDATE {self.tabela}
        #     SET {self.linha} = {atributo}
        #     WHERE cpfCliente = '{self.cpfCliente}'
        # ''')
        cursor.execute(f'''
            UPDATE {self.tabela}
            SET {self.linha} = {atributo}
            WHERE cpfCliente = '{self.cpfCliente}'
        ''')
        hotelDB.commit()

    def __str__(self):
        print("cpfCliente: ",
            self.cpfCliente,
            "\nnomeCliente: ",
            self.nomeCliente,
            "\ntelefone: ",
            self.telefone,
            "\ndataNascimento: ",
            self.dataNascimento,
            "\nvalorConsumo: ",
            self.valorConsumo
        )
        return self.cpfCliente


class Estadia(Tabelas):
    def __init__(self, cpfResponsavel, cpfCliente, numeroQuarto, dataEstadia, dataDesocupa) -> None:
        self.tabela = 'Estadia'
        cursor.execute(f'''
            INSERT INTO {self.tabela}(cpfResponsavel, cpfCliente, numeroQuarto, dataEstadia, dataDesocupa)
            VALUES('{cpfResponsavel}', '{cpfCliente}', '{numeroQuarto}', '{dataEstadia}', '{dataDesocupa}')
        ''')
        hotelDB.commit()


class Tabelamento(Tabelas):
    idTabelamento = 0
    nome = ''
    preco = 0.0
    
    def __init__(self, idTabelamento) -> None:
        self.tabela = 'Tabelamento'
        for resp in  self.push():
            if(resp[0] == idTabelamento):
                self.nome = resp[1]
                self.preco = resp[2]
        
    def cadastrar(self, nome, preco):
        self.tabela = 'Tabelamento'
        self.nome = nome
        self.preco = preco
        cursor.execute(f'''
            INSERT INTO {self.tabela}(nome, preco)
            VALUES('{nome}', '{preco}')
        ''')
        hotelDB.commit()


class Quartos(Tabelas):
    tabela = 'Quartos'


    def cadastrar(self):
        self.linha =  'estado'
        tipos = ['Simples', 'Duplo', 'Casal', 'Luxo']
        print('0 - Simples\t', '1 - Duplo\t', '2 - Casal\t', '3 - Luxo')
        self.quartos = self.push()
        tipo = int(input("TIPO DO QUARTO -> "))
        for dado in self.push():
            if "DESOCUPADO" == dado[3] and tipos[tipo] == dado[1]:
                self.changeDice(dado[0], "OCUPADO")
                self.numeroQuarto = dado[0]
                self.tipo = dado[1]
                self.diaria = dado[2]
                self.estado = dado[3]
                return dado
        return ["Sem Vagas"]


    def changeDice(self, numeroQuarto, atributo):
        cursor.execute(f'''
            UPDATE {self.tabela}
            SET {self.linha} = "{atributo}"
            WHERE numeroQuarto = {numeroQuarto};
        ''')
        hotelDB.commit()

def reservar(cpfResponsavel, cpfCliente, diarias):
    quartos = Quartos()
    dadosQuarto = quartos.cadastrar()
    print(dadosQuarto)
    if (dadosQuarto[0] == "Sem Vagas"):
        return ""
    dataSplit = mesDiaAno()
    dia = dataSplit[1]
    mes = dataSplit[0]
    ano = dataSplit[2]
    dataEstadia = f"{dia}/{mes}/{ano}"
    dataDesocupa = f"{int(dia)+diarias}/{mes}/{ano}"
    numeroQuarto = dadosQuarto[0]
    Estadia(cpfResponsavel, cpfCliente, numeroQuarto, dataEstadia, dataDesocupa)
    return dadosQuarto[2]


def mesDiaAno():
    return datetime.datetime.now().strftime("%x").split('/')


def pagarDivida(cpfCliente, valor):
    cliente = Cliente()
    cliente.login(cpfCliente)
    dividaAtual = cliente.valorConsumo - valor
    if cliente.valorConsumo < valor:
    #     print("Troco de R$", -(dividaAtual))
        dividaAtual = 0
    cliente.changeDice(dividaAtual)


def desocuparQuarto():
    pushTabela("Estadia")
    numeroQuarto = int(input("Numero do quarto -> "))
    quart = Quartos()
    isRead = False
    quartos = []
    for dado in quart.push():
        quartos.append(dado[0])
    if numeroQuarto in quartos:
        try:
            quart.changeDice("DESOCUPADO", numeroQuarto)
        except:
            return isRead    
    return isRead



isLogin = False
cpfResponsavel = input("CPF Responsável: ")
responsavel = Responsavel()
isLogin, nomeResponsavel = responsavel.login(cpfResponsavel)
if not isLogin:
    restart_program()
# print(isLogin)
# while not isLogin:
#     # cpfResponsavel = input("CPF Responsável: ")
#     cpfResponsavel = "07429224300"
#     responsavel = Responsavel()
#     isLogin, nomeResponsavel = responsavel.login(cpfResponsavel)


cpfCliente = input("CPF Cliente: ")
# cpfCliente = "07429224300"
cliente = Cliente()
isLogin = cliente.login(cpfCliente)
if not isLogin:
    # cpfCliente = input("CPF Cliente: ")
    # cpfCliente = "07429224300"
    nomeCliente = input("Nome: ")
    # nomeCliente = "Luis Felipe"
    telefone = input("Telefone: ")
    # telefone = "89981066633"
    dataNascimento = input("Data de Nascimento: ")
    # dataNascimento = "27/08/1999"
    # valorConsumo = input("Valor do Consumo: ")
    valorConsumo = 0.0
    cliente.cadastrar(cpfCliente, nomeCliente, telefone, dataNascimento, valorConsumo)
print(cliente)
while True:
    print("1 - Reservar")
    print("2 - Adicionar Consumo")
    print("3 - Pagar Debitos")
    print("4 - Sair")
    print("5 - Relatório")
    term = input("  -> ")
    match term:
        case "1":
            diarias = int(input("Diarias -> "))
            print(cpfResponsavel)
            valorQuarto = reservar(cpfResponsavel, cpfCliente, diarias)
            cliente.changeDice(valorQuarto*diarias)
            cliente.pushTabela()
            isLogin = cliente.login(cliente.cpfCliente)
            continue
        case "2":
            print("1 - Adicionar produto ao consumo")
            print("2 - Adicionar valor ao consumo")
            term = input("")
            match term:
                case "1":
                    pushTabela(
                        "Tabelamento")
                    dataSplit = mesDiaAno()
                    dia = dataSplit[1]
                    mes = dataSplit[0]
                    ano = dataSplit[2]
                    dataConsumo = f"{dia}/{mes}/{ano}"
                    print(dataConsumo)
                    # idTabelamento = 2
                    idTabelamento = int(input("Codigo: "))
                    tabelamento = Tabelamento(idTabelamento)
                    consumo = Consumo(dataConsumo, idTabelamento, cpfCliente)
                    cliente.valorConsumo = tabelamento.preco + cliente.valorConsumo
                    cliente.changeDice(cliente.valorConsumo)
                    cliente.pushTabela()
                    continue
                case "2":
                    # consumido = 20.0
                    consumido = float(input("Valor "))
                    cliente.valorConsumo = consumido + cliente.valorConsumo
                    cliente.changeDice(cliente.valorConsumo)
                    continue
            continue
        # case "3":
        #     pushTabela("Quartos")
        #     desocuparQuarto()
        #     continue
        case "3":
            print("Divida de R$", cliente.valorConsumo)
            print("1 - Pagar divida total: ")
            print("2 - Pagar divida parcial: ")
            term = input("  -> ")
            match term:
                case "1":
                    pagarDivida(cliente.cpfCliente, cliente.valorConsumo)
                    cliente.valorConsumo = 0.0
                    continue
                case "2":
                    valor = float(input("Valor pago -> "))
                    pagarDivida(cliente.cpfCliente, valor)
                    cliente.valorConsumo = cliente.valorConsumo - valor
                    if(cliente.valorConsumo < 0):
                        cliente.valorConsumo = 0
                    continue
                case _:
                    break
        case "4":
            restart_program()
        case "5":
            # pushTabela()
            # print("1 - Responsavel")
            print("\t2 - Cliente")
            print("\t3 - Quartos")
            print("\t4 - Estadia")
            print("\t5 - Tabelamento de Produtos")
            print("\t6 - Consumo")
            term = input("\t      -> ")
            match term:
                case "1":
                    pushTabelaColuna(
                        "Responsavel",
                        "cpfResponsavel",
                        cpfResponsavel)
                    continue
                case "2":
                    pushTabelaColuna(
                        "Cliente",
                        "cpfCliente",
                        cliente.cpfCliente)
                    continue
                case "3":
                    pushTabela(
                        "Quartos")
                    continue
                case "4":
                    pushTabela(
                        "Estadia")
                    continue
                case "5":
                    pushTabela(
                        "Tabelamento")
                    continue
                case "6":
                    pushTabelaColuna(
                        "Consumo",
                        "cpfCliente",
                        cliente.cpfCliente)
                    continue
                case _:
                    break
        case _:
            break


((" " * 30) + nomeResponsavel)
