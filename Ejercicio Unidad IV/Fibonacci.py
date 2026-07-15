def fibonacci_recursivo(n):
    # Casos base (0 y 1)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Caso recursivo
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

# Ejemplo: 5to número de Fibonacci (Se empieza del cero)
print(f"5to Número de Fibonacci: {fibonacci_recursivo(5)}")

def fibonacci_iterativo(n):
    # Casos base (0 y 1)
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b  # Se actualizan los valores
    return a

# Ejemplo: 5to número de Fibonacci (Se empieza del cero)
print(f"5to Número de Fibonacci: {fibonacci_iterativo(5)}")