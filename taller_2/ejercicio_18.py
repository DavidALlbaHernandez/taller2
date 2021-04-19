"""
Entradas
prestamo->int-->capital
tasa de intres->float-->razon
años a revizar-->int-->tiempo
salidas
% cobrado-->float-->intereses
"""
#entrada
capital=int(input("ingrese valor del prestamo en Bs: "))
razon=float(input("ingrese el % de la tasa de interes: "))
tiempo=int(input("dijite numero de años correspondiente a revizar: "))
#caja negra
intereses=((capital*(tiempo)*(razon/100))/(100*4))
#salidas
print("el porcentaje cobrado en la cantidad de años es: ""{:.2F}".format(intereses))