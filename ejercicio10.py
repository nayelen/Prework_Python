# Ejercicio 10: Determinar el Día de la Semana
# Escribe un programa que determine el día de la semana correspondiente a un
# número ingresado por el usuario (1 para lunes, 2 para martes, etc.).

dia = int(input('Elige un número del 1 al 7 para ver el día de la Semana: '))

def det_dia(dia):
  dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
  if dia >= 1 and dia <=7:
    return dias[dia-1]
  else:
    return 'No hay más días en la semana, elige un número del 1 al 7 campeón!'

nombre_dia = det_dia(dia)
print(nombre_dia)
