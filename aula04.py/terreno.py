#problema terreno
#declaração de variáveis
largura:float
comprimento:float
#entrada de dados
largura= (float(input("Digite a largura do terreno em metros: ")))
comprimento= (float(input("Digite o comprimento do terreno em metros: ")))
valor_metro_quadrado=float(input("Digite o valor do metro quadrado do terreno em reais: "))
#processamento de dados
area=largura * comprimento
preco = area * valor_metro_quadrado
#saida de dados
print(f"a área do terreno é de {area}")
print(f"o preco do terreno é de R${preco:.2f}")