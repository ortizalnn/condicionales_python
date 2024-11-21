'''Escribe un programa que pida un número entero entre uno y doce e imprima el 
 número de días que tiene el mes correspondiente.
 Si introducimos otro número nos da un error.'''
def obtener_dias_mes(mes):
    dias_por_mes = {
        1: 31,   # Enero
        2: 28,   # Febrero (no considera años bisiestos)
        3: 31,   # Marzo
        4: 30,   # Abril
        5: 31,   # Mayo
        6: 30,   # Junio
        7: 31,   # Julio
        8: 31,   # Agosto
        9: 30,   # Septiembre
        10: 31,  # Octubre
        11: 30,  # Noviembre
        12: 31   # Diciembre
    }

    if mes in dias_por_mes:
        return f"El mes {mes} tiene {dias_por_mes[mes]} días."
    else:
        return "Error: Número fuera de rango. Debe ser un número del 1 al 12."
try:
    mes = int(input("Introduce un número del 1 al 12 para obtener el número de días del mes: "))
    print(obtener_dias_mes(mes))
except ValueError:
    print("Error: Por favor, introduce un número válido.")