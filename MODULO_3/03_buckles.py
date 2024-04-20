"""
#while cuando algo se repita n veces hasta que una condicional deje de cumplirse
    #usadas mayormente para validar condicionales y que una porcion de codigo se ejecute muchas veceshasta que se rompa la condicional

#for es mas usado para recorrer estructuras de datos como listas
    #se utiliza cuando sabemos la cantidad determinada de veces que se va a ejecutar una sentencia.


#Siempre que While sea True, se va a cumplir al infinito

#Codigo infinito
#while True:
    #print("Hola Mundo") 

# Hay que tener cuidado, hay que agregar una condicional para que se detenga

number = 1

#Codigo que termina y no es infinito porque la condicional esta siendo afectada por una variable que cambia su valor constantemente
while number <= 5:
    print("Hello, World!")
    number = number + 1 # Cada vez que se ejecute, aumenta su valor en 1
    
    # Inicia el Buckle, "number es 1" y debido a que no se cumple "number <= 5", se agrega +1 y se reinicia
    # El nuevo valor de "number" es ahora 2 y debido a que no se cumple "number <= 5", se agrega +1 y se reinicia 
    # El nuevo valor de "number" es ahora 3 y debido a que no se cumple "number <= 5", se agrega +1 y se reinicia 
    # El nuevo valor de "number" es ahora 4 y debido a que no se cumple "number <= 5", se agrega +1 y se reinicia 
    # El nuevo valor de "number" es ahora 5 y debido a que SI se cumple "number <= 5", se detiene.
   
    # En cada instancia se ha impreso "Hello, World!" hasta que termino el buckle

    # "numero += 1" es igual a "number = number + 1"

#Programa con buckle que pide ingresar 2 enteros que se suman y si se ingresa un str, vuelve a pedir los 2 enteros hasta que se cumpla:

conditional = True
while conditional:
    try:
        number1 = int(input("Enter number 1: "))
        number2 = int(input("Enter number 2: "))
        conditional = False # Si no se cambia la condicional, el programa no se detendra incluso si ya se ha cumplido la condicional "ingresar los 2 enteros"
        print(number1 + number2)
    except Exception:
        print("There is an error.")
"""

#2. For - es usado mayormente para recorrer listas u otras estructuras de datos

#For usado en lista
list_1 = [1, 2, 3, "Alexander", "Elizabeth", "Alexander","Alexander"]
for element in list_1:
    print(element) #Se imprime todos los elementos

list_alexander = []
for element in list_1: 
    if element == "Alexander": #si el elemento de la list_1 es igual a "Alexander"
        list_alexander.append(element) #agregar "Alexander" en "list_alexander" ya que la lista esta vacia
print(list_alexander, len(list_alexander)) # como hay 3 "Alexanders, la lista tendra 3 objetos.
#['Alexander', 'Alexander', 'Alexander'] 3
#Para quitar un "Alexander" se deberia acceder al indice y eliminar el mismo valor del arreglo
#Investigar el metodo ENUMERATE (Investigar)

#For usado en rangos
for num in range(5):
    print(num) #Se imprime del 0 al 4

for num in range(3,5):
    print(num) #Se imprime 3 y 4

print("")
for num in range(3, 10, 2):
    print(num) #Se imprime de dos en dos: 3, 5, 7, 9

print("")
for num in range(10, 1, -1):
    print(num) #Se imprime de 10 a 1 en negativo)
