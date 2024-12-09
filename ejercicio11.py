# Ejercicio 11: Calculadora de Edad
# Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad
# actual.

from datetime import datetime

año = int(input('Introduce tu año de nacimiento: '))
fecha_actual = datetime.now()
año_actual = fecha_actual.year
edad = año_actual - año
print('Tu edad es ',edad, 'años o estás a punto de tenerlos!! 😅')