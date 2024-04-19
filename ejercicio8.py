# Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
# Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.

peso = float(input('Introduzca su peso en kg: '))
altura = float(input('Introduzca su altura en m: '))

indice = float(peso / altura**2)

if indice < 20:
  print('Tu IMC es: ', indice, 'es Peso Bajo')
elif indice >= 20 and indice < 25:
  print('Tu IMC es: ', indice, 'es Normal')
elif indice >= 25 and indice < 30:
  print('Tu IMC es: ', indice, 'es Sobrepeso')
elif indice >= 30 and indice < 35:
  print('Tu IMC es: ', indice, 'es Obesidad')
else:
  print('Tu IMC es: ', indice, 'es Obesidad Morbida')