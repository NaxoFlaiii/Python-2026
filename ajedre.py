# ==========================
# Inicialización del tablero
# ==========================

tablero = {}

# Piezas principales
fila_blancas = [
    "TorreB", "CaballoB", "AlfilB", "ReinaB",
    "ReyB", "AlfilB", "CaballoB", "TorreB"
]

fila_negras = [
    "TorreN", "CaballoN", "AlfilN", "ReinaN",
    "ReyN", "AlfilN", "CaballoN", "TorreN"
]

columnas = "abcdefgh"

# Colocar piezas blancas
for i in range(8):
    tablero[columnas[i] + "1"] = fila_blancas[i]
    tablero[columnas[i] + "2"] = "PeonB"

# Colocar piezas negras
for i in range(8):
    tablero[columnas[i] + "8"] = fila_negras[i]
    tablero[columnas[i] + "7"] = "PeonN"

# ==========================
# Diccionario de símbolos
# ==========================

simbolos = {
    "TorreB": "R",
    "CaballoB": "N",
    "AlfilB": "B",
    "ReinaB": "Q",
    "ReyB": "K",
    "PeonB": "P",

    "TorreN": "r",
    "CaballoN": "n",
    "AlfilN": "b",
    "ReinaN": "q",
    "ReyN": "k",
    "PeonN": "p"
}

# Lista de piezas capturadas
capturadas = []

# ==========================
# Función para mostrar tablero
# ==========================

def mostrar_tablero():
    print()
    print("  a b c d e f g h")

    for fila in range(8, 0, -1):
        print(fila, end=" ")

        for col in columnas:
            casilla = col + str(fila)

            if casilla in tablero:
                pieza = tablero[casilla]
                print(simbolos[pieza], end=" ")
            else:
                print(".", end=" ")

        print(fila)

    print("  a b c d e f g h")
    print()


# ==========================
# Juego
# ==========================

while True:
    mostrar_tablero()

    if capturadas:
        print("Piezas capturadas:", end=" ")
        for pieza in capturadas:
            print(simbolos[pieza], end=" ")
        print()
    else:
        print("Piezas capturadas: Ninguna")

    origen = input("\nCasilla de origen (o 'salir'): ").lower()

    if origen == "salir":
        break

    if origen not in tablero:
        print("Error: no existe una pieza en esa casilla.")
        continue

    destino = input("Casilla de destino: ").lower()

    pieza = tablero[origen]

    # Verificar si hay captura
    if destino in tablero:
        pieza_destino = tablero[destino]

        # Solo captura si son de distinto color
        if pieza[-1] != pieza_destino[-1]:
            capturadas.append(pieza_destino)
            print(f"Capturó a {pieza_destino} en {destino.upper()}")
        else:
            print("No puedes capturar una pieza de tu mismo color.")
            continue

    # Mover la pieza
    tablero[destino] = pieza
    del tablero[origen]

print("\nJuego terminado.")