"""
#Recordar que este es un Programa con buckle
#El programa pide ingresar 2 enteros que se suman y si se ingresa un str, vuelve a pedir los 2 enteros hasta que se cumpla:

#Crear variable con nombre "condicional"
conditional = True

def my_program():

    while conditional:
        try:
            number1 = int(input("Enter number 1: "))
            number2 = int(input("Enter number 2: "))
            conditional = False # Si no se cambia la condicional, el programa no se detendra incluso si ya se ha cumplido la condicional "ingresar los 2 enteros"
            print(number1 + number2)
        except Exception:
            print("There is an error.")
"""
#Programa

def my_program():
  while True:
    try:
      number1 = int(input("Enter number 1: "))
      number2 = int(input("Enter number 2: "))
      print(number1 + number2)
      break  # Exit loop after successful execution
    except Exception:
      print("There is an error. Please enter valid numbers.")

my_program()  # Call the function first

while True:
  End_msg = str(input("Would you like to start again? Answer YES or NO: "))
  List_S = ["Si", "SI", "S", "sI", "s", "Y", "yes", "Yes", "yeS", "yEs", "YES", "YEs", "yES","YeS","y","1"]
  List_N = ["No", "NO", "N", "nO", "n","0"]

  if End_msg in List_S:
    my_program()
  elif End_msg in List_N:
    print("Thanks for using NEMCO")
    break  # Exit outer loop when user chooses "NO"
  else:
    print("Invalid input. Please answer YES or NO.")

