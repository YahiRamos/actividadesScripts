import msvcrt
import os
print(">>>>>>> Programa de Registro de Alumnos y Calificaciones <<<<<<<")
print()
print("Introduzca El Núnero de Alumnos")
print()
print("Se le Pediran los Datos de Alumnos Junto a sus Calificaciones")
#Empiezan los datos de entrada
#A= variable que toma el numero de alumnos
#Esta variable se usara en el ciclo for para el # de repeticiones
E=open("base de datos.txt","w")
Res=()
A=int(input("Introduzca el Numero de Alumnos: "))
for x in range(A):
	#entrada de datos como nombre apellidos y calificaciones
	#para despues Guardarlos en un archivo .txt
	Na=input("Introduzca el Nombre del Alumno: ")
	print()
	Ap=input("Introduzca el Apellido Paterno del Alumno: ")
	print()
	Am=input("Introduzca el Apellido Materno del Alumno: ")
	print()
	Ca=input("Introduzca la Calificacion  del Alumno: ")
	print()
	Res=("Alumno: " + Na + " " + Ap + " " + Am + " " + "Calificacion: " + Ca)
	E.write(Res +"\n")
	pass

msvcrt.getch()
E.close()
#Condicional para preguntar si quieres ver los Datos guardados
P=input ("¿Deseas Ver Los Datos Guardados?" + "s/n :")
if P=="s":
	os.startfile("base de datos.txt")
	pass
else:
	print("Hasta La Proxima :)")
	pass
msvcrt.getch()	