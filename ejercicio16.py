# Ejercicio 16: Contador de Números Pares e Impares
# Crea un programa que cuente y muestre la cantidad de números pares e impares en
# una lista ingresada por el usuario.

def contarParesImpares(lista):
  pares = 0
  impares = 0
  for num in lista:
    if num % 2 == 0:
      pares +=1
    else:
      impares += 1
  return pares, impares

numeros = list(map(int, input('Introduce una lista de números separados por espacios: ').split()))
pares, impares = contarParesImpares(numeros)
print(f"La lista tiene {pares} números pares y {impares} números impares")