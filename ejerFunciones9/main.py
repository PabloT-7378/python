#Crear una función que calcule el MCD de dos número por el método de Euclides. El método de Euclides es el siguiente: Se divide el número mayor entre el menor. Si la división es exacta, el divisor es el MCD. Si la división no es exacta, dividimos el divisor entre el resto obtenido y se continúa de esta forma hasta obtener una división exacta, siendo el último divisor el MCD. Crea un programa principal que lea dos números enteros y muestre el MCD.
from euclides import mcd

print("**Calcular MCD**\n")

numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el segundo numero: "))
 
print("\nEl MCD de ", numero1," y ", numero2," es: ", mcd(numero1, numero2))