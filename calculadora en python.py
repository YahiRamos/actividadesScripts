import msvcrt
print ("Programa de Calculadora")
print ()
#estas son operaciones
print("menu")
print("1.-Suma")
print("2.-Resta")
print("3.-Multiplicación")
print("4.-División")
print("5.-Exponenciación")
print("6.-Raiz")
print()
z=int(input("Introduce el número de la operacion que quieres efectuar:\n "))
print()
print("Se pediran 2 Numeros para que se efectuen las operaciones")
print()
x=int(input("Introduce el primer numero:\n "))
y=int(input("Introduce el segundo numero:\n "))
if z==1:
	print("El resultado de la Suma es:" ,x+y)
	pass
elif z==2:
	print("El resultado de la Resta es:" ,x-y)
	pass
elif z==3:
 	print("El resultado de la Multiplicacion es:" ,x*y)
 	pass
elif z==4:	
	print("El resultado de la Division es:" ,x/y)
	pass
elif z==5:	
	print("El resultado de la Exponenciacion es:" ,x**y)
	pass
elif z==6:	
	print("El resultado de la Raiz es:" ,x**(1/y))
	pass
print()
print("Hecho por Yahir Ramos ")
msvcrt.getch()
