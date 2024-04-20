correo = "alexanderpatino@live.com"
print(type("alexanderpatino@live.com"))

#Concatenacion
mensaje = "Tu correo es: " + correo
print(mensaje)

#Saltos de linea

print("Alexander\nGino\nAlvaro")
#Para evitar el salto de linea, utilizamos el comando (r"texto")
print (r"C:\Documentos\Nombre\Gino") #Si no se usa "r", no se va a ejecutar bien porque la "\n" en "Nombre" saltara de linea

"""
Las 3 comillas no solo nos ayudan a realizar comentarios con multiples lineas
sino que tambien nos ayudan a guardar string sin necesidad de agregar saltos de lineas en cada espacio que un desee
"""
# Si las 3 comillas estan compiladas en una variable va a ser una cadena de texto grande
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
Ingrese una opcion de calculo:
1. Suma de dos numeros
2. Resta de dos numeros
3. Calcular intereses ganados\
"""
print(menu)

#Concatenacion sin el simbolo '+'
nombre_completo = "Alexander" "Patino"
print(nombre_completo)

presentacion = "Mi nombre completo es: " + nombre_completo
print(presentacion)

#Indexar es acceder a una porcion de una parte de una cadena de texto mediante un indice
#Indexacion: variable[indice]
country = "Peru"
#       =  0123   
print(country)
#P tiene indice 0
#e tiene indice 1
#r tiene indice 2
#u tiene indice 3
print(country[0]) #P
print(country[1]) #e
print(country[2]) #r
print(country[3]) #u

#Indexacion negativa (Python y pocos lenguajes admiten esto)
print("")
print(country[-1]) #u
print(country[-2]) #r
print(country[-3]) #e
print(country[0]) #P

pais = "Republica Dominicana"
#Indexacion: variable[indice]
print("El indice de pais en la posicion 2 es: ", pais[2])
print("El indice de pais en -4 es: ", pais[-4])
#Los espacios tambien cuentan
print("El indice de pais en la posicion 9 es: ", pais[9])

#La funcion Len nos retorna la longitud de nuestra cadena de texto
print(len(country))
print(len(pais))

#slicing/ cortes
#El indice del lado derecho posterior a los dos puntos, es el indice limite del corte el cual no sera agregado
print(country[0:2]) #PE

print(pais[0:9])
print(pais[:9])
print(pais[10:])
print(pais[:-3])

#Formula
print(pais[:9] + pais[9:])

#Toda cadena de texto tiene un indexado