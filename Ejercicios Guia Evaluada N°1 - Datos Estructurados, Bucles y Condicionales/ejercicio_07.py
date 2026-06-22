"""" 7. Determinar el factorial de un número n, donde:
n! = n·(n - 1)·(n - 2)..,3·2·1

factorial(x) =
1
si x = 0
x · factorial(x − 1) six ≥ 1
(2.2)
(2.3)"""

n = int(input("Ingrese un número:"))
factorial = 1
for i in range (1, n + 1):
    factorial = factorial * i
print ("El factorial es:",  factorial)

# Código realizado con mi compañero Victor Saldivia