import produtoOOP as p #importar o modulo
class produto:
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

p1 = p.produto()  #instanciar o objeto
#entrada de dados
print("Digite os dados do produto")
p1.nome = str(input("\tNome:"))
p1.preco = float(input("\tPreco:R$"))
p1.saldo = int(input("\tQuantidade:"))
#saida de dados
print(p1.dadosDoProduto())
q = int(input("Digite o numero de produtos a ser adicionado ao estoque:"))
p1.AdicionarProdutos(q)
print("--Dados autualizado--")
print(p1.dadosDoProduto())
