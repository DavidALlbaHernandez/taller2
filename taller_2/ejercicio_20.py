"""
Entradas
precio del computador->int-->recio
cuotas mensuales-->int-->cuotas
% de recargo-->float-->recargo
salidas
% ganancias-->float-->porcentaje
"""
#entrada
precio=int(input("ingrese precio del articulo: "))
cuotas=int(input("ingrese cantidad de cuotas mensuales: "))
recargo=float(input("ingrese el % del recargo: "))
#caja negra
vmensual=(precio/cuotas)
vrecargo=((vmensual)*(recargo/100))
valorcuota=(vmensual+vrecargo)
valorcuo=(valorcuota*cuotas)
pvcuota=((precio*100)/valorcuo)
#salidas
print("porcentaje a cobrar en la cantidad de cuotas es: ""{:.2F}".format(pvcuota))
