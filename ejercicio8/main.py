# Ingresar por teclado usuario y clave. Informar los siguientes casos: a. Si usuario=”pepito” y clave=”1234” informar “Bienvenido pepito!” b. Si usuario=”pepito” y clave no es “1234” informar “Contraseña incorrecta” c. Si usuario no es “pepito” y clave= “1234” informar “Usuario incorrecto”


usuario = input("Ingrese un Usuario: ")
clave = input("Ingrese su clave: ")

if usuario == "pepito" and clave == "1234":
  print("Bienvenido pepito!")

elif usuario == "pepito" and clave != "1234":
  print("Contraseña incorrecta")

elif usuario != "pepito" and clave == "1234":
  print("Usuario incorrecto")

else:
  print("Datos invalidos")
