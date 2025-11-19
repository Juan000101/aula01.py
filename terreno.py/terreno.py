class Terreno:
    #Membros da classe
    #1°membro atributos
    __largura : float
    __comprimento : float


    #2° Membros - propiedades


    #Propiedades largura
    @property
    def largura(self):
        return self.__largura
    @largura.setter
    def largura(self, largura:float):
        self.__largura = largura
    #Propiedade do comprimento
    @property
    def comprimento(self):
        return self.__comprimento
    @comprimento.setter
    def comprimento(self, comprimento:float):
        self.__comprimento = comprimento
    
    #3° Membro - construtor
    def __init__(self, largura:float, comprimento: float):
        self.comprimento = comprimento
        self.largura = largura

        #4° Membro - metodos
    def __area(self) ->  float:
        return self.comprimento * self.largura
    def __preco(self, preco: float) -> float:
        return self.__area() * preco
    
    def dadosTerreno(self, preco: float) -> str:
        saida = f'''Largura: {self.largura}
        Comprimento: {self.comprimento}
        Area: {self.__area():.2f}
        preco: {self.__preco(preco):.2f}'''
        return saida
    #-------Fim--da--classe
    
    #Inicio programa principal
    #Entrada de dados
try:
    largura = float(input("Digite a largura do terreno: "))
    comprimento = float(input("Digite o comprimento do terreno: "))
    preco = float(input("Digite o preço do metro quadrado:"))
    #Instanciar o objeto do tipo terreno
    terreno = Terreno(largura, comprimento)
    #saida de dados
    print(terreno.dadosTerreno(preco))
except ValueError:
    print("Error: Entrada inválida. Por favor, digite um número valido.")
    