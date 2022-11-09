# Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media. El programa pedirá el número de días que se van a introducir.

print("Temperatura media diaria")
print("________________________\n")

temp1 = float(input("Ingrese la temperatura minima: "))
temp2 = float(input("Ingrese la temperatura maxima: "))


def temperaturaMedia(temp1, temp2):
  print((temp1 + temp2)/2)
  
temperaturaMedia(temp1, temp2)