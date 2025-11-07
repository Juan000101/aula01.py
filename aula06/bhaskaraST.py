from streamlit import header, write, text_input, button, warning, success, error
from math import sqrt, pow

# Note: As variáveis 'a', 'b' e 'c' são definidas globalmente pelo Streamlit
# nos inputs, mas precisamos garantir que a função 'calculo' tenha acesso a elas,
# ou passar 'a' como parâmetro, que é a melhor prática.

# Função Python corrigida
def calculo (delta_clodoaldo, valor_a):
    # O nome da função interna da biblioteca 'sqrt' já lida com a raiz quadrada.
    # A variável 'valor' aqui não é o resultado final da raiz, mas uma parte do cálculo.
    # Renomeei 'deltaClodoaldo' para 'delta_clodoaldo' por padrão de estilo (snake_case).
    valor = (sqrt(delta_clodoaldo)) / (2 * valor_a)
    return valor

header('Calculadora de Bhaskara')
write("Calculadora de raízes de uma equação de segundo grau")
write("ax² + bx + c = 0")

# Entrada de dados (Streamlit gerencia o estado dessas variáveis como strings)
a_str = text_input('Digite o valor de a:', key='input_a')
b_str = text_input('Digite o valor de b:', key='input_b')
c_str = text_input('Digite o valor de c:', key='input_c')

# Processamento de dados
if button('Calcular raízes'):
    # Garantimos que as variáveis para raiz1 e raiz2 sejam inicializadas
    # para evitar 'UnboundLocalError' caso o bloco 'delta == 0' não seja executado.
    raiz1 = None
    raiz2 = None

    try:
        # Convertendo strings para floats APÓS o clique do botão
        a = float(a_str)
        b = float(b_str)
        c = float(c_str)

        # Validação crucial: 'a' não pode ser zero para uma equação de segundo grau
        if a == 0:
            error("O valor de 'a' não pode ser zero em uma equação do segundo grau.")
        else:
            delta = pow(b, 2) - 4 * a * c

            if delta < 0:
                warning("A equação não possui raízes reais.")
            elif delta == 0:
                # Passamos 'a' como parâmetro para a função calculo
                raiz1 = (-b) / (2 * a) # Simplificado o cálculo aqui
                success(f"A equação possui uma raiz real: Raiz única: {raiz1:.2f}")
            else:
                # Passamos 'a' como parâmetro para a função calculo
                raiz1 = (-b + sqrt(delta)) / (2 * a) # Simplificado o cálculo aqui
                raiz2 = (-b - sqrt(delta)) / (2 * a) # Simplificado o cálculo aqui
                # A mensagem de sucesso estava fora do bloco 'else' principal no seu código original
                success(f"As raízes da equação são: \n Raiz 1: {raiz1:.2f} \n Raiz 2: {raiz2:.2f}")

    except ValueError:
        # Captura se o usuário deixou um campo vazio ou digitou algo que não é número
        error("Por favor, insira valores numéricos válidos para a, b e c.")
