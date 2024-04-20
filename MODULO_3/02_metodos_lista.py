my_list = [1, 2 , 3, "Alexander", True, "Elizabeth"]

# append() - Agregar elemento al final de la lista
my_list.append("Ronald")
print(f"append: {my_list}")

my_list.append("Yvan")
print(f"append: {my_list}")

# extend() - Agrega una nueva lista a la lista original. Lo hace agregandola al final de la lista.
new_list = [15, 14, 20, 18]
my_list.extend(new_list)
print(f"extend: {my_list}")

# insert(i, a) - inserta un elemento nuevo en una posicion especifica
# "i" es un indice y "a" es un elemento nuevo
my_list.insert(3,"Joel")
print(f"insert: {my_list}") #Mueve el antiguo indice 3 a la derecha

# remove () - Elimina un elemento de la lista, pasando como argumento el elemento
my_list.remove("Yvan")
print(f"remove: {my_list}") #Quito "Yvan" de la lista

# pop() - Remueve el ultimo elemento de la lista
my_list.pop()
print(f"pop: {my_list}") # Se removio "18"

#Puedo duplicar la line para eliminar 2 valores
my_list.pop()
my_list.pop()
print(f"pop: {my_list}") # Se removio "20" y "14"

# reverse() - Revierte los indices de la lista
my_list.reverse()
print(f"reverse: {my_list}") # Se removio "20" y "14"

# sort() - Ordena de menor a mayor los elementos de la lista
#my_list.sort() #Error por no poder hacer la comparacon entre str y integers
#print(f"sort: {my_list}") 

int_list = [10, 2, 2000, 1, 3.0]
int_list.sort()
print(f"sort: {int_list}")

    # ordenar la lista de mayor a menor

int_list.sort(reverse = True)
print(f"sort de mayor a menor: {int_list}")

# clear() - eliminar todos los elementos de la lista y dejar una lista vacia.
int_list.clear()
print(f"clear: {int_list}")

# index() - Retorna indice de un elemento pasado como parametro del metodo
#Si hay mas de un elemnto igual, retornara el primer indice del elemento encontrado de izquierda a derecha
print(my_list.index('Alexander'))
print(f"Alexander esta en el indice: {my_list.index('Alexander')}")

# count() - retorna la cantidad de veces que se encontro un elemento en la lista
print(f"Numero de veces que aparece: {my_list.count('Alexander')}")

# copy() - retorna una copia de la lista, pero pasada por valor, no por referencia

new_list = my_list.copy()
print(f"My List: {my_list}, id: {id(my_list)}") #ID son dif
print(f"My New List: {new_list}, id: {id(new_list)}") #ID son dif

print(id(my_list) is id(new_list)) #False

# Operadores logicos
print("Alexander" in new_list) #True
print("YVan" not in new_list) #True

# len() - Use it with Print to show the number of items in the list. 
print(len(my_list)) #9