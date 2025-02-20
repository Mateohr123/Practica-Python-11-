radio = float(input("Ingrese el radio del círculo: "))

perimetro = 2 * math.pi * radio
area = math.pi * radio ** 2

print(f"\nPara un círculo de radio {radio}:")
print(f"El perímetro es: {perimetro:.2f}")
print(f"El área es: {area:.2f}")
