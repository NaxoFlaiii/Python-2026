sueldo_base_chile = 529000
ventas_vendedores = {
    "Pancho": [300000, 400000, 350000, 500000, 200000], 
    "Victor": [150000, 200000, 150000, 250000, 300000], 
    "Alan": [50000, 80000, 100000, 60000, 70000]    
}

for nombre, ventas in ventas_vendedores.items():
    total_ventas = sum(ventas)

    bono = 0
    if total_ventas > 1500000:
       
        bono = sueldo_base_chile * 0.20
    elif total_ventas > 1000000:
        bono = sueldo_base_chile * 0.10
    elif total_ventas > 500000:
        bono = sueldo_base_chile * 0.05
    else:
        bono = 0

    promedio = total_ventas / 5

    
    sueldo_total = sueldo_base_chile + bono


    print("--------------------------------------------")
    print("Reporte del vendedor:")
    print("Nombre del vendedor:", nombre)
    print("Total de ventas: $", total_ventas)
    print("Promedio de ventas diarias: $", promedio)
    print("Bono ganado: $", int(bono))
    print("Sueldo total a pagar: $", int(sueldo_total))

