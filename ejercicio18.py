#Ejercicio 18: Contador de Palabras
#Crea un programa que cuente la cantidad de palabras en una oración ingresada por el usuario.

frase = input('Escribe una frase para contar las palabras: ')

palabras = frase.split()
cantidad_palabras = len(palabras)
print(f"La cantidad de palabras es {cantidad_palabras}")