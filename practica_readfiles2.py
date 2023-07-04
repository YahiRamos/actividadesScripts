import msvcrt
print("Script para leer archivos 2")
print()
"Leer documento completo"
archivo = open('readme.txt','r')
contenido = archivo.read()
print(contenido)
archivo.close()


msvcrt.getch()