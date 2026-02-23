oro=100
bolsa=[]
eleccion=""
while eleccion!="salir":
    print(f"---TIENDA (oro actual: {oro})")
    print("1. pocion (30)")
    print("2. escudo (50)")
    print("3. antorcha (15)")
    eleccion=input("que desea comprar? (o escriba salir)").lower()
    if eleccion=="pocion":
        if oro>=30:
            oro-=30
            bolsa.append("pocion")
        else:
            print("no tienes el oro suficiente")
    elif eleccion=="escudo":
        if oro>=50:
            oro-=50
            bolsa.append("escudo")
        else:
            print("no tienes el oro suficiente")
    elif eleccion=="antorcha":
        if oro>=15:
            oro-=15
            bolsa.append("antorcha")
        else:
            print("no tienes el oro suficiente")
for item in bolsa:
    print(f"llevas - {item}")
print(f"oro restante: {oro}")