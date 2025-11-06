import streamlit as st
st.title("simulação de lançamento de dardo")
'''Simulação de lançamento de tres dardos. O objetivo do aplicativo mostrar o dardo com a maior distancia'''
#Entrada de dados 
st.header("Inserir as tres distancias dos dardos lançados pelo jogador.")
coluna1, coluna2, coluna3 = st.columns(3)
with coluna1:
    dardo1 = st.number_input("distancia do 1° dardo:", min_value=0.0)
with coluna2:
    dardo2 = st.number_input("distancia do 2° dardo:", min_value=0.0)
with coluna3:
    dardo3 = st.number_input("distancia do 3° dardo:", min_value=0.0)
#estrutura de controle de decisao
if (dardo1 > dardo2) and (dardo1 > dardo3):
    dardo_vencedor = "Dardo 1"
elif (dardo2 > dardo1) and (dardo2 > dardo3):
    dardo_vencedor = "Dardo 2"
else:
    dardo_vencedor = "Dardo 3"      
#saida de dados
if st.button("apresentar resultados de lançamento"):
    st.write(f"o dardo com a maior distancia foi: {dardo_vencedor}")