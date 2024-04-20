lista = [1,2,3,4,5]

"""
#Break termina de manera inmediata el buckle donde se encuentre
for element in lista:
    if element > 2:
        break
    print(element)

print("Se termino el buckle")
"""

#continue: continua a la siguiente iteracion del bucle
for element in lista:
    if element == 3:
        continue
    print(element)

print("Se termino el buckle")
