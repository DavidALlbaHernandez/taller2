"""
Entradas
edad1-->int-->dato1
edad2-->int-->dato2
edad3-->int-->dato3
salidas
promedio-->int-->c
"""
#entrada
dato1=int(input("ingrese la edad 1: "))
dato2=int(input("ingrese la edad 2: "))
dato3=int(input("ingrese la edad 3: "))
#caja negra
c=((dato1+dato2+dato3)/3)
#salidas
print("el promedio es: "+str(c))