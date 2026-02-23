compras = ["pan", "leche", "huevos", "frutas", "chocolate"]

print("mi lista de compras:")
for articulo in compras:
    print(f"- {articulo}")
    
    
#otro codigo


mochila=[]
objeto=input("¿que objeto quieres agregar a tu mochila? ")
while objeto.lower()!="salir":
    mochila.append(objeto)
    print(f"se ha guardado {objeto} en su mochila")
    objeto=input("que objeto quieres agregar a tu mochila? (o escriba salir para terminar)")
for item in mochila:
    print(f"- {item}" )