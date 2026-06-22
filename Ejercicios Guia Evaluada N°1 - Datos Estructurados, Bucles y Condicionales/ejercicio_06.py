""""6. Simular el comportamiento de un reloj digital, imprimiendo la hora, minutos y segundos
de un día desde las 00:00:00 horas hasta las 23:59:59 horas."""
for hora in range (24):
    for minuto in range (60):
        for segundo in range (60):
            print(f"{hora:02}:{minuto:02}:{segundo:02}")

# Código realizado con mi compañero Victor Saldivia