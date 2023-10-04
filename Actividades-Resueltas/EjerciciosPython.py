#1. Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.

def ejercicio1():
    nombre = input("Escribe tu nombre :")
    print("Tu nombre es... " + nombre + "¡")
    
#ejercicio1()

#2. Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:
#suma = n*(n+1)/2

def ejercicio2():
    numero = int(input("Escribe un numero positivo: "))
    
    total = 0
    
    if numero > 0:
        for x in range(numero):
            total = x*(x+1)/2
            
    
    else:
        print('El numero que has puesto no es positivo')
        

#ejercicio2()

def ejercicio3():
    
    cantidad = int(input('Escribe la cantidad depositada en tu cuenta de ahorros: '))
    primerA = float(cantidad + (cantidad * 0.4))
    segundoA = float(primerA + (primerA * 0.4))
    tercerA = float(segundoA + (segundoA * 0.4))
    
    print(f'La cantidad del primer año es : {round(primerA,2)}')
    print(f'La cantidad del segundo año es : {round(segundoA,2)}')
    print(f'La cantidad del tercer año es : {round(tercerA,2)}')
    
#ejercicio3()

def ejercicio4():
    nombre = input('Escribe tu nombre: ')
    veces = int(input('Ahora escribe cuantas veces quieres que se repita: '))
    print('Esto es la forma con bucle')
    for x in range(veces):
        print(nombre)
        
    
    print('Esta la forma sin bucles')
    print(f'{nombre}\n' * veces)
    
    
#ejercicio4()

def ejercicio5():
    nombre = input('Escribe tu nombre: ')
    totalLetras = int(len(nombre))
    print(f'{nombre.upper()} tiene {totalLetras} letras')
    
#ejercicio5()

def ejercicio6():
    telefono = input('Escribe el numero de telefono con formato (prefijo-numero-extension): ')
    print(telefono[4:len(telefono)-3])
    
#ejercicio6()

def ejercicio7():
    frase = input('Escribe una frase con una vocal en minuscula: ')
    vocal = input('Ahora escribe una vocal: ')
    for x in frase:
        if x.casefold() in vocal:
            print(x.upper(), end = '')
        else:
            print(x, end = '')

#ejercicio7()

def ejercicio8():
    dinero = input('Escribe precio de un producto en euros con dos decimales: ')
    separado = dinero.split('.')
    print('Euros : ' + separado[0] + ' Monedas: ' + separado[1])
    
#ejercicio8()

def ejercicio9():
    contrLocal = 'contraseña'
    contrUsuario = input('Escribe una contraseña: ')
    
    if contrLocal == contrUsuario.lower() :
        print('La contraseña es correcta, muchas graciass')
    else :
        print('CONTRASEÑA INCORRECTA')
        
#ejercicio9()

def ejercicio10():
    edad = int(input('Escribe tu edad: '))
    ingresos = float(input('Escribe ahora tus ingresos: '))
    
    if edad > 16 :
        if ingresos > 1000 :
            print('Si tiene que tributar')
        else :
            print('No tiene que tributar')
    else :
        print('No tiene que tributar')
        
#ejercicio10()

def ejercicio11():
    rentaAnual = float(input('Escribe la renta anual: '))
    
    if rentaAnual < 10000 :
        tipoImp = float(0.05)
    elif rentaAnual >= 10000 and rentaAnual < 20000 :
        tipoImp = float(0.15)
    elif rentaAnual >= 20000 and rentaAnual < 35000 :
        tipoImp = float(0.2)
    elif rentaAnual >= 35000 and rentaAnual < 60000 :
        tipoImp = float(0.3)
    elif rentaAnual >= 60000:
        tipoImp = float(0.45)
        
    print(f'El tipo impositivo que le corresponde es del {tipoImp} %')
    
#ejercicio11()

def ejercicio12():
    pizzaBase = ['tomate','queso']
    vegetariana = ['pimiento','tofu']
    noVegetariana = ['peperoni','jamón','salmon']
    
    tipoPizza = input('Escribe si quieres una pizza vegetariana (respuesta -> si o no): ')
    
    if tipoPizza == 'si' :
        pizzaBase.extend(vegetariana)
        print(f'Ingredientes : {pizzaBase}')
    elif tipoPizza == 'no' :
        pizzaBase.extend(noVegetariana)
        print(f'Ingredientes : {pizzaBase}')
    else :
        print('No esta correcta la respuesta...')   

#ejercicio12()

def ejercicio13():
    cantidadInvertir = float(input('Escribe la cantidad a invertir : '))
    interesAnual = float(input('Ahora escribe el interes anual : '))
    numerosA = int(input('Y para finalizar escribe los años : '))
    
    for x in range(numerosA) :
        cantidadInvertir += cantidadInvertir * interesAnual
        print(f'Año {x+1} : {cantidadInvertir}')
        
#ejercicio13()

def ejercicio14():
    contr = 'contraseña'
    correcta = False
    contrUser = input('Escribe la contraseña correcta : ')
    
    while correcta == False :
        if contrUser == contr :
            correcta = True
            print('La contraseña es correcta.')
        else :
            print('La contraseña es incorrrecta.')
            contrUser = input('Escribe la contraseña correcta : ')

#ejercicio14()           

def ejercicio15_16() :
    frase = input('Escribe una frase : ')
    letra = input('Ahora escribe la letra que quieras contar : ')
    
    cantidad = frase.count(letra)
    
    print(f'La cantidad de letras {letra} es {cantidad}')
    
#ejercicio15_16()

def ejercicio17() :
    frase = input('Escribe una fase (escribe - salir - para salir)')
    
    while frase != 'salir' :
        print(frase)
        frase = input('Escribe una fase (escribe - salir - para salir)')
    else :
        print('Gracias por participar.')
        
#ejercicio17()

def ejercicio18() :
    frase = input('Escribe una frase para darle la vuelta : ')

    print(frase[::-1])
    
#ejercicio18()

#EJERCICIO 19 (son dos metodos)
def expo(base, exponente) :
    resultado = 1
    
    for x in range(exponente):
        resultado *= base
    
    return resultado

def ejercicio19() :
    
    base = int(input('Escribe el numero base : '))
    exponente = int(input('Escribe el exponente : '))

    if base > 0 and exponente > 0 :
        print(expo(base, exponente))
    else :
        print('Lo sentimos pero la base o el exponente estan incorrectos...')
    
#ejercicio19()


#Ejercicio 20
def descuento(precio) :
    return precio * 0.5

def iva(precio):
    return precio * 0.21 

def calculo(PrecioProducto, funcion) :

    precioFinal = 0
    if funcion == "descuento" :
        precioFinal = PrecioProducto + descuento(PrecioProducto)
    elif funcion == "iva" :
        precioFinal = PrecioProducto + iva(PrecioProducto)

    return precioFinal

def ejercicio20() :
    
    print('Elige uno de los productos.\nTelevisor : 500 euros\nRaton : 50\n')
    producto = input('ESCRIBE EL NOMBRE DEL PRODUCTO : ').lower
    f = input('Escribe (1) si quieres sacar el descuento, o (2) para sacar IVA : ')
    precioFinal = 0

    if producto == 'televisor' :
        if (f == 1) :
            precioFinal = calculo(500, "descuento")
        else : 
            precioFinal = calculo(500, "iva")
    elif f == 1 :
            precioFinal = calculo(50, "descuento")
    else : 
            precioFinal = calculo(50, "iva")
    
    print(f'El precio final es : {precioFinal}')

ejercicio20()