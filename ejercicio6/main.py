#Se ingresa un numero entero (del 0 al 100), la computadora realizara tantos intentos de  adivinarlo hasta lograrlo, en el mismo rango de 0 a 100. Se desea saber:  - En cuantos intentos logro dar con el numero ingresado. - Cual fue el menor y el mayor número de los fallidos


from random import randint


numero = int(input("Ingresa un numero del 1 al 100: "))
listaNum = []
aleatorio = [randint(1,100)]

listaNum = listaNum + aleatorio
if aleatorio == numero:
    print("Adivinaste")

else:
  while aleatorio != numero:
    
    aleatorio = randint(1,100)
    listaNum.append(aleatorio)
    
    if aleatorio == numero:
        print("Adivinaste")
        break
print("Lo lograste en, ",len(listaNum), "intentos.")
print("El numero mas bajo fue el: ",min(listaNum))
print("El numero mas alto fue el: ",max(listaNum))