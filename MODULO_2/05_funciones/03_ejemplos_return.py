print("EXAMPLE 1:")
#Colocar el tipo de dato para el parametro de una funcion solo servira de documentacion mas no sera una restriccion para el programa
def calcular_mensaje_calificacion(nota: int): #Se expecifico que nota es int en (nota:int)
    if nota < 0 or nota > 20:
        raise Exception("La nota ingresada es erronea", nota) #Gestion de errores. Usar Exception es amplio. #En este caso agregue el argumento "nota" pero es opcional.
    elif nota <= 5:
        return "Baja nota, a seguir estudiando!"
    elif nota <= 10:
        return "Baja nota, puedes hacerlo mejor!"
    elif nota <= 15:
        return "Nada mal, pero puedes mejorar!"
    else:
        return "Buen trabajo!"

"""OPTION 1: No se controla la excepcion"""
print("\nOPTION 1: No se controla la excepcion")
mensaje_Alex = calcular_mensaje_calificacion(13)
#No se controla la excepcion si: calcular_mensaje_calificacion("13" como str)
print(mensaje_Alex)

"""OPTION 2.1: Controlando las excepciones con'TRY'"""
print("\nOPTION 2.1: Controlando las excepciones con'TRY' y 'EXCEPT'")
try: #Para gestionar excepciones que se levanten en ciertas partes del codigo
    mensaje_Alex = calcular_mensaje_calificacion(-1) #-1 causara error
    print(mensaje_Alex)
except Exception:
    print("Ocurrio un problema en el programa") #Ocurrio un problema en el programa 
    #Aqui hay un error porque la "Exception" de la linea 5 se esta sobrescribiendo con la linea 27
    #Para corregir hacemos lo siguiente

"""OPTION 2.2: Correccion en la excepcion con 'Exception as error'"""
print("\nOPTION 2.2: Correccion en la excepcion con 'Exception as error'")
try: 
    mensaje_Alex = calcular_mensaje_calificacion(-1)
    print(mensaje_Alex)
except Exception as error:
    print(error) #La nota ingresada es erronea (De la linea 5) - Esto es una tupla
    print(f"Nota: {error.args[1]}. {error.args[0]}.") #Esto viene de Linea 5 por indexacion

"""OPTION 3: Agregando 'ELSE' y 'FINALLY'"""
print("\nOPTION 3: Agregando 'ELSE' y 'FINALLY'")
try: 
    mensaje_Alex = calcular_mensaje_calificacion(-1)
except Exception as error:
    print(f"Nota: {error.args[1]}. {error.args[0]}.") #Esto viene de Linea 5 por indexacion
else: #Al usar Else, ejecuto el "print(mensaje_Alex)" despues de "except" porque ya se gestiono. Ver cambio de lugar con ejemplo anterior
    print(mensaje_Alex)
finally:
    print("Se termino el programa")

