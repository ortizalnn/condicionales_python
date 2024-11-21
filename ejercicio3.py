#Pedir al usuario que ingrese un numero
numero = input("ingresa un número: ")
#Intenta convertir la entrada a un numero entero
try:
    numero = int(numero) 
    #  Convertir la entrada a entero
    # verificar si es par o impar
    if numero% 2 == 0:
        print(f"{numero} es par. ")
    else:
        print(f"{numero} es impar. ") 
except valuError:
    print("por favor, ingresa un número valido. ")   
