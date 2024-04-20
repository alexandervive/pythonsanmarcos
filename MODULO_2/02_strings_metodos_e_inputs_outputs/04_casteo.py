#Casteo: Transformar un tipo de dato a otro tipo de dato
#En Python, la funcion de casteo es generalmente con el mismo nombre de la clase a la que hace referencia el tipo de dato

#Agregar comentario con """ para que no se ejecute

a = input("Ingrese un numero entero: ")
print(a)
numero_int = int(a) #Se debe hacer esto para pasar de 'str' a 'int' (Esto es castear)
suma = numero_int + 20
print(suma)

#Otra alternativa es:
a = int(input("Ingrese un numero entero: ")) #Encapsular la funcion 'input' dentro de 'int'
suma = a + 20
print(suma)
#Cerrar comentario con """ para que no se ejecute


#Casteo de 'int' a 'bool'
a = 1
print(type(a)) #<class 'int'>

veracidad = bool(a) #casteo de 'int' a 'bool'
print(type(veracidad)) #<class 'bool'>

#Casteo de 'int' a 'str'
numero = 100
texto_numero = str(numero)
print(texto_numero, type(texto_numero))