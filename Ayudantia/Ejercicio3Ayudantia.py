mis_notas = []


mis_notas.append(5.5)
mis_notas.append(3.6) 
mis_notas.append(5.5)
mis_notas.append(5.5)
mis_notas.append(5.6)



sumanotas = sum(mis_notas)

promedio_notas = sumanotas / 5

print('Nota 1:', mis_notas[0])
print('Nota 2:', mis_notas[1])
print('Nota 3:', mis_notas[2])
print('Nota 4:', mis_notas[3])
print('Nota 5:', mis_notas[4])


print('Nota máxima:', max(mis_notas))
print('Nota mínima:', min(mis_notas))
 
print('Promedio notas:', promedio_notas)