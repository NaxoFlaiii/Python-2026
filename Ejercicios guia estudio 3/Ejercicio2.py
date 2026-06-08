rut_original = " 19.543.872-K "
rut_sinespacios = rut_original.strip()
rut_limpio =rut_sinespacios.replace(".","")

largototal= len(rut_limpio)
print (f"Rut con nuevo formato = {rut_limpio}")
print (f"longitud del nuevo rut = {largototal} caracteres")