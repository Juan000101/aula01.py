
from streamlit import header, write, text_input, button, warning, success, error , 
from math import sqrt,pow
#função python
def calculo (deltaClodoaldo):
     valor = (sqrt(deltaClodoaldo)) / (2*a)
     return valor

header('Calculadora de Bhaskara')
write("calculadora de raízes \n\n de uma equação de segundo grau")
write("ax² + bx + c = 0")
#entrada de dados 
a = text_input('Digite  o valor de a:', icon='🅰')
b = text_input('Digite o valor de b:', icon='🅱')
c = text_input('digite o valor de c:', icon='🅲')
#processamento de dados
if button('calcular raízes'):
    try:
            a = float(a)#Convertendo string para dados 
            b = float(b)    
            c = float(c)
            delta =pow(b,2) - 4*a*c
            if delta < 0:
                 warning("A equação não possui raízes reais.")
            elif delta == 0:
                 raiz = (-b + calculo(delta))
                 success(f"A equação possui uma raiz real: \n  Raiz: {raiz}")
            else:
                 raiz1 = (-b + calculo(delta))
                 raiz2 = (-b - calculo(delta))
            success(f"As raízes da equação são: \n Raiz 1: {raiz1} \n Raiz 2: {raiz2}")
    except ValueError: 
       error("Por favor, insira valores válidos para a, b e c.")
    except ZeroDivisionError:
         error("O valor de 'a' não pode ser zero em uma equanção do segundo grau")