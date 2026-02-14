edad=int(input("dijite su edad:"))
ciudad=input("escriba la ciudad donde actualmente vive:")

print(f"tienes {edad} y vives en {ciudad}")
print(f"y el preximo año tendras {edad + 1} años")


#otro codigo por que asi es la vida


precio=1000
impuesto=precio*0.15
total=precio+impuesto
print(f"el precio de este producto es {precio} mas los impuestos en total seria: {total}")


#otro codigo por que si


Edad=int(input("digame su edad:"))
if Edad==100:
    print("adelante, puede pasar")
elif Edad>=18:
    print("wow, invitacion especial por ser centenario")
else:
    print("lo siento, no puede pasar")