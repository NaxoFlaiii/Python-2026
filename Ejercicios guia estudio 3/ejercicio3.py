nombre_completo = input(f"Ingrese su nombre completo: ")
nombre_sin_extremos = nombre_completo.strip()
nombresinmayusculas = nombre_sin_extremos.lower()
nombre_con_puntos = nombresinmayusculas.replace(" ", ".")
correo_final = nombre_con_puntos + "@alumnos.ulagos.cl"

print("Correo creado", correo_final)
