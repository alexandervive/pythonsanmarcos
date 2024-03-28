a = 10
b = 5

#Suma: +
print("Suma:",a+b)

#Resta: +
print("Resta:",a-b)

#Multiplicacion: *
print("Multiplicacion:",a*b)

#Division: /
print("Division:",a/b)

#Divisiones que retornan un valor exacto: //
print("Division exacta:",a//b)
print("Division exacta:",10//3)

#Resto o Modulo: %
print("El resto:",31%10)
print("El resto:",30%10)

#Potencia: **
print("Potencia:",2**3)
print("El resto:",11**2)

#Orden de operciones de izquierda a derecha
ecuacion = (40-5*4)*2-4**2
# (40-20)* 2-4**2
# 20*2-16
# 40-16
# 24
print(ecuacion)

#Para la poteniacion no iremos de derecha a izquierda
#Se debe operar de derecha a izquierda
potencias = 2 ** 2 ** 3
print(potencias)