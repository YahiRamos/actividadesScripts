import msvcrt
print("Contador de palabras")
print()
"Leer documento completo"
archivo = open('readme.txt','r')
print()
#Contador de palabras
palabras=0
for linea in archivo:
	#Divide cada linea en una lista
	#de palabras y las cuenta
	palabras+=len(linea.split())
	#Total de palabras
	print(palabras)
	pass
archivo.close()
msvcrt.getch()