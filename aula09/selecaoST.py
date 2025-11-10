import streamlit as st

#Problema lanchonete
st.title("Lanchonete do Clodoaldo")
st.header("Menu de opções do restaurante")
st.subheader("Opções de lanches")
st.markdown(
"""
|Código|Descrição do item| Preço  |
|------|-----------------|--------|
| 1001 |X-Burger---------|R$ 8,00 |
| 1001 |X-SENAI----------|R$ 10,00|
| 1003 |X-Campeao--------|R$ 12,00|
| 1005 |X-ESP32----------|R$ 15,00|
| 1005 |X-C37------------|R$ 18,00|
"""
)
opcao = st.selectbox("Selecione o codigo do lanche desejado:",options=["1001", "1002", "1003", "1004", "1005"] )
codigo = int(opcao)#Converte a string selecionada em numero inteiro
quantidade = st.number_input("Digite a quantidade desejada:", min_value=0, step=1)
#Estrutura de controle de contole de selecao
match codigo:
    case 1001:
        preco = 8.00
    case 1002:
        preco = 10.00
    case 1003:
        preco = 12.00
    case 1004:
        preco = 15.00
    case 1005:
        preco = 18.00
    case _: 0.00 
#Caso o codigo seja invalido
#processamento de dados
total = preco * quantidade
#Saida de dados
st.subheader("Total a pagar: R$ " + (str(total)))