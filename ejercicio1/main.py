# Pida al usuario cadenas de texto hasta que se escriba “cancelar”.
#Al salir con “cancelar” deben mostrarse todas las cadenas concatenadas con un guión.


palabra = input("Ingrese una palabra: ")
listaPalabras = []
while palabra != "cancelar":
  listaPalabras.append(palabra)
  palabra = input("Ingrese una palabra: ")
  
print("-".join(listaPalabras))

