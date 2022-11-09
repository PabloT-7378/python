# Diseñar una función que calcule el área y el perímetro de una circunferencia. Utiliza dicha función en un programa principal que lea el radio de una circunferencia y muestre su área y perímetro.

print("Area y Perimetro de una circunferencia")
print("======================================\n")

radio = float(input("Ingrese el Radio de la circunferencia: "))
print("........................................")

def areaPerimetro(radio):
  area = 3.14159265 * radio * radio
  perimetro = 2 * 3.14159265 * radio
  
  print("El area de la circunferencia es: ", area)
  print("El perimetro de la circunferencia es: ", perimetro)

areaPerimetro(radio)
print("........................................")
print("***Fin***")
