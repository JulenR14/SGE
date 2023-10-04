#EJERCICIO 1 - Se necesita obtener el promedio simple de un estudiante a partir de sus tres noras parciales N1, N2, N3.
def ejercicio1() :
    print('Ingrese las 3 notas del alumno...')
    n1 = float(input('N1: '))
    n2 = float(input('N2: '))
    n3 = float(input('N3: '))
    
    promedio = float((n1 + n2 + n3)/3)
    
    print(f'El promedio de las notas es : {promedio}')
    
#ejercicio1()

#EJERCICIO2 -  Dados como datos la base y la altura de un rectángulo, calcule el perímetro y la superficie de este.
def ejercicio2() :
    print('Escribe la base y el alto de un recatangulo :')
    base = float(input('Escribe la base : '))
    altura = float(input('Escribe la altura : '))
    
    superficie = base * altura
    perimetro = 2*(base + altura)

    print(f'La superficie es : {superficie}\nEl perimetro es : {perimetro}')
    
#ejercicio2()

#EJERCICIO 3 - Ingresar 2 números enteros diferentes e imprimir el menor de ellos con el mensaje “El menor es: --“.
def ejercicio3() :
    print('Ingrese dos numeros .')
    numero1 = float(input('Ingresa el primer numero : '))
    numero2 = float(input('Ingresa el segundo numero : '))
    
    if numero1 > numero2 :
        print(f'El menor es : {numero2}')
    else :
        print(f'El menor es : {numero1}')
        
#ejercicio3()

#EJERCICIO 4 - Desarrolle un algoritmo para determinar si un año leído por teclado es o no bisiesto.

def ejercicio4() :
    any = input('Ingrese el año : ')
    
    if any % 4 == 0 and any % 100 != 0 or any % 400 == 0 :
        print('El año es bisiesto.')
    else :
        print('El año no es bisiesto')
        
#ejercicio4()

#EJERCICIO 5 - Dado el siguiente diagrama de flujo determine la salida obtenida para los siguientes datos: A=2, B=90 y C=45.

def ejercicio5() :
    a = 2
    b = 90
    c = 45
    
    if a > b :
        if a > c :
            if b > c :
                print(f'{a}, {b}, {c}')
            else :
                print(f'{a}, {c}, {b}')
        else :
            print(f'{c}, {a}, {b}')
    elif b > c :
        if a > c :
            print(f'{b}, {a}, {c}')
        else :
            print(f'{b}, {c}, {a}')
    else :
        print(f'{c}, {b}, {a}')
        
        
#ejercicio5()

#EJERCICIO 6 - Se coloca un capital C, a un interés I (que oscila entre 0 y 100), durante M años y se desea saber en cuanto se habrá convertido ese capital en “M” años, sabiendo que es acumulativo.

def ejercicio6() :
    c = float(-1)
    i = float(-1)
    m = float(-1)
    
    while (c < 0) and ((i <= 0) or (i > 100)) and (m <= 0):
        print('Introduce capital, interés y tiempo apropiados.')
        c = float(input('CAPITAL : '))
        i = float(input('INTERES : '))
        m = float(input('AÑOS : '))
        
    for x in range(int(m)) :
        c = c * (1+i/100)

    print(f'Tienes {c} soles')
    
#ejercicio6()

#EJERCICIO 7 - Dado que el valor de ex se puede calcular por aproximación de la siguiente suma:
#e = 1 + x+x2/2! + x3/3! + ….. + xn/n!
#Realizar el programa que tome un valor para X y calcule ex hasta que xn/n! (error o aproximación) sea menor a 0.00001

def ejercicio7() :
    x = int(input('Introduce el valor de x :'))
    e = 1
    num = 1
    den = 1
    i = 1
    
    num = x * num
    den = den * i
    i = i + 1
    e = e + num/den
    
    while not((num/den) < 0.000001) :
        num = x * num
        den = den * i
        i = i + 1
        e = e + num/den
    
    print(f'e elevado a {x} es {e}')
    
#ejercicio7()

# EJERCICIO 8 - Escribir un algoritmo que imprima los 10 primeros números primos comenzando en 2 e imprima también sus respectivos cubos. Por ejemplo: 2 – 8 ; 3 – 27; 5 –125 …

def ejercicio8() :
    b = 2
    
    for i in range(2,29):
        co = 0
        for a in range(2,int(b/2)):
            if b % a == 0 :
                co = co + 1
                a = b
        
        if co == 0 :
            print(f'El cubo de {b} es : {b^3}')
        
        b += 1
        
#ejercicio8()
       
#EJERCICIO 9 - Para una empresa con N empleados, se desarrolla un algoritmo donde se ingresa como datos el número de orden y sueldo de cada empleado, debe imprimirse el numero de orden del empleado con 
#el mayor sueldo así como su sueldo. Haga el programa correspondiente.

def ejercicio9() :
    ce = int(input('Igrese la cantidad de empleados : '))
    i = 1
    smayor = 0
    print('Ingrese los sueldos.')
    
    while i <= ce :
        sueldo = float(input('Escribe sueldo : '))
        if sueldo > smayor :
            smayor = sueldo
            c = i
        i += 1
    
    print(f'El empleado numero {c} tiene el mayor sueldo que es {smayor}')
    
#ejercicio9()

# EJERCICIO 10 -  Se tiene N temperaturas. Se desea calcular su media y determinar entre todas ellas cuantas son superiores o iguales a esa media. Utiliza algún tipo de vector

def ejercicio10() :
    suma = 0
    media = 0
    c = 0
    temperaturas = [20,30,13,40]
    
    for i in temperaturas :
        suma += i
    
    media = suma/len(temperaturas)
    
    for i in temperaturas :
        
        if i >= media :
            c += 1
            print(i)
    
    print(f'La media es {media}\nEl total de temperaturas >= a media es {c}')
        
#ejercicio10()