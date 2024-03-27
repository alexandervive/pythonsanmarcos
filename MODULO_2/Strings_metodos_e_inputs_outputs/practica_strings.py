correo = "alexanderpatino@live.com"
print(type("alexanderpatino@live.com"))

mensaje = "Tu correo es: " + correo
print(mensaje)

#Saltos de linea

print("Alexander\nGino\nAlvaro")
print (r"C:\Documentos\Nombre\Gino")

letra_cancion = """
linea 1
linea 2
linea 3

inicio del coro
linea 1 
linea 2
linea 3
"""
print (letra_cancion)

#Agregamos el caracter "\" al inicio y al final para que no realice un salto de linea en nuestro string extenso de 3 lineas. 
letra_cancion2 = """\
linea 1
linea 2
linea 3

inicio del coro
linea 1 
linea 2
linea 3\
"""
print (letra_cancion2)

"""
Tambien se usa el """ """ para hacer un comentario siempre y cuando no haya una variable
"""

menu = """\


\
"""

#Concatenacion sin el simbolo '+'
nombre_completo = "Alexander" "Patino"
print(nombre_completo)

presentacion = "Mi nombre completo es: " + nombre_completo
print(presentacion)

#Indexar es acceder a una porcion de una parte de una cadena de texto mediante un indice
pais = "Republica Dominicana"
#Indexacion: variable(indice)
print("El indice de pais en la posicion 2 es: ", pais[9])
print("El indice de pais en -4 es: ", pais[-4])

#La funcion Len nos retorna la longitud de nuestra cadena de texto
print(len(pais))

#slicing/ cortes
