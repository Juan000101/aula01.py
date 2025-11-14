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
p1.nome = input("\tNome")
p1.preco = float(input("\tPreco:R$"))
p1.saldo = int(input("\quantidade:"))
#saida de dados
print("Dados do produto")
print(f"\tNome do produto: {p1.nome}")
print(f"\tValor de comopra: R$ {p1.preco})")
print(f"\tQuantidade em estoque: {p1.saldo}")
print(f"Valor total em estoque: R$ {p1.ValorTotalEmEstoque():.2f}") 