name = "Alex"
last_name = "Patino"
full_name = name + " " + last_name + " " + "Mamani" # Estoy usando + " " + para agregar espacios
print(full_name)

#Alternative using f
extra = f"{name} {last_name} Mamani"
print(extra)
#or
print(f"{name} {last_name} Mamani")

#a = "10" + 10" 
#print(a) va a generar un error por sumar un str con un int

"""
ERRORES:
"""
#1. ZeroDivisionError #Al dividir entre 0
#print(10/0) #ZeroDivisionError: division by zero

#2. NameError #Usar una variable no definida
#print(book + carpet) #NameError: name 'book' is not defined. Did you mean: 'bool'?

#3. TypeError #Usar de operaciones entre tipos de datos
#print(14.2 + "10.2") #TypeError: unsupported operand type(s) for +: 'float' and 'str'

#4. IndexError #Indice
#student_name = "Raphael"
#print(student_name[7]) #IndexError: string index out of range (String index max is 6)

#5. KeyError #Diccionarios
