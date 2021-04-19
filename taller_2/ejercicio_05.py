"""
Entradas
calificacion1-->float-->c1
calificacion2-->float-->c2
calificacion3-->float-->c3
examenfinal-->float-->ex1
trabajofinal-->float-->tra1
salidas
calificacionfinal-->float-->fin1
"""
#entrada
c1=float(input("ingrese calificacion 1: "))
c2=float(input("ingrese calificacion 2: "))
c3=float(input("ingrese calificacion 3: "))
ex1=float(input("ingrese calificacion del examen final: "))
tra1=float(input("ingrese calificacion del  trabajo final: "))
#caja negra
calificacionparcial=((c1+c2+c3)/3)*0.05
examenfinal=(ex1*0.0)
trabajofinal=(tra1*0.15)
calificaciontotal=(calificacionparcial+examenfinal+trabajofinal)
#salidas
print("su calificación final en la materia de Algoritmos es: "+str(calificaciontotal))