lista = [150, 95, 200, 30, 101, 170, 80, 210]
contador = 0
x = 0
while x<len(lista):
if lista[x]>100:
contador=contador+1
x=x+1
print("Los numeros de la lista son:", lista)
print("Los numeros mayores a 100 son", contador)
