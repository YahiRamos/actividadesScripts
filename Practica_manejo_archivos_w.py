
#_*_ coding: utf8 _*_
#
#ESTOS SON LAS FUNCIONES PARA ESCRIBIR,LEER Y AGREGAR DATOS A UN ARCHIVO
#
#w:Write
#a:Append
#r:Read
#
archivo = open("File_1.txt","w")
nombre = (input("Escriba aqui su nombre: "))
edad = (input("Escriba aqui su edad: "))
###############################################
###############################################
archivo.write(nombre)
archivo.write(edad)
archivo.close()

