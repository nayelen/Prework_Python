#Ejercicio 18: Contador de Palabras
#Crea un programa que cuente la cantidad de palabras en una oración ingresada por el usuario.

frase = input('Escribe una frase para contar las palabras: ')

palabras = frase.split()
i = 0
for palabra in palabras:
  i += 1
  
print('Numero de palabras:', i)