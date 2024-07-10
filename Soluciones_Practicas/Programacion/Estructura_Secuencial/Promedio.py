"""Promedio de notas con Estructura Simple en Python
Descripción:

Este programa en Python ayuda a un estudiante a calcular el promedio de las notas de sus 5 materias.

Pasos:

Solicitar las notas:
Se utilizan las variables nota1, nota2, nota3, nota4, y nota5 para almacenar las notas de cada materia.
Se utiliza un ciclo for para solicitar al usuario que ingrese cada nota.
Calcular el promedio:
Se suma el valor de todas las notas utilizando la variable promedio.
Se divide el valor de promedio por la cantidad de materias (en este caso, 5).
Mostrar el promedio:
Se imprime el valor de promedio con un mensaje que indica que es el promedio general."""




# Se inicializan las variables
nota1 = 0
nota2 = 0
nota3 = 0
nota4 = 0
nota5 = 0
promedio = 0

# Se solicitan las notas al usuario
for i in range(1, 6):
  print(f"Ingrese la nota de la materia {i}:")
  nota = float(input())
  if nota >= 0 and nota <= 10:
    if i == 1:
      nota1 = nota
    elif i == 2:
      nota2 = nota
    elif i == 3:
      nota3 = nota
    elif i == 4:
      nota4 = nota
    else:
      nota5 = nota
  else:
    print("Error: La nota debe estar entre 0 y 10.")
    i -= 1  # Se repite la solicitud de la nota

# Se calcula el promedio
promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

# Se muestra el promedio
print(f"El promedio general es: {promedio:.2f}")