# Pedir al usuario que ingrese el número de alumnos
num_alumnos = int(input("Ingresa el número de alumnos: "))

# Inicializar variables

costo_por_alumno = 0

costo_total = 0

# Determinar el costo por alumno y el costo total

if num_alumnos >= 100:

  costo_por_alumno = 65

  costo_total = costo_por_alumno *num_alumnos

elif 50 <= num_alumnos < 99:

  costo_por_alumno = 70

  costo_total = costo_por_alumno * num_alumnos

elif 30 <= num_alumnos < 49:

  costo_por_alumno = 95

  costo_total = costo_por_alumno * num_alumnos

else: # Menos de 30 alumnos

  costo_total = 4000 # Costo fijo

  costo_por_alumno = costo_total /num_alumnos 
# Cálculo del costo por alumno

# Mostrar los resultados

print(f"Costo por alumno:{costo_por_alumno} euros")

print(f"Costo total a pagar a la compañía: {costo_total} euros")