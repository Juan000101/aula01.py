import streamlit as st
import math as mt
st.header('Calculadora de Bhaskara')
st.write("calculadora de raízes \n de uma equação de segundo grau")
st.write("ax² + bx + c = 0")
#entrada de dados 
a = st.text_input('Digite  o valor de a:')
b = st.text_input('Digite o valor de b:')
c = st.text_input('digite o valor de c:')
#processamento de dados
if st.button('calcular raízes'):
    try:
            a = float(a)#Convertendo string para dados 
            b = float(b)    
            c = float(c)
            delta =mt.pow(b,2) - 4*a*c
            if delta < 0:
                 st.warning("A equação não possui raízes reais.")
            elif delta == 0:
                 raiz = -b / (2*a)
                 st.success(f"A equação possui uma raiz real: {raiz}")
            else:
                 raiz1 = (-b + mt.sqrt(delta)) / (2*a)
                 raiz2 = (-b - mt.sqrt(delta)) / (2*a)
            st.success(f"A equação possui duas raízes reais: {raiz1} e {raiz2}")
    except: 
        st.error("Por favor, insira valores válidos para a, b e c.")