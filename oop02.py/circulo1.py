from calculadora import calculadora1
raio = float(input("Digite o valor de raio:3"))
#processamento de dados 
circunferencia = calculadora1.circunferencia(raio)
area = calculadora1.area(raio)
#saida de dados 
print(f'''Circunferencia: {circunferencia:.2f}
      Area: {area:.2f}
      PI: {calculadora1.PI}      
''')