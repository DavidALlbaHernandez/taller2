"""
Entradas
ladoa-->float-->Lado1
ladob-->float-->Lado2
ladoc-->float-->Lado3
salidas
p-->float-->sperimetro
A-->float-->area
"""
#entrada
Lado1=float(input("Ingrese la longitud del primer lado: "))
Lado2=float(input("Ingrese la longitud del segundo lado: "))
Lado3=float(input("Ingrese la longitud del tercer lado: "))
#caja negra
sperimetro=(Lado1+Lado2+Lado3)/2
area=((sperimetro*(sperimetro-Lado1)*(sperimetro-Lado2)*(sperimetro-Lado3))**0.5)
print("El Semiperimetro es: " +str(sperimetro))
print("El Area del triangulo es: ""{:.5F}".format(area))