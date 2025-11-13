import streamlit as st

def calcular_estatisticas(lista_pessoas):
    """Calcula média e porcentagem usando apenas Python puro."""
    if not lista_pessoas:
        return 0, 0, []

    total_pessoas = len(lista_pessoas)
    soma_alturas = sum(p['altura'] for p in lista_pessoas)
    altura_media = soma_alturas / total_pessoas

    pessoas_menor_16 = [p['nome'] for p in lista_pessoas if p['idade'] < 16]
    porcentagem_menor_16 = (len(pessoas_menor_16) / total_pessoas) * 100
    
    return altura_media, porcentagem_menor_16, pessoas_menor_16

def main():
    st.title("Processamento de Dados de Pessoas (Streamlit Simples)")

    # --- Inicialização do Estado da Sessão ---
    # Usamos st.session_state para manter os dados vivos enquanto o usuário interage
    if 'pessoas' not in st.session_state:
        st.session_state.pessoas = []
    if 'n_pessoas' not in st.session_state:
        st.session_state.n_pessoas = 0
    if 'step' not in st.session_state:
        st.session_state.step = 'input_n'

    # --- Passo 1: Inserir N pessoas ---
    if st.session_state.step == 'input_n':
        st.header("1. Quantidade de Pessoas")
        
        n_input = st.number_input("Digite o número total de pessoas", min_value=1, step=1, key="num_pessoas_input")
        
        if st.button("Confirmar Quantidade"):
            st.session_state.n_pessoas = n_input
            st.session_state.step = 'input_data'
            st.experimental_rerun() # Recarrega para ir para o próximo passo

    # --- Passo 2: Inserir dados individuais ---
    elif st.session_state.step == 'input_data':
        current_person_index = len(st.session_state.pessoas) + 1

        if current_person_index <= st.session_state.n_pessoas:
            st.header(f"2. Dados da {current_person_index}ª pessoa")
            
            with st.form(key=f'person_form_{current_person_index}'):
                # Campos de entrada
                nome = st.text_input("Nome")
                idade = st.number_input("Idade", min_value=0, step=1)
                altura = st.number_input("Altura (m)", min_value=0.0, step=0.01)
                
                submit_button = st.form_submit_button(label="Salvar Dados")

                if submit_button:
                    if nome and altura > 0:
                        st.session_state.pessoas.append({'nome': nome, 'idade': idade, 'altura': altura})
                        st.success(f"Dados de {nome} salvos! Faltam {st.session_state.n_pessoas - current_person_index} pessoas.")
                        st.experimental_rerun() # Recarrega para o próximo formulário
                    else:
                        st.error("Por favor, preencha todos os campos corretamente.")
        else:
            # Todos os dados foram coletados, passar para resultados
            st.session_state.step = 'results'
            st.experimental_rerun()

    # --- Passo 3: Exibir Resultados ---
    elif st.session_state.step == 'results':
        st.header("3. Resultados Finais")

        # Processamento usando Python puro
        altura_media, porcentagem_menor_16, nomes_menor_16_lista = calcular_estatisticas(st.session_state.pessoas)
        nomes_menor_16_str = ", ".join(nomes_menor_16_lista)

        st.subheader("Análise Estatística")
        st.metric("Altura Média", f"{altura_media:.2f} m")
        st.metric("Pessoas com menos de 16 anos (%)", f"{porcentagem_menor_16:.1f}%")

        st.subheader("Nomes (Menos de 16 anos)")
        st.write(nomes_menor_16_str if nomes_menor_16_str else "Nenhum nome encontrado.")
        
        if st.button("Recomeçar"):
            # Reseta o estado para começar do zero
            st.session_state.pessoas = []
            st.session_state.n_pessoas = 0
            st.session_state.step = 'input_n'
            st.experimental_rerun()


if __name__ == "__main__":
    main()