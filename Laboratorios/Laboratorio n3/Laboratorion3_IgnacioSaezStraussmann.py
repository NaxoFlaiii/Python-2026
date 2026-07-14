censo_2017 = {
    14: {
        "nombre_region": "Los Rios",
        "Superficie" : 18429,
        "habitantes" : 404432
    },
    12 : {
        "nombre_region": "Magallanes",
        "Superficie" : 1382291,
        "habitantes" : 166533
    }
}
print(f"Diccionario inicial:  {censo_2017} ")


densidad14 = round(censo_2017[14]["habitantes"] / censo_2017[14]["Superficie"], 1)
densidad12 = round(censo_2017[12]["habitantes"] / censo_2017[12]["Superficie"], 1)

censo_2017[14]["densidad"] = densidad14 
censo_2017[12]["densidad"] = densidad12 

censo_2017[14]["Capital"] = "Valdivia"
censo_2017[14]["Comunas"] = ["Rio Bueno", "La Union", "Paillaco"]
censo_2017[14]["Coordenadas_simuladas"] = (-39.8, -73.2)
censo_2017[14]["Zonas_exclusivas"] = {"Urbana", "Rural", "Fronteriza"}

censo_2017[12]["Capital"] = "Punta Arenas"
censo_2017[12]["Comunas"] = ["Cabo de Hornos", "Puerto Williams", "Porvenir"]
censo_2017[12]["Coordenadas_simuladas"] = (-59.9, -90.2)
censo_2017[12]["Zonas_exclusivas"] = {"Urbana", "Rural", "Fronteriza"}


censo_2017[12]["nombre_region"] = "Magallanes y Antártica Chilena" 

while True:
    region = input("Ingrese el ID de la region para revisar sus comunas  (12 o 14)Si desea salir escriba 'salir' o 0: ")
    
    if region == "salir" or region == "0":
        print("¡Hasta luego!")
        break
        
    elif region == "12" :
        nombre = censo_2017[12]['nombre_region'] 
        comunas = censo_2017[12]['Comunas']
        print(f"El id {region} corresponde a la region de {nombre},sus comunas son {comunas}")
        
    elif region == "14":
        nombre = censo_2017[14]['nombre_region'] 
        comunas = censo_2017[14]['Comunas']
        print(f"El id {region} corresponde a la region de {nombre},sus comunas son {comunas}")
        
    else:
        print("ID de región no válido. Intente nuevamente.")


print(f"Las claves del diccionario final son: {censo_2017.keys()}")