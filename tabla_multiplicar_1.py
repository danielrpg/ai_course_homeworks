
numero = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))

for i in range(1, 11):
    resultado = i * numero
    print(f"{i} x {numero} = {resultado}")
