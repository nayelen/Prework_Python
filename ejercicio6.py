# Ejercicio 6: Verificación de Palíndromo
# Crea un programa que verifique si una palabra ingresada por el usuario es un
# palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).

palabra = input('Ingrese la palabra: ')

def es_palindromo(palabra):
  palabra = palabra.lower()
  return palabra == palabra[::-1]
print(es_palindromo(palabra))