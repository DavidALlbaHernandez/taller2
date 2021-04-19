"""
Entradas
Chelines-->int-->CA
Dracmas-->int-->DG
Pesetas-->int-->P
salidas
CA-->int-->P
DG-->int-->FrancoFrances
P-->int-->Dolares
P-->int-->LirasItalianas
"""
#entrada
CA=int(input("Ingrese la cantidad de Chelines Austriacos a cambiar: "))
DG=int(input("Ingrese la cantidad de Dracmas Griegos a cambiar: "))
P=int(input("Ingrese la cantidad de pesetas a cambiar: "))
#caja negra
Pesetas=(CA*956871)/100
FrancoFrances=((DG*88607)/100)*(1/20110)
Dolares=P/122499
LirasItalianas=(P*100)/9289
print("La cantidad de Chelines Austriacos a Pesetas es: ""{:.0F}".format(Pesetas))
print("La cantidad de Dracmas Griegos a Franco Frances es: ""{:.0F}".format(FrancoFrances))
print("La cantidad de Pesetas a Dolares es: ""{:.0F}".format(Dolares))
print("La cantidad de Pesetas a Liras Italianas es: ""{:.0F}".format(LirasItalianas))
