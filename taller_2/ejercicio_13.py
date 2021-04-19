"""
Entradas
billetesde50000->input-->N1
billetesde20000-->int-->N2
billetesde10000-->int-->N3
billetesde5000-->int-->N4
billetesde2000-->int-->N5
billetesde1000-->int-->N6
billetesde500-->int-->N7
billetesde100-->int-->N8
salidas
total-->int-->dinerototal
"""
#entrada
N1=int(input("dijite cantidad de billetes de 50000: "))
N2=int(input("dijite cantidad de billetes de 20000s: "))
N3=int(input("dijite cantidad de billetes de 10000: "))
N4=int(input("dijite cantidad de billetes de 5000: "))
N5=int(input("dijite cantidad de billetes de 2000: "))
N6=int(input("dijite cantidad de billetes de 1000: "))
N7=int(input("dijite cantidad de billetes de 500: "))
N8=int(input("dijite cantidad de billetes de 100: "))
#caja negra
dinerototal=((N1*50000)+(N2*20000)+(N3*10000)+(N4*5000)+(N5*2000)+(N6*1000)+(N7*500)+(N8*100))
#salidas
print("la cantidad de dinero en el banco es: "+str(dinerototal))
