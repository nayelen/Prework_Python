# Ejercicio 20: Suma de Números en una Lista
# Crea un programa que sume todos los números en una lista ingresada por el
# usuario.


numeros = list(map(int, input('Ingresa los valores que deseas sumar separados por un espacio:').split()))
print('La suma de todos los números es: ', sum(numeros))