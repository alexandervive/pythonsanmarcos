x = int(input("Ingrese un numero x: "))
y = int(input("Ingrese un numero y: "))

if x > y:
    print("x es mayor a y")
elif x < y:
    print("x es menor a y")
else:
    print("x es igual a y")

#Operadores ternanrio: Alternativa mas profesional o elegante solo para dos opciones

p = int(input("Ingrese un numero: "))
result = "El numero es par" if p %  2 == 0 else "El numero es impar"
print(result)

#El codigo de abajo funciona igual
q = int(input("Ingrese un numero: "))
if q % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")

#Si se ingresa texto en vez de un numero, Python va a dar un error
#Para evitar el error utilizaremos el:
"""
MANEJO DE EXCEPCIONES
"""

