# LISTAS

# Primera Forma de Declaración de Listas (Lista Mixta)
lista1 = ["Ignacio", 19, True, "Ignacio", "Ignacio", "Ignacio"]
ramos = [] # Lista vacia

# Segunda Forma de Declaración de Listas (lista Númerica)
n = list([1,2,3,4,5])

# Métodos para las Listas
# 01- COUNT() - Contar la cantidad de concurrencias de un elemento
print(lista1.count('Ignacio'))
print (ramos)

#Agregar un elemento al final de la lista
ramos .append("Quimica")
print(ramos)

ramos .append("Habilidades comunicativas")
print(ramos)

ramos .append("Programación")
print(ramos)


# Otra forma de insertar un elemento a la lista (de forma especifica)
ramos .insert(0, "Introduccion a la matematica")
print(ramos)




#Modificar un elemento especifico de una lista
ramos [2] = "Habilidades comunicativas para ingenieros"
print (ramos)

#Eliminar el ultimo elemento de la lista
ramos .pop()
print (ramos)

# Ordenar los elementos de una lista de una forma descendente a ascendente
ramos.sort()
print (ramos)
