import streamlit as st
st.title("Problema terreno")
#entrada de dados 
st.write("Digite a largura do terreno em metros:")
largura = st.number_input("largura(m):")
st.write("digite o comprimento do terreno em metros:")
comprimento = st.number_input ("comprimento(m):")
st.write("digite o valor do metro quadrado em reais:")
valor_m2 = st.number_input("valor do m²(R$):")
#procesamento de dados 
area = largura * comprimento 
preco = area * valor_m2 
#saida de dados
st.write(f"A área do terreno é de {area} metros quadrados.")
