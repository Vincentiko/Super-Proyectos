def calcular_iva(totalcompra):
    resultado = totalcompra * 0.19
    print(f"El IVA de la compra es de: {resultado}")

def descuento(totalcompra):
    descuento = totalcompra * 0.50
    resultado = totalcompra - descuento
    print(f"Su descuento en la compra de: {descuento}")
    print(f"Su valor total es de: {resultado}")

def calcular_imc(peso, altura):
    resultado = round((peso/(altura**2)))
    return resultado

def estado_imc(imc):
    if imc<18.5:
        print("Estado: Bajo Peso")
    elif imc>=18.5 and imc<=24.9:
        print("Estado: Adecuado")
    elif imc>=25 and imc<=29.9:
        print("Estado: Sobrepeso")
    elif imc>=30 and imc<=34.9:
        print("Estado: Obesidad Grado 1")
    elif imc>=35 and imc<=39.9:
        print("Estado: Obseidad Grado 2")
    elif imc>=40:
        print("Estado: Obesidad Grado 3")


def menu():
    print("------Menu------")
    print("1.- Calcular IVA")
    print("2.- Calcular decuento")
    print("3.- Calcular IMC")

while True:
    menu()
    opcion = int(input("Elige una de las opciones: "))
    if opcion == 1:
        totalcompra = int(input("Ingrese el valor de su compra: "))
        calcular_iva(totalcompra)
    elif opcion == 2:
        totalcompra = int(input("Ingrese el valor de su compra: "))
        descuento(totalcompra)
    elif opcion == 3:
        peso = int(input("Ingrese su peso: "))
        altura = int(input("Ingrese su altura: "))
        imc = calcular_imc(peso, altura)
        print(f"El IMC es de: {imc}")
        estado_imc(imc)
