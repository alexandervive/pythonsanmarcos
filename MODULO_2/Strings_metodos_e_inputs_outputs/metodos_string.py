nombre_alumno = "Rodolfo"

#Metodo Capitalize ()
titulo_libro = "lA SOCIEDAD DE LA NIEVE"
titulo_correcto = titulo_libro.capitalize()
print(titulo_correcto)

#Metodo Upper () Transforma los caracteres a mayusc
print("Metodo upper: ",nombre_alumno.upper())

#Metodo Lower () Transforma los caracteres a minus
print("Metodo lower: ",nombre_alumno.lower())

#Metodo Title () El primer caracter sera en mayusc
print("Metodo title: ",titulo_correcto.title())

#Metodo stip () El primer caracter sera en mayusc
mensaje = "     me olvide lo que te iba a decir  "
print("Total de caracteres del mensaje: ",len(mensaje))
nuevo_mensaje = mensaje.strip()
print("Total de caracteres del mensaje tras eliminar espacios en blanco: ",len(nuevo_mensaje))
print(nuevo_mensaje)

#***Adicional: esta funcion tambien acepta un argumento/ parametro
print("abc oaedededd abc".strip("abc"))

# rstrip
# lstrip
mensaje_raro = "abc oasddhdd"
print(len(mensaje_raro))
nuevo_mensaje2 = mensaje_raro

#Metodo isdigit
is_digit = "1234".isdigit()
print("Es un digito", is_digit)

#Metodo isnumeric
print("IV".isnumeric())

#Metodo Replace: Reemplazar texto
lista_de_compras = "Leche, vino, huevo"
print(lista_de_compras.replace("vino","papel"))

#Find: 
print(lista_de_compras.find("vino"))

#rFind: 
lista_de_compras2 = "Arroz, azucar, harina, huevo, papel"
print(lista_de_compras2.rfind("harina"))
print(lista_de_compras2.find("azucar"))

#Count: 
lista_de_compras3 = "arroz, azucar, arroz, huevo, papel"
print(lista_de_compras3.count("arroz"))

#Starswith(): Retorna un valor booleano True si el caracter que se pase como argumento es el caracter o caracteres
print("Hola mundo, que tal les va?".startswith('Hola mundo,'))

#Endswith() ->Retorna un valor booleano, funcionamiento similar a 'Startswith' pero desde el final
print("Hola mundo, que tal les va?".endswith('va?'))

#split() -> Este metodo retorna la lista de caracteres con un elemento de arreglo/ lista
print("Gino,Pedro,Rodrigo,Rodolfo,Jerriot".split(','))