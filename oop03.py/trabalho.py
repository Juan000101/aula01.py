import streamlit as st

class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def eh_mais_velha(self, outra_idade: int) -> bool:
        return self.idade > outra_idade


class Funcionario:
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.salario = salario

    def salario_medio(self, outro) -> float:
        return (self.salario + outro.salario) / 2

st.title("Programação Orientada a Objetos em Streamlit")

# aqui é pra abrir e fachar
if "form1_ativo" not in st.session_state:
    st.session_state.form1_ativo = False

if "form2_ativo" not in st.session_state:
    st.session_state.form2_ativo = False

#aqui fica o layout de duas colunas
col_left, col_right = st.columns(2)

#aqui ta a função do primeiro mais velho
with col_left:
    st.header("Função 1: Pessoa mais velha")

    if st.button("Calcular Pessoa Mais Velha"):
        st.session_state.form1_ativo = True

    if st.session_state.form1_ativo:
        with st.form("form_pessoa"):
            nome1 = st.text_input("Nome da Pessoa 1")
            idade1 = st.number_input("Idade da Pessoa 1", min_value=0, step=1)

            nome2 = st.text_input("Nome da Pessoa 2")
            idade2 = st.number_input("Idade da Pessoa 2", min_value=0, step=1)

            enviar = st.form_submit_button("Enviar")

            if enviar:
                pessoa1 = Pessoa(nome1, idade1)
                pessoa2 = Pessoa(nome2, idade2)

                if pessoa1.eh_mais_velha(pessoa2.idade):
                    st.success(f"A pessoa mais velha é: **{pessoa1.nome}**")
                elif pessoa2.eh_mais_velha(pessoa1.idade):
                    st.success(f"A pessoa mais velha é: **{pessoa2.nome}**")
                else:
                    st.info("As duas pessoas têm a **mesma idade**.")

                st.session_state.form1_ativo = False


#aqui ja fica a função do salario medio das duas pessoas

with col_right:
    st.header("Função 2: Salário Médio dos Funcionários")

    if st.button("Calcular Salário Médio"):
        st.session_state.form2_ativo = True

    if st.session_state.form2_ativo:
        with st.form("form_func"):
            nome_f1 = st.text_input("Nome do Funcionário 1")
            sal_f1 = st.number_input("Salário do Funcionário 1", min_value=0.0, step=100.0)

            nome_f2 = st.text_input("Nome do Funcionário 2")
            sal_f2 = st.number_input("Salário do Funcionário 2", min_value=0.0, step=100.0)

            enviar = st.form_submit_button("Enviar")

            if enviar:
                f1 = Funcionario(nome_f1, sal_f1)
                f2 = Funcionario(nome_f2, sal_f2)

                media = f1.salario_medio(f2)

                st.success(f"O salário médio dos funcionários é: **R$ {media:.2f}**")

                st.session_state.form2_ativo = False
