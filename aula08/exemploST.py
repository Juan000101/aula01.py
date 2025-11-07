import streamlit as st

# --- Interface Streamlit para corresponder ao modelo visual ---

st.title("Verificação de Triângulo e Cálculo de Perímetro ou Área")

# --- Entradas de dados (iguais ao modelo visual) ---

# Usamos colunas para alinhar melhor os rótulos e os campos, se necessário, mas o layout vertical padrão já é similar
st.subheader("Digite os valores:")

A = st.number_input("Digite o valor de A:", value=10.0, format="%.2f", key="input_a")
B = st.number_input("Digite o valor de B:", value=10.0, format="%.2f", key="input_b")
C = st.number_input("Digite o valor de C:", value=0.0, format="%.2f", key="input_c")

# Adiciona um botão para processar a entrada
if st.button("Processar Valores"):
    
    # Validação básica para garantir que os valores sejam positivos
    if A <= 0 or B <= 0 or C <= 0:
        st.error("Por favor, insira valores positivos maiores que zero para A, B e C.")
    else:
        # --- Lógica do Exercício ---
        
        # Condição de existência do triângulo (Desigualdade Triangular)
        if (A + B > C) and (A + C > B) and (B + C > A):
            # É um triângulo, calcula o perímetro
            perimetro = A + B + C
            
            # Exibição do resultado como no modelo visual
            st.write("Os valores formam um triângulo.")
            st.write(f"Perimetro = **{perimetro:.1f}**")
            
            st.header("Triângulo formado por A, B e C")
            # --- Código que simula a imagem do triângulo com HTML/CSS ---
            st.markdown(
                f"""
                <div style='text-align: center; font-size: 80px; padding: 20px;'>
                    <p style='margin:0;'>▲</p>
                    <p style='display: flex; justify-content: space-between; width: 200px; margin: auto;'>
                        <span style='font-size: 14px;'>{A:.2f}</span>
                        <span style='font-size: 14px;'>{B:.2f}</span>
                        <span style='font-size: 14px;'>{C:.2f}</span>
                    </p>
                </div>
                """, unsafe_allow_html=True
            )

        else:
            # Não é um triângulo, calcula a área do trapézio (A e B bases, C altura)
            area_trapezio = ((A + B) * C) / 2
            
            # Exibição do resultado
            st.write("Os valores não formam um triângulo.")
            st.write(f"Area = **{area_trapezio:.1f}**")
            st.header("Não foi possível formar um triângulo.")