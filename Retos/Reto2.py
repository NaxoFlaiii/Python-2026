conceptos_repetidos = ['inmutable', 'iterable', 'inmutable', 'hashable', 'interpretado', 'iterable'] 
conceptos_sin_duplicar = set(conceptos_repetidos)

lista_ordenada = list(conceptos_sin_duplicar)
lista_ordenada.sort() 

print("Conceptos limpios:", lista_ordenada)

glosario = {}

glosario['hashable'] = 'Objeto cuyo valor hash nunca cambia y puede ser clave.' 
glosario['inmutable'] = 'Objeto con un valor fijo que no se puede modificar.' 
glosario['interpretado'] = 'Lenguaje donde el código se ejecuta línea a línea.' 
glosario['iterable'] = 'Objeto capaz de devolver sus elementos uno a la vez.' 

print(" Buscador ")

palabra_ingresada = input("Ingrese un concepto a buscar: ").strip().lower()

definicion_encontrada = glosario.get(palabra_ingresada, "Concepto no encontrado en el glosario.")

print("Resultado de la búsqueda:", definicion_encontrada)

registro_busqueda = (palabra_ingresada, definicion_encontrada) 


print("Registro guardado en el sistema:", registro_busqueda)