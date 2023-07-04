import msvcrt
#¿Que es una funcion lambda?
"En python las funciones anonimas son funciones que son creadas sin un nombre en especifico."
"Las funciones normales son definidas con la palabra clave def, mientras que las funciones anonimas se crean con lambda"
"por eso tambien se les conoce como funciones lambda"
#########################################################################################################################
#Sintaxis
#definicion de funcion anonima     Argumentos            Cuerpo de la función        
#lambda                            x:                    x+1                           (lambda x: x+1)
#########################################################################################################################
#Script para demostrar uso de funciones lambda
#Lista simple del 1-10
lista=[1,2,3,4,5,6,7,8,9,10]

#Se crea una nueva lista usando map para elevar
#Cada elemento a alguna potencia n
lista_m=list(map(lambda x: x**2,lista)) 

#Ver lista nueva
print(lista_m)
print("##################################################")

#Lista simple del 1-10
lista=[1,2,3,4,5,6,7,8,9,10]

#Asignacion lambda a una funcion
m_a_2=lambda x:x > 2

#Uso  de la fucion filtro con la función lambda 
#solo filtrara los elementos mayores a 2
lista_f=list(filter(m_a_2,lista))

#Ver lista nueva
print(lista_f)
