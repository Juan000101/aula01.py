class triangulo:
    #atributos
    a:int
    b:int
    c:int

    def area(self) -> float:
        from math import sqrt
        p = ( self.a + self.b + self.c) / 2 
        area =(p * (p - self.a) * (p - self.b) * (p - self.c))
        return area



trianguloX = triangulo()
trianguloY = triangulo()

print("Digite as medidas do triangulo X:")
trianguloX.a = int(input("Digite a medida a"))
trianguloX.b = int(input("Digite a medida b"))
trianguloX.c = int(input("Digite a medida c"))
print("Digite as medidas do triangulo Y")
trianguloY.a = int(input("Digite a medida a"))
trianguloY.b = int(input("Digite a medida b"))
trianguloY.c = int(input("Digite a medida c"))

trianguloX.area()
trianguloY.area()
if areax > areay :
    saida = " Area do triangulo X eh maior que a entrada do triangulo Y"
elif areay > areax :
    saida = " Area do triangulo Y eh maior que a entrada do triangulo X"
else:
    saida  = "As areas dos triangulo X e Y sao iguais"
print(f"A area do triangulo X = {areax:.1f}")
print(f"A area do triangulo Y = {areay:.1f}")
print(saida) 