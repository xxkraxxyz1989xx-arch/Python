productos={
    "pan":1000,
    "leche":4000,
    "cafe":3000
}
producto=input("que producto desea comprar? ").lower()
dinero=float(input("cuanto dinero tiene? "))
descuento=float(input("que descuento desea? "))
def calcular_precio (precio_base,descuento):
    descuento=1-(descuento/100)
    precio_final=precio_base*descuento
    return precio_final
if producto in productos:
    precio_lista=productos[producto]
    total=calcular_precio(precio_lista,descuento)
    if dinero>=total:
        cambio=dinero-total
        print(f"hecho, su cambio es: {cambio}")
        print("gracias por su compra")
    else:
        falta=total-dinero
        print(f"no te alcanza, te falta: {falta}")
else:
    print("ese producto no lo vendemos")
