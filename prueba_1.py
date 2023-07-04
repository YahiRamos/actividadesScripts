import msvcrt
print("Prueba 1")
#intentaremos crear un programa con sentencias
print("Se solicitaran 2 numeros y se comparara cual es mayor")
print()
v1=int(input("Ingrese El Primer Número: "))
v2=int(input("Ingrese El Segundo Número: "))
if v1<v2:
	print("El Primer Numero es Menor al Segundo")
	pass
elif v1>v2:
	print("EL Primer Numero es Mayor al Segundo")	
	pass

msvcrt.getch()
