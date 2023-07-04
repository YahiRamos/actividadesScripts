#Desarrollado por Alvaro Yahir Ramos Alvarado
import math 
#--------------cambie los valores aqui--------------
x=1.5
cifra_significativa=3
#---------------------------------------------------
funcion = math.e**x
# formula para sacar la tolerancia (Es=0.5*10**(2-n))
def calcular_tolerancia(n):
    return 0.5 * 10 ** (2-n)

# Formula para el error relativo |valor verdadero - valor aproximado|
#                                 --------------------------------   X 100
#                                |           valor verdadero        |
def error_relativo(valor_verdadero,valor_aproximado):
    return abs((valor_verdadero-valor_aproximado)/valor_verdadero)*100

# Formula para el error aproximado   |Aproximación actual - aproximacion anterior|
#                                     -----------------------------------------    X 100
#                                    |             Aproximación actual           |
def error_aproximado(aproximacion_actual,aproximacion_anterior):
    return abs((aproximacion_actual - aproximacion_anterior)/aproximacion_actual)*100

# Formula para el error numérico
def error_numerico(valor_verdadero,valor_aproximado):
    return valor_verdadero - valor_aproximado

#primero calculamos la tolerancia
tolerancia=calcular_tolerancia(cifra_significativa)

#las primeras 2 iteraciónes estan fuera del ciclo, por que son las que mas varian
aproximacion=1
print('Iteración 1')
#primera iteración
print(f'|Er|% = {error_relativo(funcion, aproximacion)}')
print('|Ea|% = no hay ')
print('')
#segunda iteración
#guardamos la aproximación de la iteración anterior
aproximacion_anterior = aproximacion
#sumamos el siguiente valor en la sucesión (x)
aproximacion += x
print('Iteración 2')
print(f'e**{x}={aproximacion}')
print(f'|Er|% = {error_relativo(funcion, aproximacion)}%')
print(f'|Ea|% = {error_aproximado(aproximacion, aproximacion_anterior)}% ')
print('')
#aqui le ponemos "iteración" a el numero que va de exponente y factorial
#lo inicializamos en 2 porque asi nos lo dá la serie, suego aumenta 1 cada iteración
iteracion=2
#A partir de la tercera iteración lo resolvemos con un ciclo
#La condición es: mientras el error aproximado es mayor o igual a la tolerancia
#Por lo tanto, el programa termina cuando el error aproximado sea menor a la tolerancia
while(error_aproximado(aproximacion, aproximacion_anterior)>=tolerancia):
    aproximacion_anterior = aproximacion
    #sumamos el siguiente valor en la sucesión (x)
    aproximacion += x**iteracion/math.factorial(iteracion)
    print(f'Iteración {iteracion+1}')
    print(f'e**{x}={aproximacion}')
    print(f'|Er|% = {error_relativo(funcion, aproximacion)}%')
    print(f'|Ea|% = {error_aproximado(aproximacion, aproximacion_anterior)}%')
    print('')
    iteracion+=1
