# Crea un función EscribirCentrado, que reciba como parámetro un texto y lo escriba centrado en pantalla (suponiendo una anchura de 80 columnas; pista: deberás escribir 40 - longitud/2 espacios antes del texto). Además subraya el mensaje utilizando el carácter =.

texto = input("Ingrese un texto: ")

def centrarTexto(texto):
    print(texto.center(80))
    

centrarTexto(texto)
