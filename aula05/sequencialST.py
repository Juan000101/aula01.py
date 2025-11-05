import streamlit as st
#
TITULO ="calculadora troco de pagamento"
st.title(TITULO)
preco = st.number_input("digite o preco do produto:", min_value=0.0, format="%.2f")
#processamento de dados
quantidade = st.number_input ("digite a quantidade comprada", min_value=0.0, format="%.2f")
dinheiro = st.number_input("digite o valor em dinheiro:", min_value=0.0, format="%.2f") 
troco = dinheiro - (preco * quantidade)
st.write(f"{troco} {dinheiro} e {quantidade} .")