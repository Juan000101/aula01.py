print("Inserir as medidas do triangulo X")
ax = int(input("Digite a medida a:"))
bx = int(input("Digite a medida b:"))
cx = int(input("Digite a medida c:"))
print("inserir as medidas do trinagulo Y")
ay = int(input("digite a medida a:"))
by = int(input("digite a medida b:"))
cy = int(input("digite a medida c:"))
p = (ax + bx + cx) / 2
areax = (p * (p - ax) * (p - bx) * (p - cx)) ** 0.5
p = (ay + by + cy) / 2
areay = (p * (p - ay) * (p - by) * (p - cy)) ** 0.5
if areax > areay:
    saida = "A area do triangulo x eh maioe que a area do triangulo Y"
elif areay > areax:
    saida = "A area do triagulo Y eh maior que a area do triangulo X"
else:
    saida = "A areas dos triangulos sao iguais"
print(f"Area do triangulo X = {areax:.1f}")
print(f"A area do triangulo Y = {areay:.1f}")
print(saida)