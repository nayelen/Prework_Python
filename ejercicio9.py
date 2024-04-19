# Ejercicio 9: Conversor de Divisas
# Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que
# 1 dólar es igual a 0.85 euros.

conversor = float(input('Introduce el importe en $ que quieres convertir:' ))

euros = conversor * 0.85
print(conversor, '$ equivale a ', euros, '€')