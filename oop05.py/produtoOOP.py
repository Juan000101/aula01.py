class Produto:#Super classe
    #1° Membro - Atributos privados
    __nome:str
    __preco:float
    __quantidade:int
   
    #2° Membro - Propriedades protegidas
    #Propriedades do atributo Nome
    @property
    def _nome(self)->str:
        return self.__nome
    @_nome.setter
    def _nome(self, nome:str)-> str:
        self.__nome = nome
    #Propriedades do atributo Preço
    @property
    def _preco(self) -> float:
        return self.__preco
    @_preco.setter
    def _preco (self, preco:float) -> float:
        self.__preco = preco
    #Propriedade do atributo quantidade
    @property
    def _quantidade(self) -> int:
        return self.__quantidade
    @_quantidade.setter
    def _quantidade(self, quantidade:int) ->int:
        self.__quantidade = quantidade
   
    #3° Membro - Construtor
    def __init__(self, nome: str, preco: float, quantidade: int):
        self._nome = nome
        self._preco = preco
        self._quantidade = quantidade
   
    #4° Membro - Métodos
    def operacao(self):
        print("Operação de Produto")
        print(f"Nome: {self._nome}")        
       
class Software(Produto):#Subclasse de Produto
    #1° Membro - Atributo
    __licenca:str
   
    #2° Membro - Propriedade
    @property
    def _licenca(self) -> str:
        return self.__licenca
    @_licenca.setter
    def _licenca(self, licenca:str) ->str:
        self.__licenca = licenca
   
    #3° Membro - Construtor
    def __init__(self, nome: str, preco: float, quantidade: int, licenca: str):
        super().__init__(nome, preco, quantidade)
        self._licenca = licenca

class Hardware(Produto):#Subclasse de Produto
    #1° Membro - Atributo
    __garantia:int
   
    #2° Membro - Propriedade
    @property
    def _garantia(self) -> int:
        return self.__garantia
    @_garantia.setter
    def _garantia(self, garantia:int) ->int:
        self.__garantia = garantia
   
    #3° Membro - Construtor
    def __init__(self, nome: str, preco: float, quantidade: int, garantia: int):
        super().__init__(nome, preco, quantidade)
        self._garantia = garantia

#----Fim classes----

#-----Main code-----

software = Software("Adobe", 1000, 10, "2010")
hardware = Hardware("Dell", 2000, 10, 6)

software.operacao()
hardware.operacao()