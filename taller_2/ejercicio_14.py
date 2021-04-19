"""
Entradas
mesanterior->int-->mesant
kwhmesanterior-->float-->kwhgas
kwhmesactual-->float-->kwsact
salidas
total-->int-->dinerototal
"""
#entrada
mesant=int(input("ingrese monto pagado en el mes anterior: "))
kwhgas=float(input("digite kWh Gastados en el mes anterior: "))
kwsact=float(input("ingrese lectura actual de kWh: "))
#caja negra
precio1kwh=(kwhgas/mesant)
pagoactual=(precio1kwh*kwsact)
#salidas
print("el monto total a pagar es: ""{:.0F}".format(pagoactual))
