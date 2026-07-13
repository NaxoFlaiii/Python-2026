productos = [
    "Pan", "Leche", "Pan",
    "Queso", "Leche", 
    "Jugo", "Pan"
]

productos_cantidad = len(productos)
print("Cantidad total de registros: ", productos_cantidad)

productos_set = set(productos)

print("Productos distintos sin repetir", productos_set)

print("Productos distintos:")
for producto in productos_set:
    print(producto)

if "Jugo" in productos_set:
    print("El producto Jugo fue vendido.")
else:
    print("El producto Jugo no fue vendido.")