print("Informe lluvia caida Castro")

muestrameteorologica1=(float(input(f"Ingrese la primera muestra meteorologica=")))
muestrameteorologica2=(float(input(f"Ingrese la segunda muestra meteorologica=")))
muestrameteorologica3=(float(input(f"Ingrese la tercera muestra meteorologica=")))
muestrameteorologica4=(float(input(f"Ingrese la cuarta muestra meteorologica=")))
muestrameteorologica5=(float(input(f"Ingrese la quinta muestra meteorologica=")))

registro_lluvia= muestrameteorologica1, muestrameteorologica2, muestrameteorologica3, muestrameteorologica4, muestrameteorologica5

suma_registrolluvia = sum(registro_lluvia)
promedio= suma_registrolluvia / 5

registro_minimo= (min(registro_lluvia))
registro_maximo= (max(registro_lluvia))

brecha_pluvial= registro_maximo - registro_minimo

print (f"La brecha pluvial es = {brecha_pluvial}")
print (f"El promedio de todas las muestras es= {promedio}")

print (f"El Registro mas bajo registrado=" , registro_minimo)
print (f"El Registro mas alto registrado=" , registro_maximo)






