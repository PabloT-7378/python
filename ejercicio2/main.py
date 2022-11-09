#Hacer un programa que solicite un número entero al usuario e imprima por pantalla desde  ese número hasta 0. 
#Ejemplo: ingresa 6, deberá mostrar 6 5 4 3 2 1 0 
numero = 0
numero = int(input("Ingresa un numero entero: "))

while numero != 0:
  print(numero)
  numero = numero - 1


