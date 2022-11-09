#Crear una función recursiva que permita calcular el factorial de un número. Realiza un programa principal donde se lea un entero y se muestre el resultado del factorial.

from factorial import factorial

numero = 0

print("** Factorial **\n")

numero = int(input("Ingrese un numero, para otener su factorial: "))

factorial(numero)
print("\n-----------------------")
print("El resultado es: ", factorial(numero))
print("-----------------------")  
