# Ejercicio 19: Verificación de Año Bisiesto
# Escribe un programa que determine si un año ingresado por el usuario es bisiesto o no.

año = int(input('Introduce el año: '))

if año % 4 == 0:
    print('Es un año bisiesto')
else:
    print('No es un año bisiesto')

