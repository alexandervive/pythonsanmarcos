#Retornar valor -> Palabra reservada "RETURN"

def mult(a, b): #Consultar con Gemini si hay otra alternativa
    return a * b

result = mult(10, 20)
print(result, type(result)) 

"""Exercise 2"""

def counting():
    print("Three")
    print("Two")
    print("One")
    return
    print("Happy New Year")

counting() #No produce "print("Happy New Year")" porque al llegar a Return el programa termina

"""Exercise 3""" #Consultar con Gemini

def counting2(happy):
    print("Three")
    print("Two")
    print("One")
    if happy == False: return
    print("Happy New Year")

counting2(True)
#True es igual a falso, falso, entonce va a ejecutar "Happy New Year"
#Si selecciono "False", como False es igual a False, no retorno el mensaje

"""Exercise 3"""

#Determinar si un numero es par

def pair_number(number):
    if number % 2 == 0:
        return True

result2 = pair_number(111)
print(result2) #Prints None: No tener valor

#Para no retornar "None" se podria hacer:

def pair_number2 (number2):
    if number2 % 2 == 0:
        return True
    else:
        return False

result3 = pair_number2(111)
print(result3)