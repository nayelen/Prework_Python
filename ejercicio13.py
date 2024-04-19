# Ejercicio 13: Verificación de Número Primo
# Escribe un programa que determine si un número ingresado por el usuario es primo
# o no. 

numero = int(input('Verifica si el número es primo: '))

es_primo = True
for i in range(2, numero):
  if numero % i == 0:
    es_primo = False
    break
  
if es_primo:
  print('El número',numero, 'es primo')
else:
  print('El número',numero,'no es primo')