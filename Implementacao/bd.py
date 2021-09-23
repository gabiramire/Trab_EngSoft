from user import User
from user import Admin
from user import Cook
from receita import Receita

import sqlite3


class BD:
    def __init__(self, lista_admin, lista_cook, lista_denuncia):
        self.lista_admin = lista_admin
        self.lista_cook = lista_cook
        self.lista_denuncia = lista_denuncia



def create_tables(data):

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # TABELA USER
    ## TIPO 1 = USER, TIPO 2 = ADMIN, TIPO 3 = COOK

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS USER(
            codUser INTEGER PRIMARY KEY AUTO INCREMENT,
            login TEXT NOT NULL,
            senha TEXT NOT NULL,
            email TEXT NOT NULL,
            senha_admin INTEGER,
            tipo CHARACTER(1),
            FOREIGN KEY (lista_receitas) REFERENCES RECEITA(cod_receita),
            FOREIGN KEY (lista_denuncias) REFERENCES DENUNCIA(cod_denuncia)
    );
    """)

    # TABELA RECEITA - LINKED TO A COOK
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS RECEITA(
        cod_receita INTEGER PRIMARY KEY AUTO INCREMENT,
        FOREIGN KEY (USER) REFERENCES USER(cod_user)
        nome TEXT NOT NULL,
        FOREIGN KEY (palavras_chave ) REFERENCES PALAVRA-CHAVE(cod)
    );    
    """)

      cursor.execute("""
    CREATE TABLE IF NOT EXISTS PALAVRA-CHAVE(
        cod_receita INTEGER PRIMARY KEY AUTO INCREMENT,
        FOREIGN KEY (USER) REFERENCES USER(cod_user)
        nome TEXT NOT NULL,
        palavras_chave 
    );    
    """)
        # self.nome = None
        # self.codUser = None  # nome do criador
        # self.palavras_chave = None
        # self.doce_salgado = None
        # self.avaliacoes = []
        # self.media_avaliacao = 0
        # self.gluten = None
        # self.porcoes = None
        # self.lista_ingredientes = None      # lista de ingredientes
        # self.descricao = None
        # self.modo_preparo = None
        # self.users_avaliacoes = []
        # self.users_denuncias = []
        # self.codReceita = None





#     # TABELA DENUNCIA - TODOS OS ADMINS POSSUEM ACESSO A TODAS AS DENUNCIAS
#     cursor.execute("""(
#     CREATE TABLE IF NOT EXISTS DENUNCIA(
#         cod_denuncia INTEGER PRIMARY KEY AUTO INCREMENT,
        

#     );
#     """)

#     print('Tabelas criadas com sucesso.')
#     # desconectando...

#     conn.close()


# class ReceitaMap:
#     def __init__(self, connection):
#         self.connection = connection

# class AdminMap:
#     def __init__(self, connection):
#         self.connection = connection
#         self.denunciaMap = DenunciaMap

# class DenunciaMap:
#     def __init__(self, connection):
#         self.connection = connection
#         self.receitaMap = ReceitaMap(connection)



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
