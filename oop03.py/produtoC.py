import produtoOOP as p

#entrada de dados 
print("entre com os dados do produto:")
nome = input("Nome:")
preco = float(input("Preço: R$:" \
""))
saldo = int(input("Quantidade:"))

#ps = p.produto(nome, preco, saldo)
ps = p.produto(nome, preco)
#saida de dados
print(ps.dadosDoProduto())
