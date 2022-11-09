# programar un sistema de creditos que pida el nombre del usuario y su ingreso medio, a partir de los datos ingresados el programa arrojara el maximo credito disponible.
# las lineas de credito son: ingresos inferiores a $ 50000 son clase A. ingresos entre $50000 y $100000 son clase B. ingresos mayores a 100000 son clase C.         en todos los casos el valor de la cuota no debe superar 1/3 del ingreso, hasta en 24 cuotas. 
print("***********************")
print("* Sistema de creditos *")
print("***********************\n")

nombre = input("Ingresa tu nombre: ")
ingresoPromedio = int(input("Ingresa tu sueldo promedio: "))
claseA = ingresoPromedio / 3 * 24
claseB = ingresoPromedio / 3 * 24
claseC = ingresoPromedio / 3 * 24

if ingresoPromedio < 50000:
  print("su credito es de ", int(claseA))

elif ingresoPromedio >= 50000 and ingresoPromedio < 100000:
  print("su credito es de ", int(claseB))

elif ingresoPromedio >= 100000:
  print("su credito es de ", int(claseC))

else:
  print("Sin credito disponible")