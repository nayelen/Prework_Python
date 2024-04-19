# Ejercicio 15: Conversor de Tiempo
# Escribe un programa que convierta un número de minutos en horas y minutos. Por
# ejemplo, 145 minutos serían 2 horas y 25 minutos.

minutos = int(input('Introduce los minutos a convertir: '))

horas = minutos// 60
sobrante = minutos%60
 
print(minutos, 'minutos equivale a',horas, 'hr y',sobrante, 'minutos')