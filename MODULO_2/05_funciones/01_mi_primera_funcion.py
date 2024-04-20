def my_function():
    print("Hello World")

a = 20
b = False
#
print("Sum:", a + b)
#
#
my_function()

"""Funciones con parametros"""
#los parametros de la funcion son a y b
def basicsum(a,b): #Tambien se podria espcificar: basicsum(a = int, b = int):
    print("Las suma de los numeros es: ", a + b)

#El paso de valores se le como asignacion de argumentos de la funcion
basicsum(10,2)
basicsum(1,3) # Me ahorro de escribir el print
basicsum(5,20)
basicsum("Alexander"," Patino")
#basicsum("Alexander",10) causa error porque no puede sumar un str con un int

"Example 1:"
def message(number):
    print("The number you entered is:", number)

number = 1234
message(7) #Refers to the function above
print(number) #Prints "1234" due to it is separate from the function "message(number)"

"Example 2:"
print("-"*20) #Esto hace 20 lineas

result= 20 #Variable global
print(result)

def divide(x, y):
    result = x/ y
    print(result) #Variable especifica dentro de una funcion

divide(10,2) #5
print(result) #20 porque no es afectada por la variable "result" dentro de la funcion "divide"

### Una alumna pregunto sobre matrices: Matriz en Python en una lista que almacena otra lista

"""Varios parametros"""

def introduction(first_name, last_name, age, country = "Peru"):
    print(f"""
    My first name is: {first_name}.
    My last name is: {last_name}.
    I'm {age}.
    I'm from {country}.
    """)  #Uso de f-string para texto de varias lineas

#Paso de argumentos por parametro posicional
introduction("Alexander", "Patino", 35)
introduction("Dimelsa", "Robles", 41)
introduction("Maky", "Robles", 1, "Venezuela") #"Venezuela" reemplaza a "Peru" que seria el dato por defecto si es que no se ingresa ningun dato
introduction("Maky", "Robles", 1)

#Paso de argumentos por nombre de parametro (Lo ordena correctamente)
introduction(age = 14, last_name = "Robles", first_name = "Patrick")

#Mas entendible (buenas practicas en el codigo)
introduction(
    age = 1,
    last_name = "Robles",
    first_name = "Tigrillo"
)
