from abc import ABC, abstractmethod

class Conta(ABC):
    __numero:str
    __saldo:float

    @property
    def _numero(self) -> str:
        return self.__numero
    @_numero.setter
    def _numero(self, numero:str) -> str:
        if numero == "" or numero == None:
            raise ValueError("Valor invalido")
        else:
            self.__numero = numero
    @property
    def _saldo(self) -> float:
        return self.__saldo
    @_saldo.setter
    def _saldo(self, saldo:float) -> float:
        if saldo < 0:
            raise ValueError("Valor invalido para saldo de conta")
        else:
            self.__saldo = saldo

    def __init__(self, numero:str, saldo:float):
        self._numero = numero
        self._saldo = saldo

    def depositar(self, valor:float) -> None:
        self._saldo += valor

    def sacar(self, valor:float) -> None:
        self._saldo -= valor

#---Fim super classe ---

class ContaPoupanca(Conta):
    __taxaJuros:float

    @property
    def _taxa(self) -> float:
        return self.__taxaJuros
    @_taxa.setter
    def _taxa(self, valor:float) -> float:
        if valor < 0:
            raise ValueError("Valor de taxa de juros invalida")
        else:
            self.__taxaJuros = valor
   
    def __init__(self, numero, saldo, taxa):
        super().__init__(numero, saldo)
        self._taxa = taxa

    def aplicarJuros(self) -> None:
        self._saldo += self._saldo * ( self._taxa / 100 )
#---Fim classe ContaPoupanca---#

class ContaParaEmpresa(Conta):
    __limite:float

    @property
    def _limite(self) -> float:
        return self.__limite
    @_limite.setter
    def _limite(self, limite: float) -> float:
        if limite < 0 :
            raise ValueError("Valor invalido de limite")
        else:
            self.__limite = limite
   
    def __init__(self, numero, saldo, limite):
        super().__init__(numero, saldo)
        self._limite = limite

    def solicitarCredito(self, valor:float) -> float:
        self._limite -= valor
        self._saldo  += valor

#--Fim classes----

conta1 = ContaParaEmpresa("123456", 20000.00, 50000.00)
conta2 = ContaPoupanca("666", 500, 25)

print(f"Saldo conta empresa: R$ {conta1._saldo:.2f}")
print(f"Limite conta empresa: R$ {conta1._limite:.2f}")

print(f"Saldo conta poupanca: R$ {conta2._saldo:.2f}")
print(f"Taxa de juros conta poupanca: {conta2._taxa:.2f}%")

conta1.sacar(2500.00)
conta2.sacar(100.00)

print(f"Saldo conta empresa: R$ {conta1._saldo:.2f}")
print(f"Limite conta empresa: R$ {conta1._limite:.2f}")

print(f"Saldo conta poupanca: R$ {conta2._saldo:.2f}")
print(f"Taxa de juros conta poupanca: {conta2._taxa:.2f}%")