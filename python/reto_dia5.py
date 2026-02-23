mochila={
    "roja":20,
    "azul":50,
    "verde":75
}
def usar_funcion(mochila,color):
    if color in mochila:
        return mochila[color]
    else:
        print("esa pocion no existe")
        return 0
vida_actual=10
seleccion=input("elige una pocion para usar (roja/azul/verde):").lower()
pts_curacion=usar_funcion(mochila,seleccion)
vida_actual+=pts_curacion
print(f"ahora tu vida actual es:{vida_actual}")