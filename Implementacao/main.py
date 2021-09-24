from Mapeadores.mapAdmin import mapAdmin
from Mapeadores.mapCook import mapCook
from Mapeadores.mapDenuncia import mapDenuncia
from Mapeadores.mapReceita import mapReceita
import sqlite3
import sistema
from bd import BD
import interface

def main():
    data = BD(conn = sqlite3.connect('database.db'))
    data.create_tables()
    data.initial_admin()

    # lista_admin = []
    # lista_users = []
    # lista_denuncia = []
    # user_atual = 0
    # data = BD(lista_admin, lista_users, lista_denuncia)
    # BD.initial_admin(data)
    # BD.initial_user(data)
    # normal_user = False

    # while user_atual != 'exit':
    #     SisInterface = interface.Interface()
    #     s = sistema.Sistema(SisInterface)
    #     user_atual = s.menu_cadastro(data)
    #     for i in data.lista_admin:
    #         if user_atual == i.login:
    #             s.menu_admin(user_atual, i, data)
    #         else:
    #             normal_user = True
    #     if normal_user:
    #         for j in data.lista_users:
    #             if user_atual == j.login:
    #                 s.menu_user(user_atual, j, data)


main()
