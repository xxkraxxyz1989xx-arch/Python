equipo={
    "valeria": 100,
    "franco": 100,
    "jhon": 20,
    "luis": 75
}
nombre=input("ingrese su nombre: ")
intensidad=float(input("del 1 al 100 que tan intensa a sido tu vida? "))
def entrenar(energia_actual,intensidad):
    energia=energia_actual-intensidad
    if energia<0:
        energia=0
    return energia
if nombre in equipo:
    energia_vieja=equipo[nombre]
    energia_nueva=entrenar(energia_vieja,intensidad)
    equipo[nombre]=energia_nueva
    print(f"{nombre} tenia antes {energia_vieja} de energia y ahora tiene {energia_nueva} de energia")
    if energia_nueva==0:
        print(f"...la vida fue muy intensa para {nombre}...")
else:
    print(f"{nombre} no está en el equipo")