print("1.Hamburguesa")
print("2.Pizza")
print("3.Completo Italiano")

opcion = input('Porfavor, elige una opcion (1-3): ')

match opcion:
    case "1":
        print("Has elegido una hamburguesa. Precio: $5000")
    case "2":
        print("Has elegido pizza. Precio: $7500 ")
    case"3":
        print("has elegido Completo. Precio: $2500 ")
    case _:
        print("Opcion no valida. Por favor, elige entre 1 y 3")
    
mes = 4
match mes:
    case 12 | 1 | 2 :
        print("Verano")
    case 3 | 4 | 5 :
        print("Otoño")
    case 6 | 7 | 8 :
        print("Invierno") 
    case 9 | 10 | 11 :
        print("Primavera")
    case _:
        print("Mes no valido. Por favor, elige un numero entre 1 y 12")

hora = 18
match hora:
    case h if 0 <=h < 0:
        print("Buenas Madrugada")
    case h if 6 <=h < 12:
        print("Buenos Dias")
    case h if 12 <=h < 18:
        print("Buenas Tardes")
    case h if 18 <=h < 24:
        print("Buenas Noches")
    case _:
        print("Hora no valida. Por favor, elige un numero entre 0 y 23")

x = [1, 2, 3]
match x:
    case[a, b, c]:
        print(f"Elementos de la lista x : {a}, {b}, {c}")
    
datos = {
    "nombre": "Ignacio",
    "edad": 19,   
}
match datos:
    case {"nombre": n, "edad": e}:
        print(f"Nombre: {n}, Edad: {e}")

valor = 6
match valor:
    case x if x % 2 == 0:
        print(f"{valor} es un numero par")
    case x if x % 2 != 0:
        print(f"{valor} es un numero impar")