class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura):

        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura

    def PassarCanal(self, botao):
        if botao == '+':
            print('Subindo de canal')
        else:
            print('Descendo de canal')

    def Volume(self, botao):
        if botao == '+':
            print('Subindo de volume')
        else:
            print('Descendo de volume')

    def AbrirNetflix(self):
        print('Netflix abrindo...')
    def FecharNetflix(self):
        print('Fechando Netflix')
    def DesligarTV(self):
        print('Desligando TV...')

    def ExibirInfo(self):
        print(self.cor, self.altura, self.profundidade, self.largura)

controle = ControleRemoto('preto', 36, 23, 28)
controle.PassarCanal('+')
controle.PassarCanal('-')
controle.Volume('+')
controle.Volume('-')
controle.AbrirNetflix()
controle.FecharNetflix()
controle.DesligarTV()
controle.ExibirInfo()