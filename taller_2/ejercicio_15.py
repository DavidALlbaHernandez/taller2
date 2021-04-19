"""
Entradas
preciodelproducto->int-->PDP
preciofinalproducto-->int-->PFP
salidas
%aplicado->float-->DESC
dineroahorrado-->int-->PC
"""
#entrada
PDP=int(input("Ingrese Precio del Producto: "))
PFP=int(input("Ingrese Precio Final Pagado por el Productor: "))
#caja negra
DESC=((PFP*100)/PDP)
PC=(PDP-PFP)
#salidas
print("El Porcentaje Aplicado es: ""{:.2F}".format(DESC))
print("El Dinero Ahorrado: "+str(PC))