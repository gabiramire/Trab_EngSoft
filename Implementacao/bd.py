from user import User
from user import Admin
from user import Cook
from receita import Receita

import sqlite3


class BD:
    def __init__(self, lista_admin, lista_users, lista_denuncia):
        self.lista_admin = lista_admin
        self.lista_users = lista_users
        self.lista_denuncia = lista_denuncia



def create_tables(data):

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # TABELA USER
    ## TIPO 1 = USER, TIPO 2 = ADMIN, TIPO 3 = COOK

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS USER(
            cod_user INTEGER PRIMARY KEY AUTO INCREMENT,
            login TEXT NOT NULL,
            senha TEXT NOT NULL,
            email TEXT NOT NULL,
            senha_admin INTEGER,
            TIPO CHARACTER(1),
            FOREIGN KEY (lista_receitas) REFERENCES RECEITA(cod_receita),
            FOREIGN KEY (lista_denuncias) REFERENCES DENUNCIA(cod_denuncia)
    );
    """)

    # TABELA RECEITA - LINKED TO A COOK
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS RECEITA(
        cod_receita INTEGER PRIMARY KEY AUTO INCREMENT,
        FOREIGN KEY (USER) REFERENCES USER(cod_user)
        
    );    
    """)

    # TABELA DENUNCIA - TODOS OS ADMINS POSSUEM ACESSO A TODAS AS DENUNCIAS
    cursor.execute("""(
    CREATE TABLE IF NOT EXISTS DENUNCIA(
        cod_denuncia INTEGER PRIMARY KEY AUTO INCREMENT,
        

    );
    """)

    print('Tabelas criadas com sucesso.')
    # desconectando...

    conn.close()


class ReceitaMap:
    def __init__(self, connection):
        self.connection = connection

class AdminMap:
    def __init__(self, connection):
        self.connection = connection
        self.denunciaMap = DenunciaMap

class DenunciaMap:
    def __init__(self, connection):
        self.connection = connection
        self.receitaMap = ReceitaMap(connection)


class CookMap:

    def __init__(self, connection):
        self.connection = connection
        self.receitaMap = ReceitaMap(connection)

    def get(self, cod_user):
        cursor = self.connection.cursor()
        consulta = '''SELECT login, senha, email, lista_receitas FROM USER WHERE cod_user=\'''' + cod_user + '''\' AND TIPO=\'3\' '''
        cursor.execute(consulta)
        registro = cursor.fetchone()
        if registro != None:
            login = registro[0]
            senha = registro[1]
            email = registro[2]
            lista_receitas = registro[3]
            cook = Cook(login, senha, email)
            cook.cod_user = cod_user
            if lista_receitas != None:
                cook.curso = self.mapeadorCurso.get(lista_receitas)
            return cook
        else:
            return None

    def put(self, aluno):
        if self.get(aluno.cpf) != None:
            self.atualiza_aluno_existente(aluno)
        else:
            self.insere_novo_aluno(aluno)

    def insere_novo_aluno(self, aluno):
        cursor = self.connection.cursor()
        if aluno.curso == None:
            consulta = '''INSERT INTO PESSOA (CPF,NOME,ENDERECO,MATRICULA,TIPO) VALUES (%s,%s,%s,%s,\'3\')'''
            valores = (aluno.cpf, aluno.nome, aluno.endereco, str(aluno.matricula))
        else:
            consulta = '''INSERT INTO PESSOA (CPF,NOME,ENDERECO,MATRICULA,CURSO,TIPO) VALUES (%s,%s,%s,%s,%s,\'3\')'''
            valores = (aluno.cpf, aluno.nome, aluno.endereco, str(aluno.matricula), str(aluno.curso.codigo))
        cursor.execute(consulta,valores)
        self.connection.commit()

    def atualiza_aluno_existente(self, aluno):
        cursor = self.connection.cursor()
        if aluno.curso == None:
            consulta = '''UPDATE PESSOA SET NOME=%s,ENDERECO=%s, MATRICULA=%s WHERE CPF=%s AND TIPO=\'3\' '''
            valores = (aluno.nome, aluno.endereco, str(aluno.matricula), aluno.cpf)
        else:
            consulta = '''UPDATE PESSOA SET NOME=%s,ENDERECO=%s, MATRICULA=%s, CURSO=%s WHERE CPF=%s AND TIPO=\'3\' '''
            valores = (aluno.nome, aluno.endereco, str(aluno.matricula), str(aluno.curso.codigo), aluno.cpf)
        cursor.execute(consulta,valores)
        self.connection.commit()

    def remove(self, cpf):
        cursor = self.connection.cursor()
        query = '''DELETE FROM PESSOA WHERE CPF=\'''' + cpf + '''\' AND TIPO=\'3\' '''
        cursor.execute(query)
        self.connection.commit()
    
    def getPorNome(self, nome):
        cursor = self.connection.cursor()
        consulta = '''SELECT CPF,ENDERECO,MATRICULA,CURSO FROM PESSOA WHERE NOME=\'''' + nome + '''\' AND TIPO=\'3\' '''
        cursor.execute(consulta)
        registro = cursor.fetchone()
        if registro != None:
            cpf = registro[0]
            endereco = registro[1]
            matricula = registro[2]
            codigoCurso = registro[3]
            aluno = Aluno(cpf, nome)
            aluno.endereco = endereco
            aluno.matricula = matricula
            if codigoCurso != None:
                aluno.curso = self.mapeadorCurso.get(codigoCurso)
            return aluno
        else:
            return None








def initial_admin(data):
    a1 = Admin('admin_1', 'abc123', 'admin_1@email.com', '1111')
    a2 = Admin('admin_2', 'abc123', 'admin_2@email.com', '2222')
    a3 = Admin('admin_3', 'asd', 'asd', 'asd')
    data.lista_admin.append(a1)
    data.lista_admin.append(a2)
    data.lista_admin.append(a3)


def initial_user(data):
    # r1 = Receita('Bolo de Chocolate','Gabi', ['bolo', 'chocolate', 'doce', 'sobremesa'], 'A', 'A', 'A', [{'chocolate': '1 barra'}], 'Um delicioso bolo de chocolate.', 'Leite, ovos,...')
    # r1 = Receita('BOLO', 'a', ['BOLO', 'DOCE'], 'A', 'A', 'A', [
    #              {'jaca': '2'}], 'Um delicioso bolo de chocolate.', 'Leite, ovos,...')
    u1 = Cook('a', 'a', 'a', [])
    data.lista_users.append(u1)
    u2 = Cook('Gabi', 'abc123', 'gabi@email.com', [])
