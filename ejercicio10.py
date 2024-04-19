# Ejercicio 10: Determinar el Día de la Semana
# Escribe un programa que determine el día de la semana correspondiente a un
# número ingresado por el usuario (1 para lunes, 2 para martes, etc.).

dia = int(input('Elige un número del 1 al 7 para ver el día de la Semana: '))

if dia == 1:
  print('Lunes')
elif dia == 2:
  print('Martes')
elif dia == 3:
  print('Miércoles')
elif dia == 4:
  print('Jueves')
elif dia == 5:
  print('Viernes')
elif dia == 6:
  print('Sábado')
elif dia == 7:
  print('Domingo')
else:
  print('No hay más días en la semana, elige un número del 1 al 7 campeón!')