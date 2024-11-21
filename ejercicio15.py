'''Programa que lea las opciones de 2 jugadores, y muestra el resultado
 Empate, gana jugador 1 o gana jugador 2
 Si introducimos una opción que no coindica con piedra, papel o tijera
 Diga que opción Incorrecta'''
def determinar_ganador(jugador1, jugador2):
    opciones_validas = ["piedra", "papel", "tijera"]
    if jugador1 not in opciones_validas or jugador2 not in opciones_validas:
        return "Opción incorrecta: ambos jugadores deben elegir entre 'piedra', 'papel' o 'tijera'."
    if jugador1 == jugador2:
        return "Empate"
    if (jugador1 == "piedra" and jugador2 == "tijera") or \
       (jugador1 == "papel" and jugador2 == "piedra") or \
       (jugador1 == "tijera" and jugador2 == "papel"):
        return "Gana jugador 1"
    else:
        return "Gana jugador 2"
jugador1 = input("Jugador 1, elige piedra, papel o tijera: ").lower()
jugador2 = input("Jugador 2, elige piedra, papel o tijera: ").lower()
resultado = determinar_ganador(jugador1, jugador2)
print(resultado)