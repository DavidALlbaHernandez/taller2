"""
Entradas
cantidad de naranjas->int-->X
precio docena de naranjas-->int-->T
valor de la venta-->int-->K
salidas
% ganancias-->float-->porcentaje
"""
#entrada
X=int(input("Ingrese cantidad de Lotes de naranjas: "))
T=int(input("Ingrese Precio por Docenas de naranja: "))
K=int(input("Ingrese Precio por Docenas de naranjar: "))
#caja negra
NumDoc=(X/12)
Costo=(T*NumDoc)
Ganancia=(K-Costo)
Porcentaje=((Ganancia*100)/Costo)
#salidas
print("El porcentaje de Ganancias es: ""{:.2F}".format(Porcentaje))
