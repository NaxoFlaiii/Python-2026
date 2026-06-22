parrafo = input('Ingrese su párrafo, cuando termine presione "Enter": ').strip()

if not parrafo:
    print("ValueError: El texto no puede estar vacío.")
else:
    parrafoseparado = parrafo.split()
    print(parrafoseparado)
    palabra_buscada = input('¿Qué palabra quiere buscar? ').strip()
    contar = parrafoseparado.count(palabra_buscada)
    print(f"La palabra '{palabra_buscada}' aparece un total de {contar} veces.")

# Código realizado con mi compañero Victor Saldivia