

my_list = ["Alexander", "Elizabeth", 16.8, 4, True, False]
print(my_list, type(my_list), id(my_list)) #['Alexander', 'Elizabeth', 16.8, 4, True, False] <class 'list'> 2328081783040

# Indexacion
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[4])
print(my_list[5])
print(my_list[-1])
print(my_list[-5])

#Mutable
# Lists are mutables can be modified
my_list [2] = "Emilia" # Cambio valor
my_list [-1] = my_list [0] # Igualar valor de variable (se reemplaza el valor de la variable)
print(my_list, id(my_list)) # ['Alexander', 'Elizabeth', 'Emilia', 4, True, False] 2328081783040
#El ID se matiene

# Inmmutable 
a = 10
print(a, id (a))
a = a + 1
print(a, id (a))

# 1. Determinar tamaño de lista
print(f"El tamaño de mi lista es {len(my_list)}")

# 2. Asignacion de listas -> Asignacion por referencia (asigna el valor y la referencia de la direccion en la memoria)
print("="*50)

list_1 = [1, 2.0, "3"]
list_2 = list_1

print(list_1, id(list_1))
print(list_2, id(list_2))

# 3. Si modifico en una variable de la lista 1
list_1 [0] = "Hola Mundo"

print("="*50)

print(list_1, id(list_1))
print(list_2, id(list_2))
#Cuando se modifica la lista 1, se modifica la lista 2 (Ver el ID no cambio)

#Para evitar este error de asignacion por referencia:

# 4. Podemos utilizar 'Slice', por ejemplo imprime solo el apellido
name = "Alexander Patino"
print(name[10:16])

#Aplicar slice en la lista

list_3 = list_1 [:] # Con esto la lista 3 cambiara de ID
print("="*50)
print(list_1, id(list_1)) #ID de linea 35
print(list_3, id(list_3)) #Diferente ID de linea 

# 5. Modificar lista 1 (pero su ID no se cambiara):

list_1[1] = "que tal"
print("="*50)
print(list_1, id(list_1)) #ID de linea 35
print(list_3, id(list_3)) #Diferente ID de linea 

# 6. Lista dentro de una lista

list_x = [1, 2.0, "3", ["Emilia", "Elizabeth", "Flor"]]
print(list_x)
print(list_x[3])
print(list_x[3][1])

# Nueva lista
# Crear lista nueva con valores de otra lista

list_y = [1, 2, 3, 4, 5]
#list_z = [list_y[-1], list_y[-2]] #[5, 4]
list_z = list_y [3:]
print(list_z)