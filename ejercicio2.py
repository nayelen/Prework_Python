# Ejercicio 2: Calculadora de Propina
# Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo una propina del 15% sobre el total de la cuenta.

comida = float(input('Introduce el importe de la comida: '))
print('El importe de la comida es: ', comida, '€')
propina = comida * 0.15 
print('La propina es: ', propina, '€')
precioTotal = comida + propina
print('El precio total es: ', precioTotal , '€')