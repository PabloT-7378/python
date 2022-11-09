

def pipati(opcionUsuario,opcionPc):
  ganador = ""
  if opcionUsuario == opcionPc:
    print("Empate")
    ganador = ""

  elif opcionUsuario == 1 and opcionPc == 2:
    print("Gana Pc, papel mata piedra")
    ganador = "pc"

  elif opcionUsuario == 1 and opcionPc == 3:
    print("Gana Usuario, piedra mata tijera")
    ganador = "usuario"

  elif opcionUsuario == 2 and opcionPc == 1:
    print("Gana Usuario, papel mata piedra")
    ganador = "usuario"

  elif opcionUsuario == 2 and opcionPc == 3:
    print("Gana Pc, tijera mata papel")
    ganador = "pc"

  elif opcionUsuario == 3 and opcionPc == 1:
    print("Gana Usuario, tijera mata papel")
    ganador = "usuario"

  elif opcionUsuario == 3 and opcionPc == 2:
    print("Gana Pc, piedre mata tijera")
    ganador = "pc"

  elif opcionUsuario == 4:
    print("Fin del juego")

  else:
    print("Opcion invalida")

  return ganador