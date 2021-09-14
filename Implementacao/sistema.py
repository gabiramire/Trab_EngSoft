from receita import Receita
from user import User
from user import Admin
import pesquisa
#from bd import BD
# import keyboard as key  # using module keyboard


class Sistema():
    def __init__(self, SisInterface):
        self.IdClass = "Sistema"
        self.interface = SisInterface
        self.pesquisa = pesquisa.Pesquisa(self.interface)

    def menu_cadastro(self, data):
        user_atual = 0
        while user_atual == 0:
            comand = self.interface.menu_comando()
            if comand == "A":
                login, senha, email = self.interface.login_senha_email()
                if len(data.lista_users) >= 1:
                    nome_existe = ""
                    for user in data.lista_users:
                        if user.email == email:
                            nome_existe = "S"
                    if nome_existe == "S":
                        self.interface.retorno_print("Usuário já existente. ")
                    else:
                        lista_receitas = []  # CRIAR UMA NOVA LISTA PARA CADA USUARIO NOVO
                        x = User(login, senha, email, lista_receitas)
                        data.lista_users.append(x)
                else:
                    lista_receitas = []  # SE FOR O PRIMEIRO CADASTRO NAO ENTRA NO FOR PARA VERIFICAR O NOME
                    x = User(login, senha, email, lista_receitas)
                    data.lista_users.append(x)

                self.interface.retorno_print("-="*30)

            elif comand == "B":
                email, senha = self.interface.email_senha()
                admin = False
                if len(email) >= 1:
                    erro_pin = 0
                    for i in data.lista_admin:
                        if i.email == email and i.senha == senha:
                            pin = self.interface.menu_input_pin()
                            admin = True
                            if i.senha_admin == pin:
                                user_atual = i.login
                            else:
                                self.interface.invalid_input()
                                erro_pin = 1
                    if admin == False:
                        found = ''
                        for i in data.lista_users:
                            if found == '':
                                if i.email == email and i.senha == senha:
                                    user_atual = i.login
                                    found = 'S'
                                else:
                                    user_atual = 0
                        if user_atual == 0 and erro_pin == 0:
                            self.interface.retorno_print(
                                "Senha ou email incorretos")

            elif comand == "C":
                return 'exit'

            else:
                pass

        return user_atual

    def menu_user(self, user_atual, j, data):
        self.interface.retorno_print(f'Bem vindo, {user_atual}!')

        while user_atual == j.login:
            comand = self.interface.interface_menu_user()

            if comand == "A":  # Criar Receita
                # lista = []
                nome, palavras_chave, doce_salgado, gluten, porcoes, lista_ingredientes, descricao, modo_preparo = self.interface.parametros()  # funcao valores
                # print(j.lista_receitas)
                if len(j.lista_receitas) >= 1:
                    aux = ""
                    for receita in j.lista_receitas:
                        if receita.nome == nome:
                            aux = "S"
                    if aux == "S":
                        self.interface.retorno_print(
                            "\n ~~ Nome já existente, cadastre novamente.  ~~ \n")
                    else:
                        food = Receita(nome, user_atual, palavras_chave, doce_salgado,
                                       porcoes, gluten, lista_ingredientes, descricao, modo_preparo)
                        j.lista_receitas.append(food)
                else:
                    food = Receita(nome, user_atual, palavras_chave, doce_salgado,
                                   porcoes, gluten, lista_ingredientes, descricao, modo_preparo)
                    j.lista_receitas.append(food)

            elif comand == "B":  # Pesquisa
                self.pesquisa.pesquisar_receita(data, user_atual)

            elif comand == "C":  # Minhas Receitas
                self.interface.retorno_print("-="*30)
                cont = 1
                if len(j.lista_receitas) >= 1:
                    for receita in j.lista_receitas:
                        self.interface.retornar_lista_receitas(cont, receita)
                        cont += 1
                    alterar = self.interface.deseja_alterar_receita()
                    if alterar == '1':
                        numero_receita = self.interface.alterar_receita_escolhida()
                        if (numero_receita) <= len(j.lista_receitas):
                            i = numero_receita - 1
                            rec_escolhida = j.lista_receitas[i]
                            alterar_dados = True
                            while alterar_dados:
                                alteracao = self.interface.menu_alterar_receita()
                                if alteracao == '1':
                                    nome = self.interface.input_nome_receita()
                                    rec_escolhida.nome = nome
                                elif alteracao == '2':
                                    palavras_chave = self.interface.input_palavra_chave()
                                    rec_escolhida.palavras_chave = palavras_chave
                                elif alteracao == '3':
                                    doce_salgado = self.interface.input_doce_salgado()
                                    rec_escolhida.doce_salgado = doce_salgado
                                elif alteracao == '4':
                                    porcoes = self.interface.input_porcoes()
                                    rec_escolhida.porcoes = porcoes
                                elif alteracao == '5':
                                    gluten = self.interface.input_gluten()
                                    rec_escolhida.gluten = gluten
                                elif alteracao == '6':
                                    lista_ingredientes = self.interface.input_lista_ingredientes()
                                    rec_escolhida.lista_ingredientes = lista_ingredientes
                                elif alteracao == '7':
                                    descricao = self.interface.input_descricao()
                                    rec_escolhida.descricao = descricao
                                elif alteracao == '8':
                                    modo_preparo = self.interface.input_modo_preparo()
                                    rec_escolhida.modo_preparo = modo_preparo
                                elif alteracao == '9':
                                    j.lista_receitas.pop(i)
                                    alterar_dados = False
                                elif alteracao == '0':
                                    alterar_dados = False
                                else:
                                    self.interface.retorno_print(
                                        "Valor inválido. ")

                        else:
                            self.interface.retorno_print("Inválido. ")

                    elif alterar == '2':
                        pass
                    else:
                        self.interface.retorno_print(" Inválido. ")
                else:
                    self.interface.retorno_print(
                        "O usuário ainda não possui receitas cadastradas. ")

            # login senha, email, alterar e excluir
            elif comand == "D":  # Minha Conta
                alterar_dados = True
                while alterar_dados:
                    alteracao = self.interface.menu_alteracao_user(j)
                    if alteracao == '1':  # Alterar nome
                        novo_login = self.interface.novo_parametro()
                        user_atual = novo_login
                        old_name = j.login
                        j.login = novo_login
                        for receita in j.lista_receitas:
                            receita.nome_usuario = novo_login
                        lista = []
                        for rec in data.lista_denuncia:
                            nova = {}
                            for c, v in rec.items():
                                if c == old_name:
                                    nova[novo_login] = v
                                else:
                                    nova[c] = v
                            lista.append(nova)
                        data.lista_denuncia.clear()
                        data.lista_denuncia = lista.copy()

                    elif alteracao == '2':  # Alterar senha
                        nova_senha = self.interface.novo_parametro()
                        j.senha = nova_senha

                    elif alteracao == '3':  # Alterar email
                        novo_email = self.interface.novo_parametro()
                        j.email = novo_email

                    elif alteracao == '4':  # Excluir conta
                        self.interface.retorno_print(
                            "Conta excluída com sucesso. ")
                        data.lista_users.remove(j)
                        user_atual = 0
                        alterar_dados = False

                    elif alteracao == '0':
                        alterar_dados = False

                    else:
                        self.interface.invalid_input()

            elif comand == "E":
                user_atual = 0

            else:
                self.interface.invalid_input()

    def menu_admin(self, user_atual, i, data):
        while user_atual == i.login:
            comand = self.interface.menu_comando_admin()  # self.interface grafica
            if comand == "A":  # Todas as Contas
                aux_user = 1
                aux_adm = 1
                for admin in data.lista_admin:
                    self.interface.menu_lista_admin(
                        aux_adm, admin)  # self.interface grafica
                    aux_adm += 1
                for usuario in data.lista_users:
                    self.interface.menu_lista_user(
                        aux_user, usuario)  # self.interface grafica
                    aux_user += 1
                alteracao_conta = True
                while alteracao_conta:
                    alteracao = self.interface.menu_alteracao_admin()
                    if alteracao == 'A':  # Excluir uma conta.
                        continuar = True
                        while continuar:
                            email_encontrado = False
                            login = self.interface.email_usuario()
                            for admin_pesquisa in data.lista_admin:
                                if login == admin_pesquisa.email:
                                    if user_atual == admin_pesquisa.login:
                                        data.lista_admin.remove(admin_pesquisa)
                                        self.interface.retorno_print(
                                            f'Admin {admin_pesquisa.login} excluído com sucesso. ')
                                        user_atual = 0
                                        email_encontrado = True
                                        continuar = False
                                        alteracao_conta = False

                                    else:
                                        data.lista_admin.remove(admin_pesquisa)
                                        self.interface.retorno_print(
                                            f'Admin {admin_pesquisa.login} excluído com sucesso. ')
                                        email_encontrado = True
                                        continuar = False
                                        alteracao_conta = False
                                else:
                                    continue

                            for usuario_pesquisa in data.lista_users:
                                if login == usuario_pesquisa.email:
                                    data.lista_users.remove(usuario_pesquisa)
                                    self.interface.retorno_print(
                                        f'Usuário {usuario_pesquisa.login} excluído com sucesso. ')
                                    email_encontrado = True
                                    continuar = False

                            if email_encontrado == False:
                                self.interface.retorno_print(
                                    "Email não encontrado.")
                                continuar = False

                    elif alteracao == 'B':  # Alterar dados de uma conta
                        email = self.interface.which_user()
                        alterar_dados = True
                        choosed_user = 0
                        is_admin = False
                        for admin in data.lista_admin:
                            if email == admin.email:
                                choosed_user = admin
                                is_admin = True
                        for user in data.lista_users:
                            if email == user.email:
                                choosed_user = user
                        if choosed_user == 0:
                            self.interface.erro404()
                            break
                        while alterar_dados:
                            if is_admin == True:
                                alteracao_user = self.interface.menu_alterar_dados_admin()
                            else:
                                alteracao_user = self.interface.menu_alterar_dados_user()

                            if alteracao_user == '1':  # Alterar login
                                novo_login = self.interface.novo_parametro()
                                choosed_user.login = novo_login
                                break

                            elif alteracao_user == '2':  # Alterar senha
                                nova_senha = self.interface.novo_parametro()
                                choosed_user.senha = nova_senha
                                break

                            elif alteracao_user == '3':  # Alterar email
                                novo_email = self.interface.novo_parametro()
                                choosed_user.email = novo_email
                                break

                            elif alteracao_user == '4':
                                novo_pin = self.interface.novo_parametro()
                                choosed_user.senha_admin = novo_pin
                                break

                            elif alteracao_user == '0':
                                alterar_dados = False
                                break
                            else:
                                self.interface.invalid_input()

                    elif alteracao == 'C':  # Adicionar uma conta admnistrativa
                        login, email, senha, pin = self.interface.menu_novo_admin()
                        nome_existe = ""
                        for admin in data.lista_admin:
                            if admin.email == email:
                                nome_existe = "S"
                        if nome_existe == "S":
                            self.interface.retorno_print(
                                "Admin já existente. ")
                        else:
                            x = Admin(login, senha, email, pin)
                            data.lista_admin.append(x)
                            self.interface.retorno_print(
                                "O novo administrador está cadastrado no sistema.")
                        self.interface.retorno_print("-="*30)

                    elif alteracao == 'D':
                        alteracao_conta = False
                    else:
                        pass

            elif comand == "B":  # Pesquisa
                self.interface.retorno_print(f"""
            {'-=' *30}
                    Pesquisa de Receitas
            {'-='*30}""")
                lista_total = self.pesquisa.mostrar_todas_receitas(
                    data.lista_users)
                for receita in lista_total:
                    self.interface.retornar_lista_receitas(
                        receita.nome, receita)

            elif comand == "C":  # Denuncias
                self.interface.retorno_print(f"""
        { '-='*30}
                Denuncias Recebidas: """)

                # denuncias nao esta funcionando direito
                self.pesquisa.acessar_denuncias(data.lista_denuncia,
                                                data.lista_users)
                self.interface.retorno_print("-="*30)

            elif comand == "D":  # Sair
                user_atual = 0

            else:
                self.interface.invalid_input()
