import streamlit as st
import math as mt
#problemas medidas 
TITULO = "calculo de área de um quadrado, triângulo e trapézio"
st.title(TITULO)
#Entrada de dados 
medidaA = st.number_input("inserir a medida A:")
medidaB = st.number_input("inserir a medida B:")
medidaC = st.number_input("inserir a medida C:")    
#processamento de dados 
areaQuadrado = mt.pow(medidaA, 2)
areaTringulo = (medidaA * medidaB) /2
areaTrapezio = ((medidaA * medidaB) * medidaC) /2
#saida de dados 
st.write(f"A área do quadrado é: {areaQuadrado:.4f}")
st.write(f"A área do triângulo é: {areaTriangulo:.4f}")
st.write(f"A área do trapézio é: {areaTrapezio:.4f}")
