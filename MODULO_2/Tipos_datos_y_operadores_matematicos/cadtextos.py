my_name =  "Alexander Patino"
print (type(my_name), my_name)

pelicula = "Avengers Infinity Wars"
print(type(pelicula))
print(pelicula)

monto_ahorrado = "10,000"
print(monto_ahorrado)
"""No se puede ejecutar debido a ser un str + int:

resultado = monto_ahorrado + 10
print(resultado)"""

#Concatenacion
nombre = "Alexander"
apellidos = "Patino"
nombre_completo = nombre + " " + apellidos
print(nombre_completo)

#Usar comillas dentro de una cadena de textos
mensaje = "Pedro dice: \"El jueves no hay clases por Semana Santa\" "
respuesta_1 = "Jorge responde: 'Si aprovechare para repasar las clases' "
respuesta_2 = 'Jorge responde: "Que mala suerte, justo queria preguntarle algo al profe." '
print(mensaje)
print(respuesta_1)
print(respuesta_2)

#Salto de linea se realiza con \n Alt 92
discurso1 = "linea 1 del discurso\nlinea 2 del discurso\nlinea 3 del discurso"
print(discurso1)

#Si hay un espacio despues de \n como "\n linea2", se creara un espacio antes de "linea 2"
discurso2 = "linea 1 del discurso\n linea 2 del discurso\nlinea 3 del discurso"
print(discurso2)