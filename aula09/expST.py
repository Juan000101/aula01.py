import streamlit as st
#Experiencias com cobaias
st.title("Laboratório de cobaias")
#Declarção de variaveis de controle
total_cobaias = 0
total_ratos = 0
total_sapos = 0
total_coelhos = 0
n = st.number_input("Digite o valor de experimentos:", min_value =0, step=1)

#Estrutura de controle - PARA - loop determinado em python 
for i in range (n):
    quantidade = st.number_input(f"experimento {i+1} - Quantidade de cobaias ultilizadas:", min_value=1, step=1)
    tipo = st.selectbox(f" Experimento {i+1} - Tipo de cobaia (C:Coelho, R:rato, S:Sapo,):", options=['C', 'r', 'S'])

    #processmento de dados 
    total_cobaias += quantidade
    if tipo == 'C':
        total_coelhos +- quantidade
    elif tipo== 'R':
        total_ratos += quantidade
    elif tipo== 'S':
        total_sapos += quantidade 
if total_cobaias > 0:
    percentual_coelhos = (total_coelhos / total_cobaias) * 100
    percentual_ratos = (total_ratos / total_cobaias) * 100
    percentual_sapos = (total_sapos / total_cobaias) * 100
else:
    percentual_coelhos = percentual_ratos = percentual_sapos = 0

    #saida de dados
    st.subheader("Resulatados:")
    st.write("Total de cobaias ultilizadas :", total_cobaias)
    st.write("Total de coelhos ultilizadas :", total_coelhos)
    st.write("Total de ratos ultilizadas :", total_ratos)
    st.write("Total de csapos ultilizadas :", total_sapos)
    #percentual
    st.write(f"percentual de coelhos: {percentual_coelhos:.2f} %")
    st.write(f"percentual de ratos: {percentual_ratos:.2f} %")
    st.write(f"percentual de sapos: {percentual_sapos:.2f} %")


        

