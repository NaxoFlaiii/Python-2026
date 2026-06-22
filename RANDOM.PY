# Empezamos con nuestra caja de suma vacía
suma_total = 0

# Definimos dónde empiezan nuestras dos secuencias
num_sube = 500
num_baja = 456

# El ciclo se repetirá mientras el número que sube sea menor o igual a 800
while num_sube <= 800:
    
    # 1. Sumamos a nuestro total el número de la secuencia que sube
    suma_total = suma_total + num_sube
    
    # IMPORTANTE: Como la serie termina exactamente en 800 (que es de la secuencia que sube),
    # si ya llegamos a ese número, debemos romper el ciclo para no sumar nada más.
    if num_sube == 800:
        break
        
    # 2. Sumamos a nuestro total el número de la secuencia que baja
    suma_total = suma_total + num_baja
    
    # 3. Preparamos los números para la siguiente vuelta del ciclo
    num_sube = num_sube + 10  # Le sumamos 10 al que sube
    num_baja = num_baja - 2   # Le restamos 2 al que baja

# Finalmente, imprimimos el resultado en pantalla
print("La suma total es:", suma_total)