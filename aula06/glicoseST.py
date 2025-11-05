import streamlit as st

st.title("Classificação de niveis de glicose no sangue")
st.markdown("""
| Nível de Glicose | Classificação |
|------------------|---------------|
|   0 - 70 mmol/L  | Hipoglicemia  |
|     71 - 100     |   normal      |
|    101 - 140     |  Pré-diabetes |
|    141 ou mais   |  Diabetes     |
""")
#Entrada de dados 
glicose = st.number_input("Insira o valor da glicose no sangue (mg/dL):",min_value=0)
st.button("Classificar")#Botão para classificar o nível de glicose
if st.button("Classificar"):
    if glicose <=70:
        st.write("Nível de glicose classificado como: hipoglicemia")
    elif 71 >= glicose <=100:
        st.write("Nível de glicose classificado como: normal")
        st.balloons()
    elif 101 >= glicose <=140:
        st.write("Nível de glicose classificado como: pré-diabetes")
    else:
        st.write("Nível de glicose classificado como: Diabetes")