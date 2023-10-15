#EJERCICIO 1
def ejercicio1():
    lista = ["Matemáticas","Física","Química","Historia","Lengua"]
    notas = []
    sumaNotas = 0
    for asignatura in lista:
        nota = float(input('Escribe la nota de la asignatura ' + asignatura +": "))
        notas.append(nota)
        sumaNotas = sumaNotas + nota
    for cont in range(len(lista)):
        print('ASIG -- ', lista[cont], ', NOTA -- ', notas[cont])
        
    print('La media es : ', sumaNotas/len(lista))
    
#ejercicio1()

#Ejercicio 2
def ejercicio2():
    palabra = input('Escribe una palabra : ')
    
    if palabra == palabra[::-1]:
        print('Es palindromo')
    else :
        print('No es palindromo')

    print('-Cantidad de letra a : ', palabra.count('a'))
    print('-Cantidad de letra e : ', palabra.count('e'))
    print('-Cantidad de letra i : ', palabra.count('i'))
    print('-Cantidad de letra o : ', palabra.count('o'))
    print('-Cantidad de letra u : ', palabra.count('u'))
    
#ejercicio2()

#EJERCICIO 3
def ejercicio3():
    carta = {
        "Pasta":{"Espaquetis": 7, "Macarrones": 7, "Fusili": 8},
        "Salsa":{"Carbonara": 3, "Rabiosa": 2, "Pesto verde": 2.75, "Pesto rojo": 3, "boloñesa": 2.5},
        "Pizza":{"Clasica": 8, "Integral": 9}
    }
    ingredientes = {
        "Extra queso": 1,
        "Queso azul": 2,
        "Salchica": 1.5,
        "Carne": 2,
        "Chorizo": 2.5,
        "Jamon": 3,
        "Pimiento verde": 1,
        "Aceitunas": 1.5,
        "Anchoas": 3,
        "Atun": 2.5,
        "Salmon": 3,
        "Piña": 1.5,
    }
    postres = {
        "Tiramisu": 6,
        "Panna Cotta": 5.5
    }
    
    totalPrecio = 0
    
    pedido = input('Escribe si quieres pasta o pizza : ').lower()
    if pedido == "pasta":
        print('Carta : \n', carta["Pasta"])
        pedido = input('Elige que pasta quieres : ')
        if pedido in carta["Pasta"]:
            totalPrecio += carta["Pasta"][pedido]
            print('Carta : \n', carta["Salsa"])
            pedido = input('Escribe la salsa que quieras :')
            if pedido in carta["Salsa"]:
                totalPrecio += carta["Salsa"][pedido]
            else:
                print('NO TENEMOS ESA SALSA O ESTA MAL ESCRITO')
        else:
            print('NO TENEMOS ESA PASTA O ESTA MAL ESCRITO')
    elif pedido == ("pizza"):
        print('Carta : \n', carta["Pizza"])
        pedido = input('Elige que Pizza quieres : ')
        if pedido in carta["Pizza"]:
            totalPrecio += carta["Pizza"][pedido]
            print('Escribe 5 ingredientes para la pizza \n', ingredientes)
            for contador in range(5):
                print (contador + 1 + " ")
                pedido = input('Ingrediente : ')
                if pedido in ingredientes:
                    totalPrecio += ingredientes[pedido]
                else:
                    print('ESTE INGREDIENTE NO EXISTE O ESTA MAL ESCRITO')     
    else: 
        print('No existe esa opcion')
        
    print('Postres : \n', postres)
    pedido = input('Escribe el postre que quieras : ')
    if pedido in postres:
        totalPrecio += postres[pedido]
    else:
        print('EL POSTRE ES INCORRECTO')
        
    print('El Precio de la mesa es : ',totalPrecio)
    
#ejercicio3()