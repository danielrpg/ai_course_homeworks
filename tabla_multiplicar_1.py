'''
    Ejercicio Propuesto:
    Mostrar la tabla de multiplicar de cualquier numero ingresado por teclado FOR
    Salida: 1x5=5
            2x5=10
'''


numero = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))

for i in range(1, 11):
    resultado = i * numero
    print(f"{i} x {numero} = {resultado}")
