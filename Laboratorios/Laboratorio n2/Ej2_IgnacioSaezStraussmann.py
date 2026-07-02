print("LIMPIADOR DE REGISTROS ULAGOS")

codigo_identificador=(input(f"Ingrese su codigo identificador: "))

codigo_sin_espacios = codigo_identificador.strip()
codigo_sin_guiones= codigo_sin_espacios.replace("_", "")
codigo_a_mayusculas= codigo_sin_guiones.upper()

Longitud_del_codigo= len(codigo_a_mayusculas)

print (f"Codigo Identificador final limpio: {codigo_a_mayusculas}")

print (f"Longitud de caracteres {Longitud_del_codigo}")