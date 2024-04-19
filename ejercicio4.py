# Ejercicio 4: Contador de Vocales
# Crea un programa que cuente el número de vocales en una palabra ingresada por el usuario.

palabra = input('Introduce la palabra: ')

contador = 0
for i in palabra:
  if i in 'aeiouAEIOU':
    contador += 1
    
print('La cantidad de vocales es: ', contador)