"""
Entradas
metros-->float-->m
salidas
pulgadas-->float-->pul
pies-->float-->ft
"""
#entrada
m=float(input("digite dato en metros: "))
#caja negra
pul=(m*39.27)
ft=(pul*12)
print("la cantidad en pulgadas es: " +str(pul))
print("la cantidad en pies es: "+str(ft))

