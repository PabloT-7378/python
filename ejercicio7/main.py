# Ingresar por teclado 3 números enteros y distintos e informar cual es el mayor. Ejemplo: si ingresa 3, 20 y 8, mostrará: 20

print("Ingresa tres numeros\n")

num1 = int(input("Ingresa el primer numero: "))
num2 = int (input("Ingresa el segundo numero: "))
num3 = int(input("Ingresa el tercer numero: "))

if num1 > num2 and num1 > num3:
    print("El mayor es:", num1)

elif num2 > num1 and num2 > num3:
    print("El mayor es: ", num2)

elif num3 > num2 and num3 > num1: 
    print("El mayor es: ", num3)

else: 
  "ingreso opcion incorrecta"