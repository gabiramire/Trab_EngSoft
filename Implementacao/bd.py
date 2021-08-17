from user import User
from user import Admin
from receita import Receita


class BD:
    def __init__(self, lista_admin, lista_users, lista_denuncia):
        self.lista_admin = lista_admin
        self.lista_users = lista_users
        self.lista_denuncia = lista_denuncia

    @property
    def lista_admin(self):
        return self._lista_admin

    @lista_admin.setter
    def lista_admin(self, value):
        self._lista_admin = value

    @property
    def lista_users(self):
        return self._lista_users

    @lista_users.setter
    def lista_users(self, value):
        self._lista_users = value

    @property
    def lista_denuncia(self):
        return self._lista_denuncia

    @lista_denuncia.setter
    def lista_denuncia(self, value):
        self._lista_denuncia = value


def initial_admin(data):
    a1 = Admin('admin_1', 'abc123', 'admin_1@email.com', '1111')
    a2 = Admin('admin_2', 'abc123', 'admin_2@email.com', '2222')
    a3 = Admin('admin_3', 'asd', 'asd', 'asd')
    data.lista_admin.append(a1)
    data.lista_admin.append(a2)
    data.lista_admin.append(a3)


def initial_user(data):
    # r1 = Receita('Bolo de Chocolate','Gabi', ['bolo', 'chocolate', 'doce', 'sobremesa'], 'A', 'A', 'A', [{'chocolate': '1 barra'}], 'Um delicioso bolo de chocolate.', 'Leite, ovos,...')
    r1 = Receita('BOLO', 'a', ['BOLO', 'DOCE'], 'A', 'A', 'A', [{'jaca': '2'}], 'Um delicioso bolo de chocolate.', 'Leite, ovos,...')
    u1 = User('a', 'a', 'a', [r1])
    data.lista_users.append(u1)
    u2 = User('Gabi', 'abc123', 'gabi@email.com', [])
