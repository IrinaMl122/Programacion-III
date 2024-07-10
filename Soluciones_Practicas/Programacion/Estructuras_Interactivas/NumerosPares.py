"""Mostrar sólo los números pares desde 0 hasta el número ingresado (input).
Nota: para saber si un número es par hacer i % 2 == 0)"""

numero_maximo = int(input("Ingrese el número máximo: "))

for numero in range(0, numero_maximo + 1):
  if numero % 2 == 0:
    print(numero)