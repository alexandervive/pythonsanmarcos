#Genera el ID
def gen_id(id_actual):
    while True:
        id_trab = f"{id_actual:04d}"
        if id_trab not in trabajadores:
            return id_trab  # ID unico
        id_actual += 1  # Incrementa el numero de ID si ya esta en uso

"""
===============================================
CREAR TRABAJADOR// AGREGAR TRABAJADORES
===============================================
"""
def crear_trabajador():
    """Pide informacion del trabajador para almacenar en un diccionario."""
    datos = {}
    global id_actual

    datos["ID"] = gen_id(id_actual)
    id_actual += 1  # Actualiza la variable global despues de generar el ID
    datos["apellido"] = input("Creando un nuevo usuario:\n- Apellido: ")
    datos["nombre"] = input("- Nombre: ")
    datos["id_pais"] = input("- DNI: ")
    datos["telefono"] = input("- Teléfono: ")
    datos["tiempo_trab_meses"] = input("- Tiempo trabajando (meses): ")

    while True:
        datos["cargo"] = input("- Cargo (Limpieza, Mesero, Cajero, Vigilante, Gerente): ").upper()
        valid_cargos = ["LIMPIEZA", "MESERO", "CAJERO", "VIGILANTE", "GERENTE"]
        if datos["cargo"] in valid_cargos:
            break
        else:
            print("Posición inválida. Elija entre Limpieza, Mesero, Cajero, Vigilante o Gerente.")

    datos["sueldo"] = sueldo_cargo.get(datos["cargo"])
    return datos

def agregar_trabajadores(datos={}):
    """Pide continuamente a agregar trabajadores hasta que el usuario decide detenerse."""
    while True:
        nuevo_trab = crear_trabajador()
        trabajadores[nuevo_trab["ID"]] = nuevo_trab
        print(f"Trabajador con ID '{nuevo_trab['ID']}' agregado exitosamente.")

        agregar_trab = input("> Quiere ingresar un nuevo empleado al registro? (Si/ No): ").lower()

        valid_inputs = {"si", "no"}  # Respuestas validas
        while agregar_trab not in valid_inputs:  # Loop hasta que se cumpla la condicion
            print("Entrada inválida. Las opciones válidas son 'si' o 'no'.")
            agregar_trab = input("> Quiere ingresar un nuevo empleado al registro? (Si/ No): ").lower()

        if agregar_trab == "no":
            break

"""
===============================================
MAIN MENU
===============================================
"""
def menu():
    terminar = False
    while not terminar:
        try:
            opcion = int(input("""
====================== Gestion de Empleados ========================
|| 1. Visualizar informacion de un empleado.                      ||
|| 2. Mostrar empleado cuyo tiempo en la empresa sea el menor     ||
|| 3. Actualizar salario de un empleado                           ||
|| 4. Terminar programa                                           ||
====================================================================
> Elija la opcion que desee realizar (1/2/3/4): 
"""))
            if opcion < 1 or opcion > 4:
                raise Exception ("> Intente nuevamente.")
            elif opcion != 4:
                accion(opcion)
            else:
                terminar = True
        except ValueError:
            print("Por favor ingrese un numero de opcion.")
        except Exception as error:
            print(error)

def accion(opcion):
    if opcion == 1:
        m1_visualizar_informacion_empleado()
    elif opcion == 2:
        m2_mostrar_empleado_minimo_tiempo()
    elif opcion == 3:
        m3_actualizar_salario_empleado()

"""
===============================================
OPCION 1
===============================================
"""

def m1_visualizar_informacion_empleado():
    """Pide ingresar el ID de un trabajador e imprime la informacion de ese trabajador."""
    if not trabajadores:
        print("\nNo se han agregado trabajadores.")
        return  # Sale de la funcion si no hay trabajadores

    trabajador_id = input("""
\n>>> ========== Visualizar Información ==========
>>> Ingrese el Id del empleado (ID desde 0001 - 9999): """)

    if trabajador_id in trabajadores:
        datos_trab = trabajadores[trabajador_id]
        print(f"\n>>> ===== Información del Trabajador con ID: {trabajador_id} =====")
        print(">>> Apellido:", datos_trab["apellido"])
        print(">>> Nombre:", datos_trab["nombre"])
        print(">>> DNI:", datos_trab["id_pais"])
        print(">>> Teléfono:", datos_trab["telefono"])
        print(">>> Tiempo trabajando (meses):", datos_trab["tiempo_trab_meses"])
        print(">>> Cargo:", datos_trab["cargo"])
        print(">>> Sueldo:", datos_trab["sueldo"])
    else:
        print(f"\n>>> Lo sentimos, no se encontró un empleado con ese Id: {trabajador_id}")


"""
===============================================
OPCION 2
===============================================
"""
def m2_mostrar_empleado_minimo_tiempo():
    """Muestra la informacion del trabajador que ha trabajado menos tiempo."""
    if not trabajadores:
        print("\n>>> No se han agregado trabajadores.")
        return  # Sale de la funcion si no existen trabajadores

    # Encuentra el trabajador con menor tiempo con lista de compresion y min
    tiempos_trabajo = [int(trabajador["tiempo_trab_meses"]) for trabajador in trabajadores.values()]
    tiempo_trabajo_minimo = min(tiempos_trabajo)

    # Filtra a los trabajadores con el menor tiempo (usando lista por comprension)
    trabajadores_tiempo_minimo = [id_trabajador for id_trabajador, datos_trabajador in trabajadores.items()
                                if int(datos_trabajador["tiempo_trab_meses"]) == tiempo_trabajo_minimo]

    if trabajadores_tiempo_minimo:
        print(f">>> ========== Empleado con menor tiempo en la empresa == ({tiempo_trabajo_minimo} meses)====")
        for id_trabajador in trabajadores_tiempo_minimo:
            datos_trabajador = trabajadores[id_trabajador]
            print(f"\n>>> ID: {id_trabajador}")
            print(">>> Apellido:", datos_trabajador["apellido"])
            print(">>> Nombre:", datos_trabajador["nombre"])
            print(">>> Tiempo trabajando (meses):", datos_trabajador["tiempo_trab_meses"])
            print("-" * 20)  # Separador entre trabajadores
    else:
        print(f"\n>>> Todos los trabajadores tienen el mismo tiempo de trabajo (0 meses).")


"""
===============================================
OPCION 3
===============================================
"""
def m3_actualizar_salario_empleado():
    """Updates the salary of a worker based on their ID and a provided raise amount."""
    if not trabajadores:
        print("\n>>> No se han agregado trabajadores.")
        return  # Sale de la funcion si no existen trabajadores

    trabajador_id = input("""\n>>> ========== Actualizar salario de un empleado ==========\n>>> Ingrese el ID del trabajador (ID desde 0001 - 9999): """)

    if trabajador_id in trabajadores:
        # Pide los datos de los trabajadores
        trabajador_data = trabajadores[trabajador_id]
        sueldo_actual = trabajador_data["sueldo"]

        # Conseguir el aumento
        while True:
            try:
                aumento = int(input("\n>>> Ingrese el monto del aumento (en números): "))
                if aumento > 0:
                    break  # Valid raise amount entered
                else:
                    print(">>> El monto del aumento debe ser un número positivo.")
            except ValueError:
                print(">>> Entrada inválida. Por favor ingrese un número entero.")

        # Calcular el nuevo sueldo
        nuevo_sueldo = sueldo_actual + aumento

        # Actualizar el sueldo del trabajador en el diccionario
        trabajador_data["sueldo"] = nuevo_sueldo

        print(f"\n>>> El salario del trabajador con ID {trabajador_id} se ha actualizado de {sueldo_actual} a {nuevo_sueldo}.")
    else:
        print(f"\n>>> No se encontró ningún trabajador con ID: {trabajador_id}")

# Se inicia para llevar el control de las veces que se creo un ID
printed_workers = set()

if __name__ == "__main__":
    global id_actual  # Declara una variable global en 'if __name__ == "__main__":' 
    id_actual = 1  # Se inicia la variable global
    trabajadores = {}
    sueldo_cargo = {
        "LIMPIEZA": 1025,
        "MESERO": 1500,
        "CAJERO": 1500,
        "VIGILANTE": 1400,
        "GERENTE": 2500
    }

   
    agregar_trabajadores()
    menu()