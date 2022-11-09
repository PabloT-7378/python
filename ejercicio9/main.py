# Realice un algoritmo para determinar cuánto se debe pagar por equis cantidad de lápices considerando que si son 1000 o más el costo es de 85 centavos; de lo contrario, el precio es de 90 centavos. Represéntelo con el pseudocódigo y el diagrama de flujo. Ejemplo: ingresa 500 , deberá mostrar 450 pesos

cantidadDeLapices = int(input("ingrese la cantidad de lapices que desea: "))

porMenor = cantidadDeLapices * 0.90

porMayor = cantidadDeLapices * 0.85

if cantidadDeLapices < 1000:
  print("Le va a costar, ", int(porMenor), "pesos.")

elif cantidadDeLapices >= 1000:
  print("le va a costar, ", int(porMayor) * 0.85, "pesos.")