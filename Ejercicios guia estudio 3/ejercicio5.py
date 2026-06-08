t1 = float(input("Ingrese la muestra 1 (ms): "))
t2 = float(input("Ingrese la muestra 2 (ms): "))
t3 = float(input("Ingrese la muestra 3 (ms): "))

tiempos_respuesta = [t1, t2, t3]

suma = tiempos_respuesta[0] + tiempos_respuesta[1] + tiempos_respuesta[2]
promedio = suma / 3

tiempo_rapido = min(tiempos_respuesta)

tiempo_lento = max(tiempos_respuesta)

brecha_rendimiento = tiempo_lento - tiempo_rapido

print(f"Lista completa de datos registrados : {tiempos_respuesta} ms")
print(f"Tiempo promedio de respuesta         : {promedio:.2f} ms")
print(f"Tiempo más rápido (Mínimo)         : {tiempo_rapido} ms")
print(f"Tiempo más lento (Máximo)          : {tiempo_lento} ms")
print(f"Brecha de rendimiento calculada    : {brecha_rendimiento:.2f} ms")
