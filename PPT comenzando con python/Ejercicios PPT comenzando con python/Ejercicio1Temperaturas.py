#Promedio y diferencias de temperaturas
Temperaturas = [12.5, 14.2, 11.8]
Promedio = sum(Temperaturas) / len(Temperaturas)
Diferencia = max(Temperaturas) - min(Temperaturas)

print(Temperaturas)

print(f"El promedio de las temperaturas es de {round(Promedio)}")

print(f"La diferencia entre la temperatura máxima ({max(Temperaturas)}) y la temperatura mínima ({min(Temperaturas)}) es {round(Diferencia)}")