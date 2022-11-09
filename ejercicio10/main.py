# “Bodega Campo” es un restaurante de campo dedicado a ofrecer grandes parrilladas, previa reserva del evento; sus tarifas son las siguientes: el costo de plato por persona es de $95.00, pero si el número de personas es mayor a 200 pero menor o igual a 300, el costo es de $85.00. Para más de 300 personas el costo por platillo es de $75.00. Se requiere un algoritmo que ayude a determinar el presupuesto que se debe presentar a los clientes que deseen realizar un evento. Ejemplo: ingresa 250 personas , deberá mostrar 21.250,00 pesos

print("Parrilla Bodega Campo")
print("=====================\n")

personas = int(input("Ingrese la cantidad de personas: "))

promo1 = personas * 95
promo2 = personas * 85
promo3 = personas * 75

if personas <= 200:
  print("El costo para ", personas, "personas sera de: ", promo1, "pesos.")
elif personas > 200 and personas <= 300:
  print("El costo para ", personas, "personas sera de: ", promo2, "pesos.")
elif personas > 300:
  print("El costo para ", personas, "personas sera de: ", promo3, "pesos.")
