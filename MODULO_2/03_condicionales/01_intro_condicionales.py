"""OPERADORES RELACIONALES"""

x = 11
# == : Operador de comparacion de un valor con otro vlor, que retornara un valor booleano (True or False)
#Para ejecutar una condicion dentro de una sentencia if, el valor de la condicional siempre sera verdadero
if x < 10:
    print("x es menor que 10")
else: #el codigo dentro de la sentencia else, se ejecuta cuando la condicional de if sea falsa
    print("x es mayor que 10")

a = 10 == 10
print(a)

b = 21 != 21 # != Hace una comparacion de valores desiguales
print(b)

c = 20 >= 20
print(c)

d = "Alex"
e = "Alex"

if d != e:
    print("Las variables tienen nombres diferentes")
else:
    print("Las variables tienen nombres iguales")

"""OPERADORES LOGICOS"""
print("\nOPERADORES LOGICOS") #\n creates an extra line before this line
#and
#or
#xor
#not

arg1 = True
arg2 = False

print("Condicional and: ", arg1 and arg2) #False
print("Condicional or: ", arg1 or arg2) #True
print("Condicional xor: ", arg1 ^ arg2) #Usar "^" para xor. #Si los valores son diferentes es True
print("Negacion Arg2': ", not arg2) #Retorna el opuesto del argumento

name = "Alex"

#in, not in
#in: esta dentro de
print('x' in name)
print('a' in name)

#Indexacion
print(name[0]) #A (porque es la primera cadena de texto)