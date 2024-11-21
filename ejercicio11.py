'''La política de cobro de una compañía telefónica es: cuando se realiza una 
llamada, el cobro es por el tiempo que ésta dura, de tal forma que los primeros 
cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos,
los siguientes dos minutos, 70 céntimos, y a partir del décimo minuto, 50 céntimos.
Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno
de mañana, 15 %, y en turno de tarde, 10 %. 
Realice un programa para determinar cuánto debe pagar por cada concepto 
una persona que realiza una llamada.'''
def calcular_costo_llamada(duracion_minutos, dia, turno=None):
    if duracion_minutos <= 5:
        costo_base = duracion_minutos * 1
    elif duracion_minutos <= 8:
        costo_base = 5 * 1 + (duracion_minutos - 5) * 0.8
    elif duracion_minutos <= 10:
        costo_base = 5 * 1 + 3 * 0.8 + (duracion_minutos - 8) * 0.7
    else:
        costo_base = 5 * 1 + 3 * 0.8 + 2 * 0.7 + (duracion_minutos - 10) * 0.5
    
    
    if dia.lower() == "domingo":
        impuesto = 0.03 
    elif turno == "mañana":
        impuesto = 0.15 
    elif turno == "tarde":
        impuesto = 0.10  
    else:
        impuesto = 0 

    total_impuesto = costo_base * impuesto
    total = costo_base + total_impuesto
    
    return costo_base, total_impuesto, total

duracion = int(input("Ingrese la duración de la llamada en minutos: "))
dia = input("Ingrese el día de la semana: ")
turno = None
if dia.lower() != "domingo":
    turno = input("Ingrese el turno (mañana/tarde): ").lower()

costo_base, total_impuesto, total = calcular_costo_llamada(duracion, dia, turno)

print(f"Costo base de la llamada: {costo_base:.2f} euros")
print(f"Impuesto aplicado: {total_impuesto:.2f} euros")
print(f"Costo total de la llamada: {total:.2f} euros")