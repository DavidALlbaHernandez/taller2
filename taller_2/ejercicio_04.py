"""
Entradas
compra1-->float-->c1
salidas
descuento-->float-->d1
total-->float-->total
"""
#entrada
c1=float(input("ingrese dato de compra: "))
#caja negra
d1= (c1*0.15)
total=(c1-d1)
#salidas
print("el descuento es: "+str(d1)," total a pagar: "+str(total))