


condicional = True
lista_numeros = []
contador_numeros = 0
suma = 0

while condicional:
    try:
        texto_entrada = int(input("Ingrese el numero a agregar: "))
        if texto_entrada == "Fin":
            condicional = False
        else:
            numero = float(texto_entrada)
            contador_numeros = contador_numeros + 1
            suma = suma + numero
            lista_numeros.append(numero)
    except ValueError:
        print("Debe ingresar un dato numerico")

print(f"""
1. La suma de los numeros: {suma}
2. El total de numeros ingresados: {contador_numeros}
3. El promedio de los numeros es: {suma/ contador_numeros}
""")