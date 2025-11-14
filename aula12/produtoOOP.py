class produto:
    #atributos
    nome:str
    preco:float
    saldo:int 
    #Metodos
    def valorTotalEmEstoque(self) -> float:
        return self.preco * self.saldo
    def AdicionarProdutos(self, quantidade) -> int:
        self.saldo = self.saldo + quantidade
        return self.saldo
    def RemoverProdutos(self, quantidade) -> int:
        self.saldo = self.saldo - quantidade