#Grettel Aguilar y Mateo Hernandez
def sumar(a,b):
    return a + b
    
def restar(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b

def dividir (a,b):
    if b == 0:
        return "Error: División por cero"
    return a / b
def mostrar_menu():
    print("Calculadora Básica Mateo Hernandez y Grettel Aguilar")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
def calculadora():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ")
        
