"""
Entradas
galonesurtidoso->int-->gal
salidas
litrosurtidos->float-->GasL
totalapagar-->int-->precioL
"""
#entrada
gal=int(input("registre cantidad de galones surtidos: "))
#caja negra
GasL=(gal*3.785)
precioL=(GasL*50000)
#salidas
print("cantidad de litros surtidos: ""{:.3F}".format(GasL))
print("total a pagar: "+str(precioL))