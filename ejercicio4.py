'''Crea un programa que pida al usuario dos numeros y muestre division
si el segundo es cero, o un mnesaje de aviso en caso contradictorio'''
num1 = int(input("Ingreseun numero: "))
num2 = int(input("Ingrese un numero:" ))
if num2 == 0:
    print(f"no se puede dividir entre cero.")
else:
    print(f"la division es: ", num1/num2)    