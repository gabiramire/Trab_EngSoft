from user import Cook
from receita import Receita
from Mapeadores.mapReceita import mapReceita


class mapCook:

    def __init__(self, connection):
        self.connection = connection
        self.mapReceita = mapReceita(connection)

    def get(self, codUser):
        cursor = self.connection.cursor()
        consulta = '''SELECT login, senha, email, lista_receitas FROM USER WHERE codUser=\'''' + codUser + '''\' AND TIPO=\'3\' '''
        cursor.execute(consulta)
        registro = cursor.fetchone()
        if registro != None:
            login = registro[0]
            senha = registro[1]
            email = registro[2]
            lista_receitas = registro[3]
            cook = Cook(login, senha, email, codUser)
            if lista_receitas != None:
                cook.lista_receitas = self.mapReceita.get(lista_receitas)
            return cook
        else:
            return None

    def put(self, cook):
        if self.get(cook.codUser) != None:
            self.atualiza_cook_existente(cook)
        else:
            self.insere_novo_cook(cook)

    def insere_novo_cook(self, cook):
        cursor = self.connection.cursor()
        if cook.lista_receitas == None:
            consulta = '''INSERT INTO USER (login, senha, email, codUser, tipo) VALUES (%s,%s,%s,\'3\')'''
            valores = (cook.login, cook.senha, cook.email, str(cook.codUser))
        else:
            consulta = '''INSERT INTO USER (login, senha, email, codUser, lista_receitas, tipo) VALUES (%s,%s,%s,%s,%s,\'3\')'''
            valores = (cook.cpf, cook.nome, cook.endereco, str(cook.codUser), str(cook.lista_receitas))
        cursor.execute(consulta,valores)
        self.connection.commit()

    def atualiza_cook_existente(self, cook):
        cursor = self.connection.cursor()
        if cook.lista_receitas == None:
            consulta = '''UPDATE USER SET login=%s,senha=%s, email=%s WHERE codUser=%s AND tipo=\'3\' '''
            valores = (cook.login, cook.senha, cook.email, str(cook.codUser))
        else:
            consulta = '''UPDATE USER SET login=%s,senha=%s, email=%s, lista_receitas=%s WHERE codUser=%s AND tipo=\'3\' '''
            valores = (cook.login, cook.senha, cook.email, str(cook.codUser), str(cook.lista_receitas), cook.cpf)
        cursor.execute(consulta,valores)
        self.connection.commit()

    def remove(self, codUser):
        cursor = self.connection.cursor()
        query = '''DELETE FROM USER WHERE codUser=\'''' + codUser + '''\' AND tipo=\'3\' '''
        cursor.execute(query)
        self.connection.commit()
    
    def getPorLogin(self, login):
        cursor = self.connection.cursor()
        consulta = '''SELECT  codUser, senha, email, lista_receitas FROM USER WHERE login=\'''' + login + '''\' AND tipo=\'3\' '''
        cursor.execute(consulta)
        registro = cursor.fetchone()
        if registro != None:
            codUser = registro[0]
            senha = registro[1]
            email = registro[2]
            lista_receitas = registro[3]
            cook = Cook(codUser,senha,email)
            if lista_receitas != None:
                cook.curso = self.mapReceita.get(lista_receitas)
            return cook
        else:
            return None





