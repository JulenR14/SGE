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

#Ejercicio 5
def ejercicio5(matriz1, matriz2):
    try:
        filasMatriz1 = len(matriz1)
        columnasMatriz1 = len(matriz1[0])
        filasMatriz2 = len(matriz2)
        columnasMatriz2 = len(matriz2[0])
        
        if columnasMatriz1 != filasMatriz2:
            raise Exception
        
        resultado = [[0 for i in range(columnasMatriz2)] for j in range(filasMatriz1)]

        
        for i in range(filasMatriz1):
            for j in range(columnasMatriz2):
                for k in range(columnasMatriz2):
                    resultado[i][j] += matriz1[i][k] * matriz2[k][j]
                    
                    
        print(resultado)
    except Exception:
        print('Las matrices no se pueden calcular...')
        
#ejercicio5(((1, 2, 3), (3, 2, 1)), ((1, 2), (3, 4), (5, 6)))

#EJERCICIO 6
def ejercicio6():
    tablero = [[' ' for i in range(3)] for j in range(3)]
    jugador_actual = 'X'
    movimientos = 0
    
    while movimientos < 9:
        for fila in tablero:
            print(fila)

        print(f"Turno del jugador {jugador_actual}")

        try:
            resultadoFilaJugador = int(input("Introduce la coordenada Y del 1 al 3: "))
            fila = (resultadoFilaJugador - 1)
            resultadoColumnaJugador = int(input("Introduce la coordenada X del 1 al 3: "))
            columna = (resultadoColumnaJugador - 1)
            if not (0 <= fila < 3) or not (0 <= columna < 3):
                print("Coordenadas fuera de rango. Debe ser del 1 al 3.")
                continue
        except ValueError:
            print("Entrada no válida. Introduce un número del 1 al 3.")
            continue

        if tablero[fila][columna] != ' ':
            print("Esa coordenada ya está siendo utilizada, use una libre.")
            continue

        ficha = input("Introduce 0 para círculo (O) o X para cruz: ")
        if ficha not in ('0', 'X'):
            print("Entrada no válida. Debes introducir 0 o X.")
            continue

        tablero[fila][columna] = ficha
        movimientos += 1

        if (tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador_actual or
            tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador_actual or
            any(all(tablero[i][j] == jugador_actual for j in range(3)) for i in range(3)) or
            any(all(tablero[i][j] == jugador_actual for i in range(3)) for j in range(3))):
            for fila in tablero:
                print(fila)
            print(f"La partida la ha ganado el jugador con la ficha {jugador_actual}.")
            return

        if jugador_actual == 'X':
            jugador_actual = '0'
        else:
            jugador_actual == 'X'

    for fila in tablero:
        print(fila)
    print("La partida ha terminado en empate.")

ejercicio6()