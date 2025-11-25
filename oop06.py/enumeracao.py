from enum import Enum 

class Estados_Pedidos(Enum):
    PAGAMENTO = 1
    ENVIADO = 2
    ENTREGUE = 3
    CANCELADO = 4

#Exemplo de uso 
print(Estados_Pedidos(2))
print(Estados_Pedidos.CANCELADO)
print(Estados_Pedidos.ENVIADO.name)#imprimir o nome do estado
print(Estados_Pedidos.ENTREGUE.value)#imprimir o valor do estado
print(Estados_Pedidos(1).name)#Imprimir o nome do estado a parit do valor
print(Estados_Pedidos.SENAI.value)#imprimir o valor com estado SENAI