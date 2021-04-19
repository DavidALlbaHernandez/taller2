"""
Entradas
presupuestoanual->int-->panual
salidas
ginecologia->int-->gin
traumatologia-->int-->trau
pediatria-->int-->pedi
"""
#entrada
panual=int(input("digite presupuesto anual: "))
#caja negra
gin=(panual*0.4)
trau=(panual*0.30)
pedi=(panual*0.30)
#salidas
print("dinero a recibir en el area de ginecologia: ""{:.0F}".format(gin))
print("dinero a recibir en el area de traumatologias: ""{:.0F}".format(trau))
print("dinero a recibir en el area de pediatria: ""{:.0F}".format(pedi))
