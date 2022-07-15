print("Este programa cuenta con 5 funciones")
print("Opcion 1 - Saludar al Mundo\nOpcion 2 - Que lo saluden!\nOpcion 3 - Suma y Resta de dos numeros \nOpcion 4 - Suma y Promedio de tres numeros \nOpcion 5 -  Calcular el IVA de una Factura")
opcion = int(input("Ingrese la opcion que desea utilizar (1,2,3,4 o 5): "))
def SaludoMundo():
    print('Hola Mundo!')
def SaludarUsuario():
    nombre= str(input('Ingrese su nombre: '))
    print('Hola '+ nombre,'!')

def SumayResta():
    num1= int(input("Ingrese un numero: "))
    num2= int(input("Ingrese un 2do numero: "))
    suma= num1 + num2
    resta= num1 - num2
    print(f'Suma= {suma}\nResta= {resta}')
def SumayPromedio():
    num1= int(input("Ingrese un numero: "))
    num2= int(input("Ingrese un 2do numero: "))
    num3= int(input("Ingrese un 3er numero: "))
    suma = num1 + num2 + num3
    promedio= suma/3
    print(f'Suma= {suma}\nPromedio= {promedio}')

def CalcIVA():
    monto= float(input('Ingrese el monto de su factura: '))
    IVA= 1.21
    montoConIVA= monto*IVA
    print(f'El monto con IVA de 21% es = {montoConIVA}')

if opcion == 1:
    print("Usted eligio la Opcion 1 - Saludar al Mundo")
    SaludoMundo()
if opcion == 2:
    print("Usted eligio la Opcion 2 - Que lo saluden!")
    SaludarUsuario()
if opcion == 3:
    print("Usted eligio la Opcion 3 - Suma y Resta de dos numeros")
    SumayResta()
if opcion == 4:
    print("Usted eligio la Opcion 4 - Suma y Promedio de tres numeros")
    SumayPromedio()
if opcion == 5:
    print("Usted eligio la Opcion 5 - Calcular el IVA de una Factura")
    CalcIVA()
print("Gracias por utilizar el programa!")