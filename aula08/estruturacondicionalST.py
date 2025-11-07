import streamlit as st

# Título da entrada dos dados aqui
st.title("Verificação de Triângulo e Cálculo de Perímetro ou Área")
st.write("Digite os três valores nos campos abaixo:")
# Entradas de dados
A = st.number_input("Digite o valor de A:", value=0.0, format="%.2f")
B = st.number_input("Digite o valor de B:", value=0.0, format="%.2f")
C = st.number_input("Digite o valor de C:", value=0.0, format="%.2f")

if st.button("Calcular"):
    
    if A <= 0 or B <= 0 or C <= 0:
        st.error("Por favor, insira valores positivos maiores que zero.")
    else:
        
        # Verifica a entrada do triângulo aqui mesmo
        if (A + B > C) and (A + C > B) and (B + C > A):
            # Se for mesmo um triângulo, calcular o perímetro
            perimetro = A + B + C
            st.success("Os valores formam um triângulo.")
            st.write(f"Perímetro = {perimetro:.1f}")
        else:
            # Se não for triângulo então ele calcula a área do trapézio
            area = ((A + B) * C) / 2
            st.info("Os valores não formam um triângulo.")
            st.write(f"Área = {area:.1f}")