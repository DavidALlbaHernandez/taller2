"""
Entradas
venta1-->float-->v1
venta2-->float-->v2
venta3-->float-->v3
sueldobase-->float-->sb
salidas
comision-->float-->c
total-->float-->total
"""
#entrada
v1=float(input("ingrese la venta 1: "))
v2=float(input("ingrese la venta 2: "))
v3=float(input("ingrese la venta 3: "))
sb=float(input("ingrese duelo base: "))
#caja negra
c=(v1+v2+v3/3)*0.10
total=sb+c
#salidas
print("la comsion es: "+str(c),"sueldo total: "+str(total))

