"""En la asignatura de Programación de la carrera de Ingeniería Civil en Informática,
un estudiante ha rendido sus primeras 3 calificaciones de tareas prácticas de
laboratorio. La aprobación de la asignatura exige calcular una nota final basada
en los siguientes pesos o ponderaciones para cada laboratorio:
Laboratorio 1: 40% de la nota finalssf
Laboratorio 2: 40% de la nota final
Laboratorio 3: 20% de la nota final"""
nota1 = float(input(f"Ingrese la nota del laboratorio 1: "))
nota2 = float(input(f"Ingrese la nota del laboratorio 2: "))
nota3 = float(input(f"Ingrese la nota del laboratorio 3: "))

notas = [nota1], [nota2], [nota3]
print(notas)

porcentaje1 = notas[0] * 40
porcentaje2 = notas[1] * 20
porcentaje3 = notas[2] * 20



print(f"Nota lab 1 [nota1]")




