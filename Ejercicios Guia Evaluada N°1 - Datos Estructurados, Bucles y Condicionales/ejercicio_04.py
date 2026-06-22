"""4. Desarrollar un algoritmo que permita devolver la siguiente propiedad descubierta por
Nicomaco de Gerasa:

Sumando el primer impar,se obtiene el primer cubo. 
Sumando los dos siguientes impares,se obtiene el segundo cubo.
Sumando los tres siguientes,se obtiene el tercer cubo,y asi sucesivamente.

Ejemplo:
13=1=1
23=3+5=8
33=7+9+11=27
43=13+15+17+19=64

Imprimir por pantalla, los primeros n cubos, considerando el valor de n obtenido desde
teclado"""""

n = int(input("Ingrese el número que desee: "))

impar = 1

for i in range(1, n + 1):
    suma = 0
    expresion = ""

    for j in range(i):
        suma += impar
        expresion += str(impar)

        if j < i - 1:
            expresion += " + "

        impar += 2

    print(str(i) + "³ = " + expresion + " = " + str(suma))

# Código realizado con mi compañero Victor Saldivia 