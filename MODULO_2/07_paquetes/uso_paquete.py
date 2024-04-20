"""
#IMPORTAR PAQUETES

#Necesita un archivo __init__.py obligatoriamente

import primer_paquete.modulo_matematica

print(primer_paquete.modulo_matematica.potencia(2,3)) #8

#Para abreviar el nombre del paquete podria tuilizar:


print("\n1. IMPORTAR PAQUETE CON UN NOMBRE ASIGNADO")
import primer_paquete.modulo_matematica as mod_math
#El paquete va a ser llamado con un nombre asignado
#Para ello agrego "as" y el nombre "mod_math" en la linea import

print(mod_math.potencia(2,3)) #8


print("\n2. IMPORTAR MODULO MENSAJES")
import primer_paquete.modulo_mensajes as mod_str

mod_str.saludo() #Hi, my name is Patrick Robles
#mod_str.saludo() no utiliza print porque el modulo no tiene la funcion "return"
#Si se utilizara print, daria como output "None"


print("\n3. IMPORTAR PAQUETE CON FUNCION ESPECIFICA DE MODULO MATEMATICA")
from primer_paquete.modulo_matematica import potencia

print(potencia(2,3))
#Si se utilizara "print(division(2,3))", daria Error porque solo se importo "potencia"


print("\n4. IMPORTAR PAQUETE CON TODAS LAS FUNCIONES DEL MODULO MATEMATICA")
from primer_paquete.modulo_matematica import*

print(potencia(2,3))
print(division(6,2))

print("\n5. IMPORTAR PAQUETE MODIFICANDO ARCHIVO __INIT__.PY") #Ver archivo __init__.py
import primer_paquete

print(primer_paquete.potencia(2,3))
print(primer_paquete.division(10,2))
primer_paquete.saludo()

"""
print("\n6. IMPORTAR PAQUETE MODIFICANDO ARCHIVO __INIT__.PY CON NOMBRE ASIGNADO")
import primer_paquete as paq
import primer_paquete.subpaquete.modulo_usuario as mod_user

print(paq.potencia(2,3))
print(paq.division(10,2))
paq.saludo()

print(mod_user.mostrar_correo()) #De ejemplo 7. Crear subpaquete
print(paq.mostrar_correo()) #De ejemplo 8. Incluid subpaquete al llamar al paquete principal

print("\n7. CREAR UN SUBPAQUETE")
#A nivel de "primer paquete", crear un folder "subpaquete"
#Dentro del folder "subpaquete", crear un archivo "__init__.py" y un archivo "modulo_usuario.py"
#Crear funciones dentro del archivo "modulo_usuario.py"
#Importar subpaquete de forma similar

#import primer_paquete.subpaquete.modulo_usuario as mod_user

#print(mod_user.mostrar_correo())

print("\n8. INCLUIR SUBPAQUETE AL LLAMAR AL PAQUETE PRINCIPAL")
#Puedo agregar el subpaquete al __init__.py del primer paquete para que al importar primer_paquete, se importe tambien el subpaquete
#Se agregaria entonces: from .subpaquete.modulo_usuario import *
#print(paq.mostrar_correo()) #Esta linea de codigo deberia llamar al correo

#No es comun incluir subpaquetes, por lo general se utilizan mas paquetes con varios modulos