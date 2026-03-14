#una estructura de datos compuesta es donde puedes guardar muchos datos simples dentro de una sola variables, y puedes acceder a cada uno de esos datos individuales usando un indice o una clave, dependiendo del tipo de estructura de datos que estes usando
#las mas comunes son las listas, diccionarios, conjuntos y las tuplas

#listas: son una coleccion ordenada de elementos, que pueden ser de cualquier tipo de dato, y se escriben entre corchetes []
#diccionarios: son una coleccion de pares clave-valor, donde cada clave es unica, y se escriben entre llaves {}
#conjuntos: son una coleccion de elementos unicos, que no tienen un orden, y se escriben entre llaves {}
#tuplas: son una coleccion ordenada de elementos, que pueden ser de cualquier tipo de dato, pero a diferencia de las listas, las tuplas son inmutables, es decir, no se pueden modificar despues de ser creadas, y se escriben entre parentesis ()

lista=[1,2,3,"signo",True,12.5]

#en una lista, cada elemento tiene un indice, que empieza desde 0, y puedes acceder a cada elemento usando su indice, por ejemplo, para acceder al primer elemento de la lista, usarias lista[0], para acceder al segundo elemento, usarias lista[1], y asi sucesivamente

diccionario={"nombre":"juan","edad":25,"altura":1.75,"es_estudiante":True}

#en un diccionario, puedes acceder a cada valor usando su clave, por ejemplo, para acceder al valor asociado con la clave "nombre", usarias diccionario["nombre"], para acceder al valor asociado con la clave "edad", usarias diccionario["edad"], y asi sucesivamente
#tambien se puede escribir asi:

diccionario2={
    "nombre":"juan",
    "edad":25,
    "altura":1.75,
    "es_estudiante":True
}

conjunto={1,2,3,"signo",True,12.5}

#en un conjunto, no puedes acceder a los elementos usando un indice o una clave, ya que los conjuntos no tienen un orden, y no permiten elementos duplicados, por lo que si intentas agregar un elemento que ya existe en el conjunto, simplemente no se agregara

tupla=(1,2,3,"signo",True,12.5)

#en una tupla, cada elemento tiene un indice, que empieza desde 0, y puedes acceder a cada elemento usando su indice, por ejemplo, para acceder al primer elemento de la tupla, usarias tupla[0], para acceder al segundo elemento, usarias tupla[1], y asi sucesivamente
#pero a diferencia de las listas, las tuplas son inmutables, es decir, no se pueden modificar despues de ser creadas, por lo que no puedes agregar, eliminar o cambiar elementos en una tupla, a diferencia de las listas, donde si puedes modificar los elementos despues de ser creadas12