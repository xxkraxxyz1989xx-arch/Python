precio=50
cantidad=int(input("buenas, cuantas pociones va a comprar? "))
total=precio*cantidad

if cantidad>=10:
    total=total*0.80
    print("tienes un descuento del 20%")
print(f"el total de su compra seria: {total}")