#Ejercicio 5: Suma de Números Pares
# Escribe un programa que calcule la suma de todos los números pares del 1 al 100.

suma = 0
inicio = 1
fin = 101

while inicio < fin:
  if inicio % 2 == 0:
    print(inicio)
    suma = suma + inicio
  inicio += 1

print('La suma de los numeros pares es: ', suma)