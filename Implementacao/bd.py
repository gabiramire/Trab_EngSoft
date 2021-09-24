from user import User
from user import Admin
from user import Cook
from denuncia import Denuncia
from receita import Receita
import sqlite3
from Mapeadores.mapAdmin import mapAdmin
from Mapeadores.mapCook import mapCook
from Mapeadores.mapDenuncia import mapDenuncia
from Mapeadores.mapReceita import mapReceita

class BD:
    def __init__(self, conn):
        self.users = []
        self.conn = conn
        self.mapAdmin = mapAdmin(self.conn)
        self.mapCook = mapCook(self.conn)
        self.mapDenuncia = mapDenuncia(self.conn)
        self.mapReceita = mapReceita(self.conn)

    ## TODO:
        # DENUNCIA TABLE
        # RECEITA TABLE
        # CONFERIR MAPADMIN E MAPUSER
        # FAZER MAPDENUNCIA
        # FAZER MAPRECEITA
        # AJUSTAR O RESTO DO PROGRAMA PARA AS NOVAS CLASSES CRIADAS PARA O BD
        # TESTAR O BD
        # ESTUDAR MAIS SOBRE HERANÇA E COMPOSIÇÃO EM SQL
        ## -> AS PALAVRAS CHAVE PRECISAM SER OUTRA CLASSE (?)
        ### PALAVRA CHAVE TABLE
        ### PALAVRA CHAVE MAP


    def create_tables(self):
        # TABELA USER
        ## TIPO 1 = USER, TIPO 2 = ADMIN, TIPO 3 = COOK
        cursor = self.conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS USER(
            codUser INTEGER PRIMARY KEY AUTOINCREMENT,
            lista_receitas INTEGER,
            login TEXT NOT NULL,
            senha TEXT NOT NULL,
            email TEXT NOT NULL,
            tipo CHARACTER(1),
            senha_admin INTEGER,
            FOREIGN KEY(lista_receitas) REFERENCES RECEITA(codReceita)
        );
        """)


        # TABELA RECEITA - LINKED TO A COOK

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS RECEITA(
            codReceita INTEGER PRIMARY KEY AUTOINCREMENT,
            user INTEGER,
            nome TEXT NOT NULL,
            doce_salgado TEXT,
            media_avaliacao INTEGER,
            gluten TEXT,
            porcoes TEXT,
            lista_ingredientes INTEGER,
            avaliacoes INTEGER,
            descricao TEXT,
            modo_preparo TEXT,
            FOREIGN KEY(user) REFERENCES USER(codUser),
            FOREIGN KEY (avaliacoes) REFERENCES AVALIACAO(codAvaliacao)
        );    
        """)

        # TABELA PALAVRA-CHAVE - uma receita possui várias palavras-chave
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS PALAVRACHAVE(
            receita INTEGER,
            palavra TEXT NOT NULL,
            FOREIGN KEY (receita) REFERENCES RECEITA(codReceita)
        );    
        """)

        # TABELA INGREDIENTE - uma receita possui vários ingredientes 

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS INGREDIENTE(
            receita INTEGER,
            nome TEXT NOT NULL,
            quantidade TEXT NOT NULL,
            FOREIGN KEY (receita) REFERENCES RECEITA(codReceita)
        );    
        """)

        # TABELA AVALIACAO - uma receita possui varias avaliacoes, tentarei tbm ligar a usuarios
        ## user neste caso é quem avaliou não quem foi avaliado

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS AVALIACAO(
            codAvaliacao INTEGER PRIMARY KEY AUTOINCREMENT,
            receita INTEGER,
            user INTEGER,
            nota INTEGER,
            FOREIGN KEY (receita) REFERENCES RECEITA(codReceita)
            FOREIGN KEY (user) REFERENCES USER (coduser)
        );
        """)

        # TABELA DENUNCIA - TODOS OS ADMINS POSSUEM ACESSO A TODAS AS DENUNCIAS
        ## user neste caso é o denunciado não quem denunciou

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS DENUNCIA(
            coddenuncia INTEGER PRIMARY KEY AUTOINCREMENT,
            receita INTEGER,
            user INTEGER,
            motivo CHARACTER(1),
            FOREIGN KEY (receita) REFERENCES RECEITA(codReceita),
            FOREIGN KEY (user) REFERENCES USER(coduser)
        );
        """)

            
        print('Tabelas criadas com sucesso.')
        # desconectando...

        self.conn.commit()


    def initial_admin(data):
        lista_admin = []
        a1 = Admin('admin_1', 'abc123', 'admin_1@email.com', '1111', 201)
        a2 = Admin('admin_2', 'abc123', 'admin_2@email.com', '2222', 202)
        a3 = Admin('admin_3', 'abc123', 'admin_3@email.com', '3333', 203)
        lista_admin.append(a1)
        lista_admin.append(a2)
        lista_admin.append(a3)
        for i in lista_admin:
            mA = mapAdmin(data.conn)
            mA.put(i)

    def initial_user(data):
        # r1 = Receita('Bolo de Chocolate','Gabi', ['bolo', 'chocolate', 'doce', 'sobremesa'], 'A', 'A', 'A', [{'chocolate': '1 barra'}], 'Um delicioso bolo de chocolate.', 'Leite, ovos,...')
        # r1 = Receita('BOLO', 'a', ['BOLO', 'DOCE'], 'A', 'A', 'A', [
        #              {'jaca': '2'}], 'Um delicioso bolo de chocolate.', 'Leite, ovos,...')
        u1 = Cook('a', 'a', 'a', [])
        data.lista_users.append(u1)
        u2 = Cook('Gabi', 'abc123', 'gabi@email.com', [])
