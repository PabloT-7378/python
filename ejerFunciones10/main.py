# Escribir dos funciones que permitan calcular: La cantidad de segundos en un tiempo dado en horas, minutos y segundos. La cantidad de horas, minutos y segundos de un tiempo dado en segundos. Escribe un programa principal con un menú donde se pueda elegir la opción de convertir a segundos, convertir a horas,minutos y segundos o salir del programa.

from funciones import cantidad_segundos
from funciones import segundos_a_segundos_minutos_y_horas

print("Convertidor\n")

print("Ingrese una opcion:")
print("1. Convertir a segundos")
print("2. Convertir a horas, minutos y segundos\n")

opcion = int(input(": "))

if opcion == 1:
  horas = int(input("\nIngrese la cantidad de horas: "))
  minutos = int(input("Ingrese la cantidad de minutos: "))
  segundos = int(input("Ingrese la cantidad de segundos: "))
  cantidad_segundos(horas, minutos, segundos)

elif opcion == 2:
  segundos = int(input("Ingresa la cantidad de segundos: "))
  segundos_a_segundos_minutos_y_horas(segundos)

else:
  print("Opcion incorrecta")
 