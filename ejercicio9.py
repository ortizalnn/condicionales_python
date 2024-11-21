'''PROGRAMA QUE PIDA TRES NUMEROS Y LOS MUESTRE ORDENADOS(MAYOR A MENOR)'''
numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))
numero3 = float(input("Ingrese el tercer numero: "))
numeros = [numero1, numero2, numero3]
numeros.sort(reverse=True)
print("Numeros ordenados de mayor a menor: ", numeros)