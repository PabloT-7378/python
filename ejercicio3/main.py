# Dado un número ingresado por el usuario queremos mostrar en pantalla la suma desde 1  hasta ese número inclusive. Ejemplo: ingresa 5, deberá mostrar 15.

numero = int(input("Ingrese un numero: "))
suma = 0
for num in range(1, numero+1):
  suma = suma + num

print(suma)

