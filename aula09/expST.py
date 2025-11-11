import streamlit as st

# Função porcemtagem (Note a digitação: 'porcemtagem')
def porcemtagem(cobaia, total): # A função precisa receber o total como argumento
    if total == 0:
        return 0
    return (cobaia / total) * 100

# A função qtd está incorreta na lógica original (falta o que é 'qtd' na linha 23 e 24, e não acumula corretamente)
# Mantive a função, mas ela não faz o que o código principal tenta fazer
def qtd(total):
    # Esta função está incompleta na sua definição original e não pode ser usada como está
    # total += qtd # Isso causa um erro de tipo
    return total # Retorna o valor original para evitar erro, mas a lógica está quebrada

# Experiencias com cobaias
st.title("Laboratório de cobaias")

# Declarção de variaveis de controle
# Estas variáveis zerao a cada interação do Streamlit
total_cobaias = 0
total_ratos = 0
total_sapos = 0
total_coelhos = 0

n = st.number_input("Digite o valor de experimentos:", min_value=0, step=1)

# Estrutura de controle - PARA - loop determinado em python
# Este loop executa de uma vez só quando a página carrega ou interage
for i in range(n):
    quantidade = st.number_input(f"experimento {i+1} - Quantidade de cobaias utilizadas:", min_value=1, step=1, key=f'q_{i}')
    tipo = st.selectbox(f" Experimento {i+1} - Tipo de cobaia (C:Coelho, R:rato, S:Sapo,):", options=['C', 'R', 'S'], key=f't_{i}') # 'r' foi alterado para 'R' para consistência
    
    # processamento de dados (isso só processa na primeira execução)
    # total_cobaias += quantidade # Linha original comentada
    
    # A chamada de função qtd estava incorreta e sem atribuição
    total_cobaias += quantidade
    
    # Correção de indentação e sintaxe de comparação
    if tipo == 'C':
        # total_coelhos +- quantidade # Sintaxe errada, usei +=
        total_coelhos += quantidade
    # Correção de indentação
    elif tipo == 'R':
        total_ratos += quantidade # Atribuição direta, pois a função qtd não funciona aqui
    # Correção de indentação
    elif tipo == 'S':
        total_sapos += quantidade
        
# A partir daqui, a indentação do seu código original estava errada. 
# Tudo a seguir deve estar fora do loop 'for'.
if total_cobaias > 0:
    # Correção de digitação: 'porcentagem' para 'porcemtagem' (como definido na função)
    percentual_coelhos = porcemtagem(total_coelhos, total_cobaias)
    percentual_ratos = porcemtagem(total_ratos, total_cobaias)
    percentual_sapos = porcemtagem(total_sapos, total_cobaias)
else:
    percentual_coelhos = percentual_ratos = percentual_sapos = 0

# saida de dados
st.subheader("Resultados:")
st.write("Total de cobaias utilizadas :", total_cobaias)
st.write("Total de coelhos utilizadas :", total_coelhos)
st.write("Total de ratos utilizadas :", total_ratos)
st.write("Total de sapos utilizadas :", total_sapos) # 'csapos' corrigido para 'sapos'

# percentual
st.write(f"percentual de coelhos: {percentual_coelhos:.2f} %")
st.write(f"percentual de ratos: {percentual_ratos:.2f} %")
st.write(f"percentual de sapos: {percentual_sapos:.2f} %")

