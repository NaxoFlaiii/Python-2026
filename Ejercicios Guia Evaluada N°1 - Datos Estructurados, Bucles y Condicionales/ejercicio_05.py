simbolos = {
    "PeónB": "P", "TorreB": "T", "AlfilB": "A", "ReyB": "K", "ReinaB": "Q", "CaballoB": "C",
    "PeónN": "p", "TorreN": "t", "AlfilN": "a", "ReyN": "k", "ReinaN": "q", "CaballoN": "c",
    "": "."
}

tablero = [
    ["TorreB", "CaballoB", "AlfilB", "ReyB", "ReinaB", "AlfilB", "CaballoB", "TorreB"],
    ["PeónB", "PeónB", "PeónB", "PeónB", "PeónB", "PeónB", "PeónB", "PeónB"],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["PeónN", "PeónN", "PeónN", "PeónN", "PeónN", "PeónN", "PeónN", "PeónN"],
    ["TorreN", "CaballoN", "AlfilN", "ReyN", "ReinaN", "AlfilN", "CaballoN", "TorreN"],
]

letras = ("  A B C D E F G H")
print (letras)
for fila in range(8):
    print(fila + 1, end=" ")

    for columna in range(8):
        print(simbolos[tablero[fila][columna]], end=" ")


    print()

print(letras)

# Código realizado con mi compañero Victor Saldivia