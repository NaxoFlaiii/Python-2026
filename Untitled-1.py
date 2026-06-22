def simulador_ajedrez():
    # a) Inicialización del tablero
    tablero = {}
    filas = "12345678"
    columnas = "abcdefgh"
    
    # Primero, creamos todas las casillas vacías usando bucles anidados
    for f in filas:
        for c in columnas:
            tablero[f"{c}{f}"] = None

    # Colocamos las piezas blancas (Fila 1 y 2)
    orden_piezas = ["Torre", "Caballo", "Alfil", "Reina", "Rey", "Alfil", "Caballo", "Torre"]
    for i, c in enumerate(columnas):
        tablero[f"{c}1"] = f"{orden_piezas[i]}B"
        tablero[f"{c}2"] = "PeonB"

    # Colocamos las piezas negras (Fila 7 y 8)
    for i, c in enumerate(columnas):
        tablero[f"{c}8"] = f"{orden_piezas[i]}N"
        tablero[f"{c}7"] = "PeonN"

    # b) Mapa de símbolos ASCII
    simbolos = {
        "TorreB": "R", "CaballoB": "N", "AlfilB": "B", "ReinaB": "Q", "ReyB": "K", "PeonB": "P",
        "TorreN": "r", "CaballoN": "n", "AlfilN": "b", "ReinaN": "q", "ReyN": "k", "PeonN": "p"
    }

    # d) Interacción con el usuario: Declarar lista de capturadas
    capturadas = []

    while True:
        # c) Mostrar el tablero dibujado (y f: Redibujar tras cada turno)
        print("\n  a b c d e f g h")
        for f in range(8, 0, -1):  # Bucle del 8 al 1 hacia atrás
            fila_str = f"{f} "
            for c in columnas:
                pieza = tablero[f"{c}{f}"]
                if pieza is not None:
                    fila_str += f"{simbolos[pieza]} " # Imprime el símbolo
                else:
                    fila_str += ". "                  # Imprime el punto si está vacío
            fila_str += str(f)
            print(fila_str)
        print("  a b c d e f g h")
        
        # f) Imprimir la lista de capturadas convertida a símbolos ASCII
        if capturadas:
            simbolos_capturados = [simbolos[p] for p in capturadas]
            print(f"\nPiezas capturadas: {' '.join(simbolos_capturados)}")

        # d) Solicitar input del usuario
        print("\n--- Nuevo Turno ---")
        origen = input("Ingrese casilla de origen (ej. e2) o escriba 'salir': ").lower()
        if origen == 'salir':
            print("Juego terminado.")
            break
            
        destino = input("Ingrese casilla de destino (ej. e4): ").lower()

        # e) Lógica de movimiento
        # Validar si la clave origen existe y tiene una pieza
        if origen not in tablero or tablero[origen] is None:
            print("\n** Error: No existe la clave origen o la casilla está vacía. **")
            continue
            
        # Validar que la casilla destino exista en el diccionario
        if destino not in tablero:
            print("\n** Error: La casilla de destino no es válida. **")
            continue

        # Extrae la pieza de origen
        pieza_origen = tablero[origen]
        pieza_destino = tablero[destino]

        # Si hay una pieza en el destino, se asume captura
        if pieza_destino is not None:
            capturadas.append(pieza_destino)
            print(f"\n>> ¡Capturó a {pieza_destino} en {destino.upper()}! <<")

        # Mover la pieza: actualizar destino y vaciar origen
        tablero[destino] = pieza_origen
        tablero[origen] = None

# Para ejecutar el juego, simplemente llama a la función:
# simulador_ajedrez()