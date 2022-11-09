# Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor.
# Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, solamente tenemos tres oportunidades para intentarlo.
from login import login

print("***Inicio***\n")
print("----------------------")
usuario = input("Ingrese usuario: ")
contraseña = input("Ingrese contraseña: ")
contador = 0   
login(usuario, contraseña)
  
if usuario != "usuario1" and contraseña != "asdasd":
  contador = contador + 1
  for intento in range(0, 2):
    usuario = input("Ingrese usuario: ")
    contraseña = input("Ingrese contraseña: ")
    login(usuario, contraseña)
    contador = contador + 1
    print("Los intentos fallidos fueron ", contador)
    if contador == 3:
      print("\n##############################")
      print("# Se terminaron los intentos #")
      print("##############################")
    
elif usuario == "usuario1" and contraseña == "asdasd":
  print("Los intentos fallidos fueron, ", contador)
  print("Fin")
  

 
