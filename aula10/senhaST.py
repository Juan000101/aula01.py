import streamlit as st
#Problema senha fixa
st.title("sistema de login simples")
#Declaração de constantes
#crdenciais fixas
USUARIO ="clodoaldo"
SENHA = "senha123"

#Entrada de dados
usuario_entrada = st.text_input("Nome do usuario")
senha_entrada = st.text_input("senha", type="password")
#Estrutura de controle loop
botao = st.button("Logar")

#tentativas
MAXIMO_TENTATIVAS = 3

if 'tentativas' not in st.session_state:
    st.session_state.tentativas = 0

if botao is True:
    if st.session_state.tentativas >= MAXIMO_TENTATIVAS:
        st.error("maximo de tentativas atingido. acesso bloqueado")
    else:
        #usar while para controlar as tentativas
        while st.session_state.tentativas < MAXIMO_TENTATIVAS:
            if usuario_entrada == USUARIO and senha_entrada == SENHA:
                st.success("login bem sucedido!")
                st.session_state = 0 
                break
            else:
                st.session_state.tentativas += 1
                st.warning(f"Credenciais invalaidas. Tentativa {st.session_state.tentativas} de {MAXIMO_TENTATIVAS}")
                break
            