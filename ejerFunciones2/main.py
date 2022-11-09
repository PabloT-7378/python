# Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. Crea una función EsMultiplo que reciba los dos números, y devuelve si el primero es múltiplo del segundo.

print("** Ingresa 2 numeros enteros para saber si son multiplos **\n")

num1 = int(input("Ingresa el primer numero entero: "))
num2 = int(input("Ingresa el segundo numero entero: "))

def esMultiplo(num1, num2):
  if num1 % num2 == 0:
    print("Son multiplos!!!")

  else:
    print("NO son multiplos...")
    
esMultiplo(num1, num2)