# Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo. Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior.

print("**Ingrese 6 numeros para saber el mayor y menor**\n")
lista = []

def calcularMaxMin(lista):
  print("\nEl mayor es: ", max(lista))
  print("El menor es: ", min(lista))
for numero in range(0,6):
  numero = int(input("Igrese un numero: "))
  lista.append(numero)

calcularMaxMin(lista)

print("\n***Gracias por utilizar este programa.***")