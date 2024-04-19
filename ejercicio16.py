# Ejercicio 16: Contador de Números Pares e Impares
# Crea un programa que cuente y muestre la cantidad de números pares e impares en
# una lista ingresada por el usuario.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = 0
impares = 0

for numero in numeros:
  if numero % 2 == 0:
    pares += 1
  else:
    impares += 1

print('Los numeros pares son:', pares)
print('Los numeros impares son:', impares)
  