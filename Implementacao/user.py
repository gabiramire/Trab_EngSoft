class User:
    def __init__(self, login, senha, email):
        self.login = login
        self.senha = senha
        self.email = email

class Admin(User):
    def __init__(self, login, senha, email, senha_admin):
        super().__init__(login, senha, email)
        self.senha_admin = senha_admin

class Cook(User):
    def __init__(self, login, senha, email, lista_receitas):
        super().__init__(login,senha,email)
        self.lista_receitas = lista_receitas