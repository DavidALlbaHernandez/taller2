"""
Entradas
nombre-->input-->nombre
hijos-->int-->hij
sueldobase-->int-->slb
horastrabajadas-->int-->hrst
horasextras-->int-->hrsx
salidas
totaldeducciones-->int-->deducciones
totaltotalasignaciones-->int-->asignaciones
sueldoneto-->int-->sueldoneto
"""
#entrada
nombre=(input("ingrese su nombre: "))
hij=int(input("digite numero de hijos: "))
slb=int(input("ingrese su sueldo base: "))
hrst=int(input("ingrese horas trabjadas: "))
hrsx=int(input("ingrese horas extras realizdas: "))
#caja negra
dia=(slb/31)
hrs=(dia/8)
sueldo=(hrs*hrst)
horex=(hrsx*0.25)
hex=(horex+hrs)
dparof=(slb*0.05)
politicahab=(slb*0.02)
cajadeahorro=(slb*0.07)
deducciones=(dparof+politicahab+cajadeahorro)
asignaciones=(250.000+(173.000*(hij))+180.000)
sueldoneto=((sueldo+asignaciones+hex)-deducciones)
print("las deducciones son: "+str(deducciones))
print("las asignaciones son: "+str(asignaciones))
print("su sueldo neto es: "+str(sueldoneto))
