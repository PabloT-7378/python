#Se pide ingresar tantos nombres de personas, y para cada uno contar la cantidad de  caracteres que contiene. Cuando ya no se ingresen más nombres deberá imprimir el total  de nombres ingresados y el total de caracteres.

listaNom = []
nombres = input("ingrese un nombre o exit para salir: ")
caracteres = 0
while nombres != "exit":
  listaNom.append(nombres)
  caracteres = caracteres + len(nombres)
  nombres = input("ingrese un nombre o exit para salir: ")

print("Se ingresaron", len(nombres), "nombres.")
print("Y suman", caracteres, "caracteres en total.")
  