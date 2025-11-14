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
        return self.saldo
    def dadosDoProduto(self) -> str:
        saida = f'''
            Dados do produto:
            \tNome do produto : {self.nome}
            \tValor da compra do produto: R$ {self.preco}
            \tquantidade de estoque: {self.saldo}
            \tValor valor total em estoque: R$({self.valorTotalEmEstoque():.2f}
            '''
        return saida