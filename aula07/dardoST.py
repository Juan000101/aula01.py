import streamlit as st
def grafico(datsu1,datsu2,datsu3):
    #apresentação de grafico exibindo lançamento
    st.area_chart([0, datsu1], use_container_width=True,height=200,color="#eaff00")
    st.area_chart([0, datsu2], use_container_width=True,height=200,color="#f65200")
    st.area_chart([0, datsu3], use_container_width=True,height=200,color="#5100ff")







st.title("simulação de lançamento de dardo")
'''Simulação de lançamento de tres dardos. O objetivo do aplicativo mostrar o dardo com a maior distancia'''
#Entrada de dados 
st.header("Inserir as tres distancias dos dardos lançados pelo jogador.")
coluna1, coluna2, coluna3 = st.columns(3)
with coluna1:
    dardo1 = st.number_input("distancia do 1° dardo:", min_value=0)
with coluna2:
    dardo2 = st.number_input("distancia do 2° dardo:", min_value=0)
with coluna3:
    dardo3 = st.number_input("distancia do 3° dardo:", min_value=0)
maior_distancia = max(dardo1, dardo2, dardo3)
#estrutura de controle de decisão
if (dardo1 > dardo2) and (dardo1 > dardo3):
    dardo_vencedor = "Dardo 1"
elif (dardo2 > dardo1) and (dardo2 > dardo3):
    dardo_vencedor = "Dardo 2"
elif (dardo3 > dardo1) and (dardo3 > dardo2):
    dardo_vencedor = "Dardo 3"
elif (dardo1 == dardo2) or (dardo1 == dardo3):
    dardo_vencedor = "Empate"     
#saida de dados
if st.button("apresentar resultados de lançamento"):
    if dardo_vencedor == "Empate":
        st.write("houve empate sem vencedores")
else:
    st.write(f"o dardo com a maior distancia é {dardo_vencedor} com {maior_distancia}")
    grafico(dardo1,dardo2,dardo3)