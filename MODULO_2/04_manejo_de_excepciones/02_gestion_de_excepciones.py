"""EXERCISE 1"""
#Exercise 1: We MUST change variables x and y
print("EXERCISE 1")
x = 10
y = 0

try:
    result = x / y
except ZeroDivisionError as error:
    #print("Sorry. You can't divide by 0")
    print("Sorry, we found the following error: \n", error)

"""EXERCISE 2"""
#Exercise 2: Usando palabra reservada "Exception"
print("\nEXERCISE 2")
try:
    number1 = int(input("Enter Number 1: "))
    number2 = int(input("Enter Number 2: "))
    result2 = number1 + number2
    division = number1 / number2
    print(result2)
    print(division)
except Exception: #se puede poner "Exception" que cubre todos los errores, o se puede poner varios errores "TypeError,ValueError"
    print('"Sorry, there is an error".')

"""EXERCISE 3"""
print("\nEXERCISE 3")
#Exercise 3
try:
    number3 = int(input("Enter Number 3: "))
    number4 = int(input("Enter Number 4: "))
    result3 = number3 + number4
    division2 = number3 / number4
    print(result3)
    print(division2)
except ZeroDivisionError:  #Excepciones individuales, una debajo de otra
    print('"Sorry, divisions by 0 are not allowed".')
except ValueError:
    print('"You have not entered a valid number".')
except KeyboardInterrupt: #Cuando se usa "Control + Key" (Hay otro motivo?)
    print('\n"The program was stopped".')

"""EXERCISE 4"""
print("\nEXERCISE 4")
#Exercise 4: Crear nuestras propias excepciones con #raise
try:
    p = (int(input("Enter a value for number'p': ")))
    q = (int(input("Enter a value for number'q': ")))
    if q == 0:
        raise ZeroDivisionError("p can't take 0 value", p, q)
except ZeroDivisionError as error:
    print(error) #Primero imprime el error
    print(error.args[0]) #Los datos vienen de la linea de Raise #Luego imprime "p can't take 0 value"
    print(error.args[1]) #Luego imprime "p" de la linea raise
    print(error.args[2]) #Luego imprime "q" de la linea raise
else:
    print(f"The result is {p/q}")

"""EXERCISE 5"""
print("\nEXERCISE 5")
#Exercise 4: Nuevas palabras reservadas "Except" y "Finally"
try:
    a = (int(input("Enter a value for number'a': ")))
    b = (int(input("Enter a value for number'b': ")))
    result4 = a / b
except Exception:
    print("There is an error")
else:
    print("The result of the divion is: ", result4)
finally: #Con else deberia terminar el programa, pero se le agrega Finally para ingresar un mensaje adicional
    print("Program has been executed")

#Si se desea que se repita la lina de codigo, se utiliza los "BUCKLES" con iteraciones con "For" y "While"
#Control de flujos con Buckles