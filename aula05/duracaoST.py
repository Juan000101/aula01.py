import streamlit as st
#probelma duração de tempo
TITULO ="calculadora duração de tempo"
st.title(TITULO)
#entrega de dados
tempo = st.number_input("digite o tempo em segundos:")
#processamento de dados
horas = tempo // 3600 // 60 #calculo dos minutos 
minutos = (tempo // 60) % 60 #calculo dos minutos
segundos = tempo % 60 #calculo de segundos
#saida de dados
st.write(f"{horas}horas, {minutos}minutos e {segundos} segundos.")
