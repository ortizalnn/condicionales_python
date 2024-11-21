def calcular_potencia(base, exponente):
    if exponente > 0:
        return base ** exponente
    elif exponente == 0:
        return 1
    else:
        return 1 /(base ** abs(exponente))
base = float(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))
resultado = calcular_potencia(base, exponente)
print(f"El resultado de {base} elevado a {exponente} es: {resultado}")