class User:
    def __init__(self, login, senha, email, codUser):
        self.login = login
        self.senha = senha
        self.email = email
        self.codUser = codUser

class Admin(User):
    def __init__(self, login, senha, email, senha_admin, codUser):
        super().__init__(login, senha, email, codUser)
        self.senha_admin = senha_admin

class Cook(User):
    def __init__(self, login, senha, email, lista_receitas, codUser):
        super().__init__(login, senha, email, codUser)
        self.lista_receitas = lista_receitas
