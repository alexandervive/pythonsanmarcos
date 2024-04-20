#Todo paquete ecesita un archivo __init__.py obligatoriamente
#No necesita completarse pero si se incluyen sus los modulos y funciones, estos van a ser ejecutados al momento de importarse.

print("Se ejecuto el __init__ del modulo")
from .modulo_matematica import*
from .modulo_mensajes import*
from .subpaquete.modulo_usuario import * #Esto incluye al subpaquete cuando se llame al paquete principal
#Si uso:
#from .modulo_matematica import division
#importaria solo 'division' pero causaria errores en los archivos donde se ejecute el paquete si es que llaman a esa funcion

#from .modulo_matematica import division, potencia
#Importa division y potencia
