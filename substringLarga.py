#!/usr/bin/env python3
import string

def buscarSubstring(cad):
	substring = ""
	listaAux = []
	substringLarga = ""
	# Quitar signos de puntuación
	cadena = ''.join([i for i in cad if i not in string.punctuation])
	nuevaCadena = cadena.split()

	# Ordenar las palabras de la string sin letras repetidas en una nueva lista
	for palabras in nuevaCadena:
		for letras in palabras:
			if letras not in substring:
				substring += letras
		listaAux.append(substring)
		substring = ""

	# Buscar en la lista creada la substring más larga
	i = 0
	for palabrasMod in listaAux:
		if len(palabrasMod) > len(substringLarga):
			substringLarga = palabrasMod
		i += 1
	return substringLarga


def main():
	cadena = input("Ingrese la cadena: ")
	print("La substring mas larga sin letras repetidas en: '{}' es: '{}' ".format(cadena,buscarSubstring(cadena)))

main()