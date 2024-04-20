nombre_alumno = "Rodolfo"
titulo_libro = "lA SOCIEDAD DE LA NIEVE"

#1. Metodo Capitalize ()
titulo_correcto = titulo_libro.capitalize()
print("1. Metodo capitalize: ",titulo_correcto)

#2. Metodo Upper () -> Transforma los caracteres a mayusc
print("2. Metodo upper: ",nombre_alumno.upper())

#3. Metodo Lower () -> Transforma los caracteres a minusc
print("3. Metodo lower: ",nombre_alumno.lower())

#4. Metodo Title () -> El primer caracter sera en mayusc
print("4. Metodo title: ",titulo_correcto.title())

#5. Metodo strip () -> Nos ayuda a eliminar espacios del inicio y del final
print("")
print("STRIP")
mensaje = "     me olvide lo que te iba a decir    "
print("5.1 Mensaje:", mensaje)
print("5.2 Total de caracteres del mensaje (incluyendo espacios): ",len(mensaje))
nuevo_mensaje = mensaje.strip()
print("5.3 Total de caracteres del mensaje tras eliminar espacios en blanco: ",len(nuevo_mensaje))
print("5.4 Nuevo mensaje: ", nuevo_mensaje)

#6. Strip con argumento: esta funcion tambien acepta un argumento/ parametro
print("")
print("STRIP CON ARGUMENTO: Eliminar 'abc' de 'abc oaedededd abc'")
print("6.1 Strip con argumento 'abc':")
print("abc oaedededd abc".strip("abc"))
#or Using f-string and brackets
print(f"6.1 Strip con argumento 'abc': {'abc oaedededd abc'.strip('abc')} - (Alternativa en una sola linea)")

#7. Tambien se podria crear una variable con un valor especifico, por ejemplo:
print("")
print("STRIP CON ARGUMENTO: Eliminar contenido de una variable")
subtitle = "Rex Tyrano Rex"
print("7.1 Remove 'Rex' from:", subtitle)
print("7.2 Character Count: ",len(subtitle))
new_sub = subtitle.strip("Rex")
print("7.3 Strip With Argument 'Rex':", new_sub)
new_sub_final = new_sub.strip()
print("7.4 Character Count After Removing 'Rex': ", len(new_sub_final))

#8. Alternative using REPLACE and STRIP:
print("")
print("STRIP CON ARGUMENTO: Eliminar contenido de una variable con REPLACE y STRIP")
title = "Et Viator Et"
print("8.1 Remove 'Et' from:", title)
print("8.2 Character Count: ",len(title))
new_title = title.replace("Et","")
print("8.3 Strip With Argument 'Et':", new_title)
new_title_final = new_title.strip()
print("8.3 Character Count After Removing 'Et':", len(new_title_final))

#9.1 rstrip -> Right strip, derecha
#9.2 lstrip -> Left strip, izquieda
print("")
print("RSTRIP Y LSTRIP")
mensaje_raro = "abc oasddhdd   " #3 spaces on the right
print("9.1 Variable (with 3 spaces on the right): ", mensaje_raro)
print("9.2 Character Count: ", len(mensaje_raro))
signal = mensaje_raro.rstrip()
print("9.3 Remove spaces from the right: ", signal)
print("9.4 New Character Count: ", len(signal))

#10. rstrip and lstrip with argument
print("")
print("RSTRIP Y LSTRIP CON ARGUMENTO: Remove 'abc' from 'abc eieidjei abc'")
print("10.1 Remove 'abc' from the right: ","abc eieidjei abc".rstrip("abc")) #Es importante las comillas en ("abc")
print("10.2 Remove 'abc' from the left: ","abc eieidjei abc".lstrip("abc")) #Es importante las comillas en ("abc")

#11. Metodo isdigit: Retorna "True" si los caracteres son del 0 al 9
print("")
print("IS DIGIT")
is_digit = "1234".isdigit()
print("11.1 '1234' es un digito?: ", is_digit)
print("11.2 '¹²³' es un digito?: ", "¹²³".isdigit())
print("11.3 '¹ ² ³' es un digito?: ", "¹ ² ³".isdigit())
print("11.4 '¹,²,³' es un digito?: ", "¹,²,³".isdigit())
#Numeros romanos da como resultado "False"
print("11.5 'Ⅳ' es un digito?: ", "Ⅳ".isdigit())

#12. Metodo isnumeric
print("")
print("IS NUMERIC")
print("12.1 'Ⅳ' es un numero?: ", "Ⅳ".isnumeric()) #Unicode character "Ⅳ" recognized as Roman Number
print("12.2 'IV' es un numero?: ", "IV".isnumeric()) #Text "IV" not recognized as Roman Number

#13. Metodo Replace: Reemplazar texto "a" por texto "b"
print("")
print("REPLACE")
lista_de_compras = "leche, vino, huevo"
print("13.1 Lista de compras: ", lista_de_compras)
print("13.2 Reemplazar 'vino' por 'papel': ", lista_de_compras.replace("vino","papel"))
#El primer argumento es para encontrar el string y el segundo argumento es el de reemplazo

#14.1 Metodo Find: Encuentra el indice de inicio de cierta cadena de texto
#La busqueda es de izquierda a derecha
print("")
print("FIND Y RFIND") 
print("14.1 Ubica 'leche' con .find: ", lista_de_compras.find("leche"))

#14.2 rFind: Busqueda de derecha a izquierda
lista_de_compras2 = "arroz, azucar, harina, huevo, papel, arroz"
print("14.2 Ubica 'arroz' con .rfind: ",lista_de_compras2.rfind("arroz"))
print("14.3 Ubica 'arroz' con .find: ",lista_de_compras2.find("arroz"))

#15. Count: Cuenta la cantidad de veces que aparece un texto en el texto original
print("")
print("COUNT")
lista_de_compras3 = "arroz, azucar, huevo, papel, azucar"
print("15. Numero de veces aparece 'azucar': ",lista_de_compras3.count("azucar"))

print("")
print("STARTS WITH AND ENDSWITH")
#16.1 Starswith(): Retorna un valor booleano True si el caracter que se pase como argumento es el caracter o caracteres con el cual inicia el texto original
print("Hola mundo, que tal les va?".startswith('Hola mundo,'))

#16.2 Endswith() ->Retorna un valor booleano, funcionamiento similar a 'Startswith' pero desde el final
print("Hola mundo, que tal les va?".endswith('va?'))

print("")
print("SPLIT")
#17. Split() -> Este metodo retorna la lista de caracteres con un elemento de arreglo/ lista
print("Gino,Pedro,Rodrigo,Rodolfo,Jerriot".split(',')) #especificar el caracter para separar
#Se almacena un arreglo: ['Gino', 'Pedro', 'Rodrigo', 'Rodolfo', 'Jerriot']