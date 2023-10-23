import sys
import timeit

#Ejercicio 0
lista = ["hola", "valor1", "valor2"]
tupla = ("hola", "valor1", "valor2")
set = {"hola", "valor1", "valor2"}

print('Orden de mayor a menor tamaño: ')

if sys.getsizeof(lista) > sys.getsizeof(tupla):
    if sys.getsizeof(lista) > sys.getsizeof(set):
        print("1. Lista.")
        if sys.getsizeof(tupla) > sys.getsizeof(set):
            print("2. Tupla.\n3. Set.")
        else:
            print("2. Set.\n3. Tupla.")
    else:
        print("1. Set.\n2. Lista.\n3. Tupla.")
elif sys.getsizeof(tupla) > sys.getsizeof(set):
    print("1. Tupla.")
    if sys.getsizeof(lista) > sys.getsizeof(set):
        print("2. Lista.\n3. Set.")
    else:
        print("2. Set.\n3. Lista.")

tiempoJuntarListas = timeit.timeit(lambda: lista + lista, number=10000000)
tiempoJuntarTuplas = timeit.timeit(lambda: tupla + tupla, number=10000000)
tiempoJuntarSet = timeit.timeit(lambda:  set.union(set),number=10000000)

print('Tiempo de juntar listas -- ', tiempoJuntarListas)
print('Tiempo de juntar tuplas -- ', tiempoJuntarTuplas)
print('Tiempo de juntar set -- ', tiempoJuntarSet)



