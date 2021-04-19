"""
Entradas
sueldobase-->int-->slb
hrstrabjadasc-->float-->hrst
salidas
sueldoneto-->int-->snt
"""
#entrada
slb=int(input("ingrese sueldo base: "))
hrst=float(input("ingrese horas trabajadas: "))
#caja negra
descuento=(slb*0.2)
b=(slb-descuento)
dia=(b/30)
hrs=(dia/8)
snt=(hrs*hrst)
print("su salario neto es: ""{:.5F}".format(snt))