mascota={
    "nombre":"Firulais",
    "especie":"perro",
    "edad":3
}
print(f"mi mascota es un {mascota['especie']}, llamado {mascota['nombre']} y tiene {mascota['edad']} años")


#otro codigo por que estamos jovenes


edad={
    "reinaldo":15,
    "maria":14,
    "valeria":14
}
print(f"valeria tiene {edad['valeria']}")
edad["gemini"]=1
print(edad)


#mini reto


receta={
    "huevos":2,
    "leche":1,
    "flores":12,
    "muchos colores":3
}
receta["muchos colores"]=255
del receta["flores"]
print(receta)