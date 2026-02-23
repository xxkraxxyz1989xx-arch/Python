oro=100
nombre_jugador="kraxxyz"
cofre=["pocion","diamante","escudo"]
equipo={
    "espada":10,
    "armdura":5
}
for items in cofre:
    respuesta = input(f"{nombre_jugador} quieres recoger el/la {items}? (si/no)").lower()
    if respuesta=="si":
        equipo[items]=1
print(f"tienes {oro} de oro")
mejora=input("deseas mejorar la espada por 50 de oro? si/no:").lower()
if mejora=="si" and oro>=50:
    equipo["espada"]+=20
    print("espada mejorada")
elif mejora=="si":
    print("no tienes suficiente oro")
print("--- TU INVENTARIO FINAL ---")
for objeto, poder in equipo.items():
    print(f"->{objeto}: {poder}pts")