# args y kwargs: se usan para enviar argumentos a una funcion
# kwargs: la diferencia es que kwargs hace uso de llaves para pasar cada argumento a una funcion
# args: no necesitan pasar una llave al argumento de la funcion

def func_args(param_comun, *args):
    print(f"Parametro comun: {param_comun}")
    print(f"Args: {args}")

func_args("Alexander", 1, 2, 3, 4, "5", 6.0, True, False)

def func_kwargs(param_comun2, **kwargs):
    print(f"Parametro comun 2: {param_comun2}")
    print(f"Kwargs: {kwargs}")

func_kwargs("Rafo", age = 20, curso = "Python")