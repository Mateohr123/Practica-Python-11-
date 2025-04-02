numero = int(input("Ingresa un número de tres digitos por favor: "))

digito1 = numero % 10  
digito2 = (numero // 10) % 10  
digito3 = numero // 100  

numero_invertido = digito1 * 100 + digito2 * 10 + digito3

print(f"El número {numero} al revés es: {numero_invertido}")
