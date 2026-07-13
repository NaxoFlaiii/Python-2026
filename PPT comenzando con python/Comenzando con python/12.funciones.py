def multiplicacion (x):
    return x * 10
y=multiplicacion(2)
print(f"El resultado de la multiplicación es: {y}")

def saludo(nombre):
    print(f"Hola, mi nombre es {nombre}")

saludo("Pancho")
#Saluda: a llamada a la funcion imprime un hola.

def suma (a,b):
    return a + b
#LLamada a la funcion con argumentos posicionales :2->a, ->b
resultado = suma(2, 3)
#El orden si importa a=2, b=3
print(f"El resultado de la suma es: {resultado}")

# Definición de la función "resta" con parámetro por defecto (b=5)
def resta(a, b=5):
    return a - b
resultado1= resta(6)
print("Resultado 1 (b por defecto):", resultado1)
resultado2 = resta(4,4)
print("Resultado 2 (b especificado):", resultado2)

def factorial_normal(n):
    r = 1
    i = 2
    while i <= n:
        r *= i
        i += 1  
    return r    

print(factorial_normal(5))  
