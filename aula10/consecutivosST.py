import streamlit as st
st.title("Calculadora pares consecutivos")
numero = st.number_input("Digite o numero inteiro", step=1)
botao = st.button("calcular")
contagem  = 1
if botao:
    if (numero%2) !=0:
        numero += 1
    soma = numero
    while contagem < 5:
        numero += 2
        contagem += 1
        soma += numero
    st.write(soma)