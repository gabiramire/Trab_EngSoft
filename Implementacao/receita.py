class Receita:
    def __init__(self, nome, nome_usuario, palavras_chave, doce_salgado, porcoes, gluten, lista_ingredientes, descricao, modo_preparo):
        self.nome = nome
        self.nome_usuario = nome_usuario  # nome do criador
        self.palavras_chave = palavras_chave
        self.doce_salgado = doce_salgado
        self.avaliacoes = []
        self.media_avaliacao = 0
        self.gluten = gluten
        self.porcoes = porcoes
        self.lista_ingredientes = lista_ingredientes      # lista de ingredientes
        self.descricao = descricao
        self.modo_preparo = modo_preparo
        self.users_avaliacoes = []
        self.users_denuncias = []

    def retorno(self):
        return self.nome, self.doce_salgado, self.media_avaliacao, self.gluten, self.porcoes, self.lista_ingredientes, self.descricao, self.modo_preparo

    def avaliar(self, nota):
        self.avaliacoes.append(nota)
        media = 0
        for i in self.avaliacoes:
            media += i
        self.media_avaliacao = media/len(self.avaliacoes)
        return self.media_avaliacao
