# como usuario quiero ingresar por teclado mi nombre y dos numeros para que me devuelva un saludo personalizado por consola y la suma de los dos numeros con la leyenda "La suma de los numeros es: "

nombre = input("Imgrese su nombre: ")
num1 = int(input("\nIngresa un numero: "))
num2 = int(input("\nIngresa otro numero: "))
print("\nHola",nombre, ", la suma de los numeros es:",(num1 + num2))