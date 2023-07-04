import msvcrt
print("LISTA POR COMPRENSION")
print()
#Sintaxis  operacion + estructura de un ciclo normal + condicion(opcional)
#Ejemplo [x*2 for x in range(10) if x < 5]
#Comparacion entre una lista normal y una lista por comprension
#CON COMPRENSION DE LISTAS
Pares=[x for x in range(101) if x % 2 == 0]
print("Estos son Numeros par")
print(Pares)
Inpares=[x for x in range(101) if x % 2 != 0]
print("Estos son numeros inpar")
print(Inpares)
msvcrt.getch()