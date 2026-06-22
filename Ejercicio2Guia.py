
suma_total = 0


numero_suma_diez = 500
numero_resta_dos = 456


while numero_suma_diez <= 800:
    
   
    suma_total = suma_total + numero_suma_diez
    
   
    if numero_suma_diez == 800:
        break
    
    
    suma_total = suma_total + numero_resta_dos
    
    numero_suma_diez = numero_suma_diez + 10  
    numero_resta_dos = numero_resta_dos - 2   


print("La suma total es:", suma_total)