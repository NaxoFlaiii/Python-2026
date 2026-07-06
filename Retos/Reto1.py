print("Ingresa tus notas")
nota1 = float(input("Ingresa la nota del Laboratorio 1 : "))
nota2 = float(input("Ingresa la nota del Laboratorio 2 : "))
nota3 = float(input("Ingresa la nota del Laboratorio 3 : "))

lista_notas = [nota1, nota2, nota3]


promedio_final = (lista_notas[0] * 0.40) + (lista_notas[1] * 0.40) + (lista_notas[2] * 0.20)


print(" Reporte de Notas:")
print(f"Laboratorio 1 (40%): {lista_notas[0]}")
print(f"Laboratorio 2 (40%): {lista_notas[1]}")
print(f"Laboratorio 3 (20%): {lista_notas[2]}")

print(f"Promedio: {round(promedio_final, 2)}")


