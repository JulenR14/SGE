#PUNTO 1

def ejercicio(*args):
    if len(args) == 1:
        if isinstance(args[0], (int, float)):
            return args[0]**2
        else:
            return "No es un número " + args[0]
    elif len(args) == 2:
        if isinstance(args[0], (int, float)) and isinstance(args[1], (int, float)):
            return args[0] * args[1]
    else:
        return sum(args)
        
#print(ejercicio(2, 5, 4))

#PUNTO 2
print((lambda x: x**2)(int(input("Ingrese un número: "))))

#PUNTO 3

