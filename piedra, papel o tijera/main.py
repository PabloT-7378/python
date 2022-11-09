# crear juego piedra papel o tijera

import random
from pipati import pipati

print("##########################")
print("# Piedra, Papel o Tijera #")
print("##########################\n")

print("1. Piedra")
print("2. Papel")
print("3. Tijera\n")
print("4. Salir\n")

scorePc = 0
scoreUsuario = 0

print("-"*30)
opcionUsuario = 1
while opcionUsuario == 1 or opcionUsuario == 2 or opcionUsuario == 3:
  opcionUsuario = int(input("Ingresa una opcion: "))
  
  opcionPc = random.randint(1,3)

  print("Pc eligio la opcion:",opcionPc)

  ganador = pipati(opcionUsuario, opcionPc)

  print("-"*30)

  if ganador == "usuario":
    scoreUsuario = scoreUsuario +1
  elif ganador == "pc":
    scorePc = scorePc + 1
  else:
    continue
print("Puntaje")
print("=======")
print(f"Usuario: {scoreUsuario}")
print(f"Pc: {scorePc}")
