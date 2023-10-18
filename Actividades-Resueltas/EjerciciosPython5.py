import timeit
import sys

mytuple = (1,3,4,5,"hello", True)
mylist = [1,3,4,5,"hello", True]

def unirTupla(tupla):
    cadena = ""
    for i in tupla:
        cadena += str(i)
    
    return cadena

def unirLista(lista):
    cadena = ""
    for i in lista:
        cadena += str(i)
    
    return cadena

tiempoForTuple = timeit.timeit(lambda: unirTupla(mytuple), number=100000)
tiempoForLista = timeit.timeit(lambda: unirLista(mylist), number=100000)

print('Tiempo de recorrer la tupla con for: ', tiempoForTuple)
print('Tiempo de recorrer la lista con for: ', tiempoForLista)

print()
tiempoJoinTuple = timeit.timeit(lambda: "".join(map(str, mytuple)), number=100000)
tiempoJoinLista = timeit.timeit(lambda: "".join(map(str, mylist)), number=100000)

print('Tiempo de recorrer la tupla con join: ', tiempoJoinTuple)
print('Tiempo de recorrer la lista con join: ', tiempoJoinLista)

print()
tamanoTuple = sys.getsizeof(mytuple)
tamanoLista = sys.getsizeof(mylist)

print('Tamaño en memoria de la tupla : ', tamanoTuple)
print('Tamaño en memoria de la lista : ', tamanoLista)