# Se desea determinar el estado de un alumno según la nota obtenida y mostrar si el alumno aprobó, recupera o perdió la materia. La nota obtenida puede ser alguna de las siguientes letras ‘A’, ‘B’, ‘C’ o ‘D’. Los estados posibles son aprobado, recupera, o pierde la materia. Para las notas ‘A’ y ‘B’ se considera aprobado la materia, para la nota ‘C’ se debe recuperar y para la nota es ‘D’ se pierde la materia. Ejemplo: ingresa “C”, deberá mostrar que debe recuperar.

print("Estado del alumno")
print("*****************\n")

nota = input("Igrese la nota optenida: ")

if nota == "A" or nota == "B":
  print("Exelente, aprovaste")
elif nota == "C":
  print("Debes recuperar la materia")
elif nota == "D":
  print("La materia esta perdida")
else:
  print("Nota no corresponde")
