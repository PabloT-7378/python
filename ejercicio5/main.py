#El usuario ingresa un valor N. Escriba un programa que imprima los primeros N números terminados en 5. Ejemplo: ingresa 4, deberá mostrar 5 15 25 35 
print("Ingrese un numero del 1 al 9\n")

numero = int(input("Ingrese el numero: "))
suma = [0,5,15,25,35,45,55,65,75,85,95]
if numero == 1:
  print(suma[1])
  
elif numero == 2:
  print(suma[1:3])
  
elif numero == 3:
  print(suma[1:4])

elif numero == 4:
  print(suma[1:5])

elif numero == 5:
  print(suma[1:6])

elif numero == 6:
  print(suma[1:7])
  
elif numero == 7:
  print(suma[1:8])

elif numero == 8:
  print(suma[1:9])

elif numero == 9:
  print(suma[1:10])
  
else:  
  print("fin")
    
    


