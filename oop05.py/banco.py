class ContaPessoaFisica:#Super classe
    #1° Membro - Atributos privados
    __numeroDaConta:int
    __titular:str
    __saldo:float

    #2° Membro - Propriedades
    #Propriedade do numero da conta
    @property
    def _numeroDaConta(self) ->int :
        return self.__numeroDaConta
    @_numeroDaConta.setter
    def _numeroDaConta(self, numero:int) ->int :
        self.__numeroDaConta = numero
    #Propriedade titular
    @property
    def _titular(self) -> str:
        return self.__titular
    @_titular.setter
    def _titular(self, nome:str) ->str:
        self.__titular = nome
    #Propriedade saldo
    @property
    def _saldo(self) -> float:
        return self.__saldo
    @_saldo.setter
    def _saldo(self, saldo:float) ->float:
        self.__saldo = saldo
   
    #3° Membro - Construtor
    def __init__(self, numeroDaConta:int, titular:str, saldo:float):
        self._numeroDaConta = numeroDaConta
        self._titular = titular
        self._saldo = saldo
   
    #4° Membro - Métodos
    def depositar(self, deposito:float) -> float:
        self._saldo += deposito
    def saque(self, saque:float) -> float:
        self._saldo -= saque - 5.00
    def dados(self) -> str:
        saida = f'''
        Numero: {self._numeroDaConta}
        Titular: {self._titular}
        Saldo: {self._saldo}
'''
        return saida

    #---Fim super classe---

class ContaPessoaJuridica(ContaPessoaFisica):#Sub classe da classe Conta Pessoa Fisica
    #1° Membro - Atributos
    __limite:float

    #2° Membro - Propriedades
    @property
    def _limite(self) -> float:
        return self.__limite
    @_limite.setter
    def _limite(self, limite) -> float:
        self.__limite = limite

    #3° Membro - Construtor
    def __init__(self, numeroDaConta, titular, saldo, limite):
        super().__init__(numeroDaConta, titular, saldo)
        self._limite = limite
   
    #4° Membro - Métodos
    def limiteDisponivel(self) -> float:
        return self._limite
   
    def saque(self, saque:float) -> float:#Sobrescrita do método saque
        self._saldo -= saque
        return self._saldo
   
    def dados(self) -> str:
        saida = f'''
        {super().dados()}        Limite: {self._limite}
'''
        return saida


    #----Fim sub classe----

class ContaPoupanca(ContaPessoaFisica):
    #1° Membro - Atributos
    __taxaDeJuros = 0.05

    #2° Membro - Propriedades
    @property
    def _taxaDeJuros(self) -> float:
        return self.__taxaDeJuros
   
    #3° Membro - Construtor
    def __init__(self, numeroDaConta, titular, saldo):
        super().__init__(numeroDaConta, titular, saldo)
   
    #4° Membro - Métodos
    def saque(self, saque:float) -> float:#Sobrescrita do método saque
        self._saldo -= saque
        return self._saldo
    def atualizarSaldo(self) -> float:
        self._saldo += self._saldo * self._taxaDeJuros
        return self._saldo
#---------------Fim classes-------------

#Programa Principal

conta1 = ContaPessoaFisica(123456, "Clodoaldo", 1000)
conta2 = ContaPessoaJuridica(654321, "Adriano", 500, 100)
conta3 = ContaPoupanca(789, "Vitor", -100)

#Saida de dados 1
print(f'''{conta1.dados()} {conta2.dados()} {conta3.dados()}''')
conta1.depositar(200)
print(f'Saldo após depósito na conta 1: {conta1._saldo}')
conta1.saque(50)
print(f'Saldo após saque na conta 1: {conta1._saldo}')
#Saida de dados 2
print(f'''{conta1.dados()} {conta2.dados()} {conta3.dados()}''')
conta2.saque(100)
print(f'Saldo após saque na conta 2: {conta2._saldo}')
conta2.depositar(300)
print(f'Saldo após depósito na conta 2: {conta2._saldo}')