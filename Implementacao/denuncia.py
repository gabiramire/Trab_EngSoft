class Denuncia:
    def __init__(self, user, motivo, receita):
        self.user = user  
        self.motivo = motivo
        self.receita = receita
    
    def get_motivo(self):
        if self.motivo == '1':
            return 'Contêm conteúdo inapropriado'
        elif self.motivo == '2':
            return 'Não é uma receita'
        elif self.motivo == '3':
            return 'Receita plagiada'
               

