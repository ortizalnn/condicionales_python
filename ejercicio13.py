'''Realiza un programa que pida el dia de la semana (del 1 al 7) y escriba 
 el dia correspondiente. 
 Si introducimos otro número nos da un error.'''
def obtener_dia_semana(numero):
    dias = {
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sábado",
        7: "Domingo"
    }

    if numero in dias:
        return f"El día correspondiente es: {dias[numero]}"
    else:
        return "Error: Número fuera de rango. Debe ser un número del 1 al 7."

try:
    numero = int(input("Introduce un número del 1 al 7 para obtener el día de la semana: "))
    print(obtener_dia_semana(numero))
except ValueError:
    print("Error: Por favor, introduce un número válido.")