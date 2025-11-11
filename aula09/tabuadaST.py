import streamlit as st


#tabuada
#titulo da pagina
TITULO ="Tabuada"
st.title(TITULO)
st.set_page_config(TITULO)
#Entrada de dados
n = None
try:
    n = int(st.text_input("Deseja a tabuada de qual numero:"))
    for i in range(1,11):
        saida = f" {n} X {i} = {n*i}"
        st.markdown(f""" {saida}"""    )
except ValueError:
    if n is None:
        st.warning("Digite algum valor")
    else:
        st.error("Digite somente números inteiros")


