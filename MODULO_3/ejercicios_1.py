

condicional = True
lista_numeros = []

while condicional:
    try:
        texto_entrada = int(input("Ingrese el numero a agregar: "))
        if texto_entrada == "fin":
            condicional = False
        else:
            numero = int(texto_entrada)
            lista_numeros.append(numero)
    except ValueError:
        print("Debe ingresar un dato numerico")