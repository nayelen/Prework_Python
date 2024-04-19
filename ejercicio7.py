# Ejercicio 7: Calculadora Simple
# Crea un programa que realice operaciones aritméticas simples (suma, resta,
# multiplicación, división) según la elección del usuario.

num1 = int(input('Numero 1: '))
num2 = int(input('Numero 2: '))
opcion = input('Selecciona + , - , * , / :')

if opcion == '+':
  total = num1 + num2
if opcion == '-':
  total = num1 - num2
if opcion == '*':
  total = num1 * num2
if opcion == '/':
  total = num1 / num2
print(total)