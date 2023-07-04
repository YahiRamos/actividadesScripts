import msvcrt
print("LISTA NORMAL")
print()
#Comparacion entre una lista normal y una lista por comprension

#Lista normal
#Lista para guardar los datos
Pares=[]
Inpares=[]
#iteracion del 0 al 10
for x in range(11):
	#Si el residuo es 0 es par
	if x % 2 == 0:
		print("Estos numeros son pares")
		Pares.append(x)
		print(Pares)
		pass
	elif x % 2 != 0:
		print("Estos numeros son Inpares")
		Inpares.append(x)
		print(Inpares)
	pass	
msvcrt.getch()
