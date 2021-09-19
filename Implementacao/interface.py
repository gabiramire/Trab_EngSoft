class Interface():
    def __init__(self):
        self.IdClass = "Interface"

    # parametros para criar receita #####
    # comeco das funcoes para input de parametros

    def input_nome_receita(self):
        nome = input("Nome da comida: ").upper()
        return nome

    def input_palavra_chave(self):
        palavras_chave = []
        while 0 >= len(palavras_chave) or 100 >= len(palavras_chave):
            comand = input(f"""
            {"-="*30}
                1 -Inserir palavra chave
                0 - Exit
            {"-="*30}
                Resposta: """).upper()
            if comand == '1':
                palavra = input("\n Palavra chave: ").upper()
                palavras_chave.append(palavra)
            elif comand == '0':
                break
            else:
                print("Input inválido. ")
        return palavras_chave

    def input_doce_salgado(self):
        doce_salgado = ''
        while doce_salgado != "A" and doce_salgado != "B":
            doce_salgado = input(f"""
    {"-="*30}
            A receita é:   
                A - Doce
                B - Salgada
    {"-="*30}
            Resposta: """).upper()
        if doce_salgado == 'A':
            doce_salgado = 'Doce'
        else:
            doce_salgado = 'Salgada'
        return doce_salgado

    def input_gluten(self):
        gluten = ''
        while gluten != "A" and gluten != "B":
            gluten = input(f"""
    {"-="*30}
        A receita é:
            A - Com glúten
            B - Sem glúten
    {"-="*30}
        Resposta: """).upper()

        if gluten == 'A':
            gluten = 'Com glúten'
        else:
            gluten = 'Sem glúten'
        return gluten

    def input_porcoes(self):
        porcoes = ''
        while porcoes != "A" and porcoes != "B":
            porcoes = input(f"""
    {"-="*30}
        A receita pode servir:
        
            A - até 2 pessoas
            B - mais de 2 pessoas 
    {"-="*30}
        Resposta: """).upper()

        if porcoes == 'A':
            porcoes = 'Serve até 2 pessoas'
        else:
            porcoes = 'Serve mais de 2 pessoas'
        return porcoes

    def input_lista_ingredientes(self):
        print("-="*30)
        inserir_ingrediente = True
        lista_ingredientes = []
        print('1='*30)
        i = 1
        mais_ingredientes = ''
        print('Insira a seguir os ingredientes de sua receita: ')
        while inserir_ingrediente:
            dic = {}

            if mais_ingredientes == '':
                ingrediente = input(f"Ingrediente {i}: ")
                dic[ingrediente] = input("Quantia utilizada: ")
                i = i + 1
                lista_ingredientes.append(dic)
                mais_ingredientes = input(
                    'Deseja inserir mais ingredientes? 1- Sim, 2- Não\nResposta: ')
            if mais_ingredientes == '2':
                inserir_ingrediente = False
            elif mais_ingredientes == '1':
                mais_ingredientes = ''
                continue
            else:
                print("Valor inválido. ")
                mais_ingredientes = input(
                    'Deseja inserir mais ingredientes? 1- Sim, 2- Não\nResposta: ')
        return lista_ingredientes

    def input_modo_preparo(self):
        modo_preparo = input("Modo de preparo: ")
        return modo_preparo

    def input_descricao(self):
        descricao = input("Descrição da receita: ")
        return descricao
    # end funcoes para input de parametros

    def parametros(self):
        nome = self.input_nome_receita()

        palavras_chave = self.input_palavra_chave()

        doce_salgado = self.input_doce_salgado()

        gluten = self.input_gluten()

        porcoes = self.input_porcoes()

        lista_ingredientes = self.input_lista_ingredientes()

        modo_preparo = self.input_modo_preparo()

        descricao = self.input_descricao()

        return nome, palavras_chave, doce_salgado, gluten, porcoes, lista_ingredientes, descricao, modo_preparo

    def retornar_receita(self, receita):     # imprimir os dados de uma receita
        nome, doce_salgado, avaliacoes, gluten, porcoes, lista_ingredientes, descricao, modo_preparo = receita.retorno()

        print(f"""
        {"#"*53}

        **{nome.upper()}**
            {"#"*53}
                Avaliações (0-10): {avaliacoes:.1f}
                Receita {doce_salgado}
                Tipo: {gluten}
                {porcoes}
            {"#"*53}

            Descrição: {descricao}
            Numero de ingredientes: {len(lista_ingredientes)} 
                Ingredientes: """)
        for k in lista_ingredientes:
            for c, v in k.items():
                print(
                    f"""          {"Nome:":>48} {c:<15}{" ":8}quantidade: {v}""")
        print(f"""
                Modo de preparo: {modo_preparo}
        """)

    ########## interface pesquisa       ##############################

    def menu_nome_receita(self):
        nome_usuario = input(" Nome do usuario que pretende acessar: ")
        nome_receita = input(" Nome da receita: ").upper()
        return nome_usuario, nome_receita

    def menu_pesquisa_receita(self, lista_total):
        # print(lista_total)
        pesquisa = input(f"""
            {"-="*30}
            ######################
            # Pesquisar Receitas #
            ######################
            {"-="*30}
                O que iremos cozinhar hoje? 
                        *Colocar nome da receita ou palavra chave
                            F - Para sair

                \n    """).upper()
        return pesquisa

    def menu_denunciar_motivo(self):
        motivo = input(f"""
            {"-="*30}
            Motivo da denúncia:
                1 - Contêm conteúdo inapropriado
                2 - Não é uma receita
                3 - Receita plagiada
                0 - Sair
            {"-="*30}
            Resposta: """)
        return motivo

    def menu_comando_avaliar(self):
        avaliar = input("""
                Deseja:
                    1 - Avaliar a receita
                    2 - Denunciar a receita

                    0 - Não fazer nada
            """)
        return avaliar

    def menu_verificar_receita_user(self):
        comand = input("""
            1 - Verificar receitas do usuario
            2 - Deletar receita do usuario

            0 - Exit
            """)
        return comand

    def menu_nota_receita(self):
        nota = float(input(f"""
        {"-="*30}
        Nota da receita (0-10):
        {"-="*30}
        Resposta: """))
        return nota

    def menu_lista_denuncia(self, lista_denuncia):
        for i in lista_denuncia:
            for c, v in i.items():      # chave, valor de cada item
                print(f" Usuário: {c} receita: {v[0]} motivo: {v[1]}")
        print('-'*40)

    def erro404(self):
        print(" Dados não encontrados. ")

    def invalid_input(self):
        print("Valor inválido. ")

    def sem_resposta_continuar_pesquisa(self):
        sair = input('Deseja sair? 1- Sim, 2- Não \nResposta: ')
        return sair

    ## interface usadas no sistema      ##########################

    def novo_parametro(self):
        novo_parametro = input(" Digite o novo parâmetro: ")
        return novo_parametro

    def login_senha_email(self):
        print("-="*30)
        login = input("Login: ")
        senha = input("Senha: ")
        email = input("Email: ")
        return login, senha, email

    def email_senha(self):
        print("-="*30)
        email = input("Email: ")
        senha = input("Senha: ")
        print("-="*30)
        return email, senha

    def menu_alteracao_user(self, j):
        print(f"""
        {'-'*30}
            Nome:   {j.login}
            Email:  {j.email}
        {'-'*30}
        """)
        alteracao = input("""
            1 - Alterar nome
            2 - Alterar senha
            3 - Alterar email
            4 - Excluir conta

            0 - Sair
        """)
        return alteracao

    def menu_alterar_dados_user(self):
        alteracao = input("""
                1 - Alterar nome
                2 - Alterar senha
                3 - Alterar email

                0 - Sair
            """)
        return alteracao

    def menu_alterar_dados_admin(self):
        alteracao = input("""
                1 - Alterar nome
                2 - Alterar senha
                3 - Alterar email
                4 - Alterar pin de segurança

                0 - Sair
            """)
        return alteracao

    def menu_comando(self):
        comand = input(f"""
        Sistema de Cadastro:
            A - Cadastrar usuario
            B - Acessar conta
            C - Sair
        {"-="*30}
        Resposta: """).upper()
        return comand

    def menu_comando_user(self):
        comand = input(f"""
    {"##"*30}    
        A - Criar Receita
        B - Pesquisa
        C - Minhas Receitas
        D - Minha Conta 
        
        E - Sair
    {"-="*30}
    Resposta: """).upper(self)
        return comand

    def menu_comando_admin(self):
        comand = input(f"""
            Sistema da Administracao:
                A - Todas as Contas
                B - Pesquisa
                C - Denuncias
                D - Sair
            {"-="*30}
            Resposta: """).upper()
        return comand

    def menu_alteracao_admin(self):
        print('\n #### Deseja fazer alguma alteracao? ####')
        comand = input(f"""
                    A - Excluir uma conta.
                    B - Alterar dados de uma conta.
                    C - Adicionar uma conta admnistrativa.
                    D - Nao, sair.
                    {"-="*30}
                    Resposta: """).upper()
        return comand

    def menu_input_pin(self):
        print("Bem vindo, administrador. Por segurança do sistema, favor insira seu pin de administração para prosseguir.")
        pin = input("Pin: ")
        return pin

    def interface_menu_user(self):
        comand = input(f"""{"##"*30}    
        A - Criar Receita
        B - Pesquisa
        C - Minhas Receitas
        D - Minha Conta 
        
        E - Sair
        {"-="*30}
        Resposta: """).upper()
        return comand

    def menu_lista_admin(self, aux_adm, admin):
        print(f"ADMIN {'-='*30} ")
        print(
            f'Admin {aux_adm}, Login : {admin.login}, Email : {admin.email}, Senha : {admin.senha}, Pin : {admin.senha_admin}')
        print("-="*30)

    def menu_lista_user(self, aux_user, usuario):
        print(f"USER {'-='*30} ")
        print(
            f'Usuario {aux_user}, Login : {usuario.login}, Email : {usuario.email}, Senha : {usuario.senha}')

    def deseja_alterar_receita(self):
        alterar = input(
            f""" 
            {'-'*30}
            Deseja alterar alguma receita? \n1 - Sim, 2 - Não\nResposta: """)
        return alterar

    def receita_para_alterar(self):
        rec_escolhida = int(
            input(f"{'-'*30}\n Insira o número referente à receita que deseja alterar:\n"))
        return rec_escolhida

    def retornar_lista_receitas(self, i, receita):
        print(f"""
        #############
        # RECEITA {i} #
        ##############\n
        # Nome: {receita.nome} \n\n
        # Ingredientes: {receita.lista_ingredientes} \n\
        # Modo de preparo: {receita.modo_preparo} \n\n
        # Descricao: {receita.descricao} \n\n
        # Palavras Chave: {receita.palavras_chave}
                                """)

    def deseja_alterar_receita(self):
        alterar = input(f"""
        {'-'*30}
            Deseja alterar alguma receita? 
            1 - Sim, 2 - Não
            Resposta: """)
        return alterar

    def alterar_receita_escolhida(self):
        int_rec_escolhida = ''
        while int_rec_escolhida != int:
            rec_escolhida = input(
                f"{'-'*30}\n Insira o número referente à receita que deseja alterar: ")

            try:
                int_rec_escolhida = int(rec_escolhida)
                break
            except:
                print("Insira um número válido. ")
        return int_rec_escolhida

    # def menu_sair():
    #     sair = input("S - sair")
    #     return sair

    def email_usuario(self):
        login = input(" Email do usuário: ")
        return login

    def retorno_print(self, palavra):
        print(palavra)

    def menu_alterar_receita(self):
        #nome, user_atual, palavras_chave, doce_salgado,
        # porcoes, gluten, lista_ingredientes, descricao, modo_preparo)
        alteracao = input("""
            1 - Alterar nome
            2 - Alterar palavras chave
            3 - Alterar se é doce ou salgado
            4 - Alterar número de porcoes
            5 - Alterar se tem gluten
            6 - Alterar a lista de ingredientes
            7 - Alterar a descrição
            8 - Alterar o modo de preparo
            9 - Deletar a receita
            
            0 - Sair
        """)
        return alteracao

    def menu_novo_admin(self):
        print("Adicionar uma conta admnistrativa.")
        login = input("Insira o nome de usuário: ")
        email = input("Email do novo administrador: ")
        senha = input("Senha: ")
        pin = input("Pin de segurança: ")
        return login, email, senha, pin

    def which_user(self):
        print("Alterar dados de uma conta.")
        user = input("Qual o email do usuário que deseja alterar? ")
        return user
