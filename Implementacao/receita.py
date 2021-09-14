class Receita:
    def __init__(self):
        self.nome = None
        self.nome_usuario = None  # nome do criador
        self.palavras_chave = None
        self.doce_salgado = None
        self.avaliacoes = []
        self.media_avaliacao = 0
        self.gluten = None
        self.porcoes = None
        self.lista_ingredientes = None      # lista de ingredientes
        self.descricao = None
        self.modo_preparo = None
        self.users_avaliacoes = []
        self.users_denuncias = []

    def setNome(self, nome):
        self.nome = nome

    def setNomeUser(self, nome_usuario):
        self.nome_usuario = nome_usuario

    def setPalavrasChave(self, palavras_chave):
        self.palavras_chave = palavras_chave

    def setDoceSalgado(self, doce_salgado):
        self.doce_salgado = doce_salgado

    def setPorcoes(self, porcoes):
        self.porcoes = porcoes

    def setGluten(self, gluten):
        self.gluten = gluten

    def setListaIngredientes(self, lista_ingredientes):
        self.lista_ingredientes = lista_ingredientes

    def setDescricao(self, descricao):
        self.descricao = descricao

    def setModoPreparo(self, modo_preparo):
        self.modo_preparo = modo_preparo

    def retorno(self):
        return self.nome, self.doce_salgado, self.media_avaliacao, self.gluten, self.porcoes, self.lista_ingredientes, self.descricao, self.modo_preparo

    def avaliar(self, nota):
        self.avaliacoes.append(nota)
        media = 0
        for i in self.avaliacoes:
            media += i
        self.media_avaliacao = media/len(self.avaliacoes)
        return self.media_avaliacao


class ReceitaBuilder():
    def __init__(self, receita, SisInterface):
        self.receita = receita
        self.interface = SisInterface

    def buildNome(self, nome):
        self.receita.setNome(nome)

    def buildNomeUser(self, nome_usuario):
        self.receita.setNomeUser(nome_usuario)

    def buildPalavrasChave(self):
        palavras_chave = self.interface.input_palavra_chave()
        self.receita.palavras_chave = palavras_chave

    def buildDoceSalgado(self):
        doce_salgado = self.interface.input_doce_salgado()
        self.receita.doce_salgado = doce_salgado

    def buildPorcoes(self):
        porcoes = self.interface.input_porcoes()
        self.receita.porcoes = porcoes

    def buildGluten(self):
        gluten = self.interface.input_gluten()
        self.receita.gluten = gluten

    def buildListaIngredientes(self):
        lista_ingredientes = self.interface.input_lista_ingredientes()
        self.receita.lista_ingredientes = lista_ingredientes

    def buildDescricao(self):
        descricao = self.interface.input_descricao()
        self.receita.descricao = descricao

    def buildModoPreparo(self):
        modo_preparo = self.interface.input_modo_preparo()
        self.receita.modo_preparo = modo_preparo
