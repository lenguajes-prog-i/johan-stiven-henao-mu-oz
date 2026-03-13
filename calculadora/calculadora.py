def suma(a,b):
    suma = a + b
    print(suma)

def resta(a,b):
    resta = a - b
    print(resta)

def multiplicacion(a,b):
    multiplicacion = a * b
    print(multiplicacion)

def division(a,b):
    division= a / b
    print(division)

def potencia(a,b):
    potencia = a**b
    print(potencia)

def variable1():
    primerNumero = int(input("ingrese el primer numero"))
    return primerNumero
    
def variable2():
    segundoNumero = int(input("ingrese el segundo numero"))
    return segundoNumero

x = 9

while x != 0:
    print("1. suma, 2. resta, 3.multiplicacion, 4.division, 5.potencia, 0. finalizar")
    
    x = int(input("ingrese un numero del 1 al 5 para ejecutar las siguientes operaciones"))

    a = variable1()
    b = variable2()

    if x == 1:
        suma(a,b)
    elif x == 2:
        resta(a,b)
    elif x == 3:
        multiplicacion(a,b)
    elif x ==4:
        division(a,b)
    elif x == 5:
         potencia(a,b)
    else:
        if x == 0:
            print("Espero haberte ayudado")
        else:
            print("ingrese un numero correcto")
    
        
        
        


        