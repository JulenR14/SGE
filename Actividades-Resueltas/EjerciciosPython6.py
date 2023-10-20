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
#print((lambda x: x**2)(int(input("Ingrese un número: "))))

#PUNTO 3
class Persona:

    def __init__(self, nombre, identificador, telefono, email, direccion):
        self.nombre = nombre
        self.identificador = identificador
        self.__telefono = telefono
        self.email = email
        self.direccion = direccion  
        
    def __str__(self):
        return f"Nombre: {self.nombre}\nIdentificador: {self.identificador}\nTeléfono: {self.__telefono}\nEmail: {self.email}\nDirección: {self.direccion}"
        
        
class Cliente(Persona):
    def __init__(self, nombre, identificador, telefono, email, direccion):
        super().__init__(nombre, identificador, telefono, email, direccion)
        self.ultima_compra = ([], "")
        
    def compra(self, *productos):
        Cliente.ultima_compra = (productos, "Fecha de la compra")
        
    def __str__(self):
        return super().__str__() + f"\nÚltima compra: {self.ultima_compra}"
    
class Empleado(Cliente):
    
    numeroEmpleados = 0
    
    def __init__(self, nombre, identificador, telefono, email, direccion, numeroCuenta, seccion, supervisorIdentificador):
        super().__init__(nombre, identificador, telefono, email, direccion)
        self.__numeroCuenta = numeroCuenta
        self.seccion = seccion
        self.supervisorIdentificador = supervisorIdentificador
        Empleado.numeroEmpleados += 1
    
    def getNumeroEmpleados():
        return Empleado.numeroEmpleados
    
    def aumentarEmpleado():
        Empleado.numeroEmpleados += 1
        
    def reducirEmpleado():
        Empleado.numeroEmpleados -= 1
        
    def __str__(self):
        return super().__str__() + f"\nNúmero de Cuenta: {self.__numeroCuenta}\nSección: {self.seccion}\nSupervisor: {self.supervisorIdentificador}"
    
cliente1 = Cliente("Cliente 1", "ID001", "123-456-7890", "cliente1@email.com", "Dirección Cliente 1")
cliente1.compra("Producto A", "Producto B", "Producto C")
print('Información del Cliente:\n', cliente1)

empleado1 = Empleado("Empleado 1", "ID002", "555-555-5555", "empleado1@email.com", "Dirección Empleado 1", "Cuenta123", "Sección A", "Supervisor 1")
Empleado.aumentarEmpleado()
empleado2 = Empleado("Empleado 2", "ID003", "777-777-7777", "empleado2@email.com", "Dirección Empleado 2", "Cuenta456", "Sección B", "Supervisor 2")

print("\nInformación de Empleados:\n")
print(empleado1)
print()
print(empleado2)
print()
print(f"Número de Empleados: {Empleado.getNumeroEmpleados()}")