from user import Admin
from denuncia import Denuncia
from Mapeadores.mapDenuncia import mapDenuncia


class mapAdmin:

    def __init__(self, connection):
        self.connection = connection
        self.mapDenuncia = mapDenuncia(connection)

    def get(self, codUser):
        cursor = self.connection.cursor()
        consulta = '''SELECT login, senha, email, senha_admin, lista_denuncias FROM USER WHERE codUser=\'''' + codUser + '''\' AND tipo=\'2\' '''
        cursor.execute(consulta)
        registro = cursor.fetchone()
        if registro != None:
            login = registro[0]
            senha = registro[1]
            email = registro[2]
            senha_admin = registro[3]
            lista_denuncias = registro[4]
            admin = Admin(login, senha, email, senha_admin, codUser)
            if lista_denuncias != None:
                admin.lista_denuncias = self.mapDenuncia.get(lista_denuncias)
            return admin
        else:
            return None

    def put(self, admin):
        if self.get(admin.codUser) != None:
            self.atualiza_admin_existente(admin)
        else:
            self.insere_novo_admin(admin)

    def insere_novo_admin(self, admin):
        cursor = self.connection.cursor()
        if admin.lista_denuncias == None:
            consulta = '''INSERT INTO USER (login, senha, email, senha_admin, codUser, tipo) VALUES (%s,%s,%s,\'3\')'''
            valores = (admin.login, admin.senha, admin.email, admin.senha_admin, str(admin.codUser))
        else:
            consulta = '''INSERT INTO USER (login, senha, email, senha_admin, codUser, lista_denuncias, tipo) VALUES (%s,%s,%s,%s,%s,\'3\')'''
            valores = (admin.cpf, admin.nome, admin.endereco, admin.senha_admin, str(admin.codUser), str(admin.lista_denuncias))
        cursor.execute(consulta,valores)
        self.connection.commit()

    def atualiza_admin_existente(self, admin):
        cursor = self.connection.cursor()
        if admin.lista_denuncias == None:
            consulta = '''UPDATE USER SET login=%s, senha=%s, email=%s, senha_admin=%s WHERE codUser=%s AND tipo=\'2\' '''
            valores = (admin.login, admin.senha, admin.email, admin.senha_admin, str(admin.codUser))
        else:
            consulta = '''UPDATE USER SET login=%s, senha=%s, email=%s, senha_admin=%s, lista_denuncias=%s WHERE codUser=%s AND tipo=\'2\' '''
            valores = (admin.login, admin.senha, admin.email, admin.senha_admin, str(admin.codUser), str(admin.lista_denuncias))
        cursor.execute(consulta,valores)
        self.connection.commit()

    def remove(self, codUser):
        cursor = self.connection.cursor()
        query = '''DELETE FROM USER WHERE codUser=\'''' + codUser + '''\' AND tipo=\'2\' '''
        cursor.execute(query)
        self.connection.commit()
    
    def getPorLogin(self, login):
        cursor = self.connection.cursor()
        consulta = '''SELECT  codUser, senha, email, senha_admin, lista_denuncias FROM USER WHERE login=\'''' + login + '''\' AND tipo=\'2\' '''
        cursor.execute(consulta)
        registro = cursor.fetchone()
        if registro != None:
            codUser = registro[0]
            senha = registro[1]
            email = registro[2]
            senha_admin = registro[3]
            lista_denuncias = registro[4]
            admin = Admin(codUser,senha,email,senha_admin)
            if lista_denuncias != None:
                admin.curso = self.mapReceita.get(lista_denuncias)
            return admin
        else:
            return None





