import sys
import timeit

#Ejercicio 0
def ejercicio0():
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
    
#ejercicio0()

#Ejercicio 1
def ejercicio1():
    set = {3,9,2,1}
    numeroMayor = 0
    numeroMenor = 10000
    for numero in set:
        if numero > numeroMayor:
            numeroMayor = numero
        elif numero < numeroMenor:
            numeroMenor = numero
    print('El numero mayor es : ', numeroMayor)
    print('El numero menor es : ', numeroMenor)
    
#ejercicio1()

#Ejercicio 2
def ejercicio2():
    set = {3,9,2,1}
    print('Longitud del conjunto -- ',len(set))
    
#ejercicio2()

#Ejercicio 3
def ejercicio3():
    set = {"hola", "vamos", "a", "buscar", "valor", "en", "el", "conjunto"}
    print('¿La palabra - vamos - se encuentra en el conjunto? - ', "valor" in set)

#ejercicio3() 

#Ejercicio 4
def ejercicio4():
    set1 = {"valor1", "valor2", "valor3"}
    set2 = {"valor6", "valor4", "valor3"}
    
    if set1.isdisjoint(set2):
        print('No tienen elementos en comun')
    else:
        set1.intersection_update(set2)
        print('Valores en comun -- ', set1)
        
#ejercicio4()

#Ejercicio 5
def ejercicio5():
    x = {1,2,3}
    y = {2,3}
    
    if x.issuperset(y):
        print('El conjunto x es un subconjunto de y')
    else:
        print('El conjunto x no es un subconjunto de y')

#ejercicio5()

#Ejercicio 6
def ejercicio6():
    set = {"valor1","valor2","valor3"}
    print(set)
    
    valorAbuscar = input('Escribe el valor que quieres buscar: ')
    if valorAbuscar in set:
        print('Si que esta el valor.')
    else:
        print('No que esta el valor.')
        
#ejercicio6()

#Ejercicio 7
def ejercicio7():

    set1 = {1, 2, 3, 4, 5}

    set2 = {3, 4, 5, 6, 7}

    set1.difference_update(set2)

    print("Primer conjunto despues de eliminar la interseccion :", set1)
    
#ejercicio7()

#Ejercicio 8
def ejercicio8():
    set = {3,9,2,1,10,13}
    numeroMayor = 0
    for numero in set:
        if (numero%2) == 0:
            if numero > numeroMayor:
                numeroMayor = numero
    print('El numero mayor es : ', numeroMayor)
    
#ejercicio8()

#Ejercicio 9
def ejercicio9():
    set1 = {1,2,3,4}
    set2 = {3,4,5,6}
    
    set1.symmetric_difference_update(set2)
    print(set1)
    
#ejercicio9()

#Ejercicio 10
def ejercicio10():
    listaPalabras = ["hola", "portugues", "cosa", "asoc", "prueba"]
    grupoAnagramas = {}
    
    for palabra in listaPalabras:
        palabraOrdenada = ''.join(sorted(palabra))
    
        if palabraOrdenada not in grupoAnagramas:
            grupoAnagramas[palabraOrdenada] = []
            
        grupoAnagramas[palabraOrdenada].append(palabra)
            
    for grupo in grupoAnagramas:
        print(grupo)
        
ejercicio10()