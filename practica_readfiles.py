import msvcrt
print("Script para leer archivos")
print()
print()
# Para abrir un archivo en python necesitas
# Primer argumento:Ruta al archivo
# O nombre si esta junto al script
# Segundo: Permisos de lectura "read"
archivo=open('readme.txt','r')

"Leer linea * linea"
for linea in archivo:
	print(linea)
	pass
archivo.close()
msvcrt.getch()