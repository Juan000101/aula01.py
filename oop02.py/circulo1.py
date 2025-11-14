import calculadora as c
#instanciação do objeto
circulo = c.calculadora1()
#entrada de dados 
raio = float(input("Digite o valor de raio"))
#processamento de dados 
circunferencia = circulo.circunferencia(raio)
area = circulo.area(raio)
#saida de dados 
print(f'''Circunferencia: {circunferencia:.2f}
      Area: {area:.2f}
      PI: {circulo.PI}      
''')