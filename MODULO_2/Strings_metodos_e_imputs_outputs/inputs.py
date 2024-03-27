print("Ingresa dos numeros para la sumatoria: ")
numero_1 = input("Ingrese el numero 1: ")
numero_2 = input("Ingrese el numero 2: ")

#cuando se asigna un input y se asigna a una variale, este sera una cadena de texto
a = int(numero_1) #Casteo / Transformar un tipo de dato a otro
b = int(numero_2)
print(type(a))
print(type(b))
print("La suma de los numeros es: ",a + b)