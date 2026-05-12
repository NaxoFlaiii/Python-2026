# Datos Numericos
PI = 3.1415926535 
edad = 19
annio_nacimiento = 2007

# Numeros flotantes
Estatura = 1.75
Peso = 75

# Operacion aritmetica basica (area de un triangulo)
base = 8.7
altura = 12.5
area = (base * altura) / 2

# Salida de numeros
print(f"El numero PI con 1 decimales es: {PI:.1f}")

# numeros complejos
num_complejo = 4 + 2j 
otro_complejo = complex(4.2) 

# Redondear
area_redondeada = round(area)
print(f"El area del triangulo redondeada es: {area_redondeada} cm")

# transformaciones
print(float(edad))

# Cadenas de texto
carrera = "Ingenieria Civil en Informatica"
institucion = "Universidad los Lagos"
 

# Imprimir la posicion del caracter
print(carrera[0])
print(carrera[30])

print("Hola" * 4) 

print(carrera[0:11]) 

# Metodo len permite contar caracteres
print(len(institucion))

# ARREGLOS (LISTAS)
print("Arreglos de texto")
colores = ["Azul", "Rojo","Verde", "Amarillo" ]
numeros =[1,2,3,4,5,6]

print(colores)
print(numeros)

# Boleanos (Logicos)
interruptor = False
Luz_electrica = True # Recuerda que los nombres de variables no llevan espacios (bien hecho con el guion bajo)

print("Boleanos")
print(interruptor)
print(Luz_electrica)


# Type
print(f"El tipo de datos es {type(num_complejo)}")

# Evaluando datos bool
print(bool(1))
print(bool(0))
print(bool(""))
print(bool("false"))

#Evaluando numeros con operadores de comparacion
print (100 <= 50)
print (10 == 10)
print(20 < 0)