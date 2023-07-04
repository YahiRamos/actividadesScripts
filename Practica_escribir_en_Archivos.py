import msvcrt
print("Escribir archivos")
print()
Archivo=open("base de datos.txt","w")
Archivo.write("Hola mundo")
Archivo.close()
msvcrt.getch()