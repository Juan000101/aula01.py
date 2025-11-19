class Retangulo:
    #Membros da classe

    #1° Membro - Atributos
    __base:float
    __altura:float

    #2° Membro - Propriedades
    #Propriedade da base
    @property #Pegar o valor do atributo base
    def base(self):
        return self.__base
    @base.setter #Definir o valor do atributo base
    def base(self, base:float):
        if altura < 0:
            base = 0
        self.__base = base

    #Propriedade da altura
    @property #Pegar o valor do atributo altura
    def altura(self):
        return self.__altura
    @altura.setter #Definir o valor do atributo altura
    def altura(self, altura:float):
        if altura < 0:
            altura = 0
        self.__altura = altura

    #3° Membro - Construtor
    def __init__(self, base:float ,altura: float):
        self.altura = altura
        self.base = base
   
    #4° Membro - Metodos
    def area(self) -> float:
        return self.altura * self.base

    def perimetro(self) -> float:
        return (self.altura * 2) + (self.base * 2)
   
    def diagonal(self) -> float:
        from math import sqrt, pow
        return sqrt(pow(self.base, 2) + pow(self.altura, 2))
   
    def dadosRetangulo(self) -> str:
        saida = f'''Area = {self.area()}\n
        Perimetro = {self.perimetro()}\n
        Diagonal = {self.diagonal()}'''
        return saida
#-----Fim classe-------

#Inicio programa principal

#Entrada de dados
base = float(input("Digite a base do retangulo: "))
altura = float(input("Digite a altura do retangulo: "))
#Instanciar o objeto do tipo retangulo
retangulo = Retangulo(base, altura)
#Saida de dados
print(retangulo.dadosRetangulo())