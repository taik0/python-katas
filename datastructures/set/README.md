# Implementacion de estructura de datos Set
implementa el set más básico q se te ocurra y calcula el coste computacional en tiempo y espacio
analiza la diferencia entre el coste en tiempo para leer y para chequear si un elemento exite en el set
reduce el coste en tiempo del lookup
reduce el coste en espacio del lookup
pasa los costes a algo constante sacrificando exactitud y a partir de ese estudio inicial, empieza a analizar técnicas de hashing para hacer búsquedas y escrituras en O(1) y estructuras de datos q te permitan pasar el tamaño a O(1) la secuencia de estructuras q deberías revisar es:
listas, mapas/diccionarios, btrees, bitsets, funciones de hashing, filtros de bloom

Picar 5 versiones diferentes de esa misma interfaz
cada una intentando mejorar alguno de los defectos de la anterior

## Tipo de implementación


1: usando una lista (sin evitar repiticiones)
2: usando una lista de elementos únicos
3: usando un mapa/diccionario/set
4: usando un bitset
5: usando un filtro de bloom (https://llimllib.github.io/bloomfilter-tutorial/)

## Interfaz

Add(element)
Size()
Contains(element)
