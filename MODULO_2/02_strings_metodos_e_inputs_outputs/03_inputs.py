print("Ingresa dos numeros para la sumatoria: ")
numero_1 = input("Ingrese el numero 1: ") #los input siempre reconocen a los valores como 'str"
numero_2 = input("Ingrese el numero 2: ") #Se debe de castear de 'str' a 'int'

#cuando se asigna un input y se asigna a una variale, este sera una cadena de texto
a = int(numero_1) #Casteo / Transformar un tipo de dato a otro
b = int(numero_2)
print(type(a))
print(type(b))
print("La suma de los numeros es: ",a + b)

#Agregando f-sting para hacer mas elaborada la linea de codigo
print(f"El resultado de la resta de {a} con el valor de {b} es igual a {a - b}")

#Utilizando .format y sin f-string
print("El resultado de la resta de {0} con el valor de {1} es igual a {2}".format(a, b, a -b))