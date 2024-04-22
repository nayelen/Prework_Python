# Ejercicio 1: Conversor de Temperatura
# Escribe un programa que convierta una temperatura de grados Celsius a grados
# Fahrenheit.
# °F = (9/5)°C + 32

grados = float(input('Escribe los grados Celsius a convertir:'))
F = 9 / 5 * grados + 32 
print(grados, 'grados Celsius equivale a' ,F, 'grados Farenheit')