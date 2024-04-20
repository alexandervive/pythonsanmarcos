#IMPORTAR MODULOS

#import math #es un modulo

#Para utilizar funciones en otros archivos podemos utilizar los modulos

#Funciones, variables, clases

#The module will be another .py file with defined functions and variables.
#The name of the file to import as a module may not start with digits.

#METODO 1
print("METODO 1: Importar todas las funciones como 'Import' modulo_1")
import modulo_1
result = modulo_1.suma(10,90)
print(result)
result_2 = modulo_1.multi(3,3)
print(result_2)
#No se puede imprimir la variable email como: print(email) porque va a dar un NameError
"""
#METODO 2
print("\nMETODO 2: Importar funcion especifica como 'from' modulo_1 'Import' multi")
#Si quiero llamar a una sola funcion del modulo, utilizo "from" (modulo) "import"
from modulo_1 import multi
result_3 = multi(3,3) #Si se utiliza otra funcion como "suma" va a dar error porque solo se llamo a la funcion "mullti"
print(result_3)
#No se puede imprimir la variable email como: print(email) porque va a dar un NameError

#METODO 3
print("\nMETODO 3: Importar todas las funciones del modulo como 'from' modulo_1 'Import'*")
from modulo_1 import*
result_4 = multi(3,3) 
print(result_4)
result_5 = suma(3,5) 
print(result_5)
print(email)


#METODO 4
print("\nMETODO 4: Importar todas las funciones del modulo como un valor especifico como 'import' modulo_1 'as' 'm'")
#Alternativa al metodo 1
import modulo_1 as m
result_6 = m.suma(3,3) 
print(result_6)
result_7 = m.multi(3,5) 
print(result_7)
print(m.email)
"""
#La carpeta __pycache__ se creo cuando llamamos a un modulo
#Alamcena un codigo .pyc (Python cache) que incluye las veces que se llamo