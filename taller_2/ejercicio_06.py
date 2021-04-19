"""
Entradas
mujeres-->int-->tem
hombres-->int-->teh
salidas
%hombres-->int-->ph
%mujeres-->int-->pm
"""
#entrada
tem=int(input("ingrese catidad de estudiantes mujeres: "))
teh=int(input("ingrese catidad de estudiantes hombres: "))
#caja negra
te=(tem+teh)
ph=((100*teh)/te)
pm=((100*tem)/te)
print("el porcentaje de estudiantes mujeres es: es: "+str(ph),"el porcentaje de estudiantes hombres es: "+str(pm))