notas = {
    "Ana" : 6.2,
    "Luis": 4.8,
    "Pedro": 3.9,
    "Sofia": 5.5
}

total_aprobados = 0

for nombre, nota in notas.items():
    if nota >= 4.0:
        estado = "Aprobado"
        total_aprobados += 1
    else:
        estado = "Reprobado"
        
    print(f"{nombre} : {nota}  {estado}")

print()
print(f"Total de aprobados: {total_aprobados}")