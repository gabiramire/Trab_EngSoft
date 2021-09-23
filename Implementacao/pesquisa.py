<<<<<<< HEAD
#from receita import Receita
#from user import User #
from denuncia import Denuncia

=======
>>>>>>> 39df86735ca30ea46bacd64e3f02f29211f05ef6
class Pesquisa():
    def __init__(self, PesInterface):
        self.IdClass = "Pesquisa sistema"
        self.interface = PesInterface

    def get_avaliacao(self, receita):
        return receita.media_avaliacao

    def pesquisar_receita(self, data, user_atual):

        lista_total = []  # era uma lista de listas das receitas dos usuarios agora é uma lista com apenas receitas
        for i in data.lista_users:
            for j in i.lista_receitas:
                lista_total.append(j)

        # retornar as 5 melhores receitas
        lista_total.sort(reverse=True, key=self.get_avaliacao)
        if len(lista_total) > 0:
            melhores = 0
            for i in lista_total:
                if melhores < 5:
                    self.interface.retornar_receita(i)
                    melhores += 1

        continuar = True
        while continuar:
            pesquisa = self.interface.menu_pesquisa_receita(lista_total)
            if pesquisa != 'F':
                # for receita in lista_total:
                if len(lista_total) > 0:
                    receita_encontrada = False
                    encontro = ''
                    for receita in lista_total:  # uma lissta da lista
                        # for receita in receita_encontrada:  # a receita da lita .palavra_chave
                        # if len(receita.palavras_chave) > 0:
                        # if not(receita_encontrada):

                        for palavra in receita.palavras_chave:
                            if pesquisa == palavra:  # imprimir a uma tabela sobre a receita
                                self.interface.retornar_receita(receita)
                                # lista de denuncia
                                self.denunciar_avaliar(
                                    receita, data.lista_denuncia, user_atual)
                                receita_encontrada = True
                                encontro = 's'

                        if encontro == '':
                            if pesquisa == receita.nome:
                                self.interface.retornar_receita(receita)
                                # lista de denuncia
                                self.denunciar_avaliar(
                                    receita, data.lista_denuncia, user_atual)
                                receita_encontrada = True
                                encontro = 's'
                        encontro = ''

                    if not(receita_encontrada):
                        self.interface.retorno_print(" Receita não encontrada. ")
                        sair = self.interface.sem_resposta_continuar_pesquisa()
                        if sair == '1':
                            continuar = False
                            break
                        elif sair == '2':
                            pass
                        else:
                            self.interface.retorno_print(" Inválido. ")

                else:
                    self.interface.retorno_print(" # Sem receitas no banco.  ")

            elif pesquisa == 'F':
                sair = self.interface.sem_resposta_continuar_pesquisa()
                if sair == '1':
                    continuar = False
                    break
                elif sair == '2':
                    pass
                else:
                    self.interface.retorno_print(" Inválido. ")

    def avaliar_receita(self, receita):        # para avaliar uma receita
        nota = -1
        while nota < 0 or nota > 10:
            nota = self.interface.menu_nota_receita()
            if 0 <= nota <= 10:
                receita.avaliar(nota)
                break
            else:
                self.interface.invalid_input()

    def denunciar_receita(self, receita, lista_denuncia: list):
        motivo = ''
        while len(motivo) <= 0:
            # denuncia = {}
            motivo = self.interface.menu_denunciar_motivo()

            if motivo in ("1", "2", "3"):
                denuncia = Denuncia(receita.nome_usuario, motivo, receita.nome)
                lista_denuncia.append(denuncia)
                
            elif motivo == "0":
                break
            else:
                self.interface.invalid_input()
                motivo = ''

# user_atual == j.login:
    def denunciar_avaliar(self, receita, lista_denuncia, user_atual):
        usados = []
        while True:
            comando = self.interface.menu_comando_avaliar()
            jaAvaliou = False
            jaDenunciou = False
            if comando == '1' and (comando not in usados):
                for nome in receita.users_avaliacoes:
                    if nome == user_atual:
                        jaAvaliou = True

                if not jaAvaliou:
                    self.avaliar_receita(receita)
                    receita.users_avaliacoes.append(user_atual)
                else:
                    self.interface.invalid_input()
                usados.append('1')

            elif comando == '2' and (comando not in usados):
                for nome in receita.users_denuncias:
                    if nome == user_atual:
                        jaDenunciou = True

                if not jaDenunciou:
                    self.denunciar_receita(receita, lista_denuncia)
                    receita.users_denuncias.append(user_atual)
                else:
                    self.interface.invalid_input()
                usados.append('2')
            elif comando == '0':
                usados = []
                break
            else:
                self.interface.invalid_input()

    # funcoes (base) para o administrador

    def acessar_denuncias(self, lista_denuncia: list, lista_users):
        self.interface.menu_lista_denuncia(lista_denuncia)
        ver_denuncias = True
        while ver_denuncias:
            comand = self.interface.menu_verificar_receita_user()
            if comand == '1':
                nome_usuario, nome_receita = self.interface.menu_nome_receita()
                found = ''
                for i in lista_denuncia:
                    if i.user == nome_usuario and i.receita == nome_receita:
                        found = 's'
                        # metodo para retornar os dados
                        self.verificar_receitas(nome_usuario, nome_receita, lista_users)
                if found == '':
                    self.interface.erro404()

            elif comand == '2':
                nome_usuario, nome_receita = self.interface.menu_nome_receita()
                found = ''
                for i in range(len(lista_denuncia)):
                    dado_encontrado = False
                    for c, v in lista_denuncia[i].items():
                        if nome_usuario == c:
                            if nome_receita == v[0]:
                                dado_encontrado = True
                    if dado_encontrado:
                        # colocar o pop da lista do usuario
                        found = 's'
                        self.deletar_receitas(
                            nome_usuario, nome_receita, lista_users)
                        lista_denuncia.pop(i)
                if found == '':
                    self.interface.erro404()

            elif comand == '0':
                ver_denuncias = False

            else:
                self.interface.invalid_input()

    # verificar a conta do usuario

    def verificar_receitas(self, nome_usuario, nome_receita, lista_users):
        for i in lista_users:
            if i.login == nome_usuario:
                for j in i.lista_receitas:
                    if j.nome == nome_receita:
                        self.interface.retornar_receita(j)
                        self.interface.retorno_print(
                            f" \n ### Receita denunciada: {j.nome} ### \n {'-='*30}")

    # deletar a receita do usuario

    def deletar_receitas(self, nome_usuario, nome_receita, lista_users):
        for i in lista_users:
            if i.login == nome_usuario:
                for j in range(len(i.lista_receitas)):
                    if i.lista_receitas[j].nome == nome_receita:
                        i.lista_receitas.pop(j)

    def mostrar_todas_receitas(self, lista_users):
        lista_total = []  # era uma lista de listas das receitas dos usuarios agora é uma lista com apenas receitas
        for i in lista_users:
            for j in i.lista_receitas:
                lista_total.append(j)
        return lista_total
