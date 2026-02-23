ca=5
while ca>0:
    print(ca)
    ca=ca-1
print("ignicion")


#otro codigo por que aja


mensaje=""
while mensaje!="parar":
    mensaje=input("escriba algo: ")
    if mensaje!="parar":
        print(f"el loro dice: {mensaje}")


#mini reto


s=100
o=""
while o!="salir" and s>0:
    print(f"su saldo actual es {s}")
    o=input("cuanto desea retirar? (o puede escribir salir para terminar)")
    if o!="salir":
        r=int(o)
        s=s-r
print("gracias por usar el cajero")