#EJERCICIO 1
def ejercicio1():
    numeroCorreto = False
    while not numeroCorreto:
        try:
            # get keyboard input (string)
            rawInput = input('Enter number:')
            # convert string to integer
            x = int(rawInput)
            # calculate number squared
            print(x*x)
            #Cambiamos booleano para que no entre al bucle
            numeroCorreto = True
        except ValueError:
            print('Tiene que ser un numero.')

#ejercicio1()

#EJERCICIO 2
def ejercicio2():
    lista = ["Julen", "Juan", "Lucas", "Marta"]
    try:
        for x in range(10):
            print(lista[x])
    except:
        print('La lista ha terminado.')
        
#ejercicio2()

#EJERCICIO 3
def ejercicio3():
    #Ejecutando el codigo nos salta la exception por terminal
    #Lo ideal es capturar exactamente la excepcion que salta con el try
    try:
        r = 34/0
        print(r)
    except ZeroDivisionError:
        print('No se puede dividir entre 0.')
    
    #Ejecutando el codigo nos salta la exception por terminal
    #Lo ideal es capturar exactamente la excepcion que salta con el try
    try:
        patata = 5 + 'Enter number:'
    except TypeError:
        print('No se puede sumar un String y un entero')
    
    
#ejercicio3()

#EJERCICIO 4
def ejercicio4():
    try:
        r = 34/cosa
        fichero = open(calabaza)
        patata= mi_lista[15] +'Enter number:'
        print(fichero.read())
    except Exception as e:
        print(f'Ha saltado la excecion {e}')

#ejercicio4()
