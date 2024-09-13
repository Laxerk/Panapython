#PRIMER PROBLEMA
def sacarContraseña (contraseña):
    caracteres = len(contraseña) >= 10
    mayuscula = any(d.isupper() for d in contraseña)
    minuscula = any(d.islower() for d in contraseña)
    numero = any(d.isdigit() for d in contraseña)
    caracterEspecial = any(d in ".,_-{[]}^*+~¨´¿¡'?=/&%$#!" for d in contraseña)

    errores = []
    if not caracteres:
        errores.append("Tu contraseña tiene que tener mas de 10 caracteres")
    if not mayuscula:
        errores.append("Tu contraseña tiene que tener al menos una mayuscula")
    if not minuscula:
        errores.append("Tu contraseña tiene que tener al menos una minuscula")
    if not numero:
        errores.append("Tu contraseña tiene que tener al menos un numero")
    if not caracterEspecial:
        errores.append("Tu contraseña tiene que tener un caracter especial")
    if not errores:
        return"Tu contraseña es segura"
    else:
        return f'Tu contraseña es insegura, tiene los siguientes errores\n: {errores}'

contraseñaEZ = input("Coloca una contraseña: ")
validacion = sacarContraseña(contraseñaEZ)
print(validacion)

#SEGUNDO PROBLEMA
monedasP = {
    'USD' : 1.0,
    'EUR' : 0.91,
    'MXN' : 19.82,
    'JPY' : 142.53,
    'AUD' : 1.49,
    'CAD' : 1.36,
    'KWD' : 0.31,
    'GBP' : 0.76,
    'ARS' : 959.25
}

def calcularMoneda(cantidad, monedaPrincipal, monedaCalcular1, monedaCalcular2):
    if monedaPrincipal not in monedasP:
        print("Coloca una moneda valida")
    if monedaCalcular1 not in monedasP:
        print("Coloca una moneda valida")
    if monedaCalcular2 not in monedasP:
        print("Coloca una moneda valida")

    monedaBase = cantidad / monedasP[monedaPrincipal]
    monedaCal1 = monedaBase * monedasP[monedaCalcular1]
    monedaCal2 = monedaBase * monedasP[monedaCalcular2]
    return f'{cantidad} {monedaPrincipal} son {monedaCal1:.2f} {monedaCalcular1} y {monedaCal2:.2f} {monedaCalcular2}'
print("TIPOS DE MONEDA PRESENTES\n USD = Dolar Estadounidense\n EUR = Euro\n MXN = Pesos mexicanos\n JPY = Yens\n AUD = Dolar Australiano\n CAD = Dolar Canadiense\n KWD = Dinar Kuwaiti\n GBP = Libra Esterlina\n ARS = Pesos Argentinos")
monedaAusar = input("Ingresa la moneda que quieras utilizar: ").upper()
cantidadDEF = float(input("Ingresa la cantidad de dinero que quieras calcular: "))
monedaAcalcular1 = input("Ingresa la primer moneda que quieras calcular tu cantidad: ").upper()
monedaAcalcular2 = input("Ingresa la segunda moneda que quieras calcular tu cantidad: ").upper()
calculoDEF = calcularMoneda(cantidadDEF, monedaAusar, monedaAcalcular1, monedaAcalcular2)
print(calculoDEF)

#TERCER PROBLEMA
candidatos = {
    'Luis' : 0,
    'Tomas' : 0,
    'Gerson' : 0,
    'Cesar' : 0,
    'David' : 0
}
def registrarVOTO(candidato):
    if candidato not in candidatos:
        decision = input("El candidato no existe, desea agregarlo?(si/no): ").lower()
        if decision == "si":
            candidatos[candidato] = 1
        elif decision == "no":
            return "Intente nuevamente"
        else:
            print("Ingrese una opcion valida")
    else:
        candidatos[candidato] += 1

while(True):
    votar = input("BIENVENIDO AL REGISTRO DE VOTOS\n --Lista de candidatos existentes--\n Luis\n Tomas\n Gerson\n Cesar\n David\n Vote por alguno de los candidatos existentes o de lo contrario agregue uno de su preferencia: ").capitalize()
    registrarVOTO(votar)
    
    continuar = input("Desea votar nuevamente? (si/no): ").lower()
    if continuar == "si":
        continue
    elif continuar == "no":
        break
    else:
        print("Ingrese una opcion valida")
for candidato, votos in candidatos.items():
    print(f'El candidato {candidato} tiene {votos} votos')

#CUARTO PROBLEMA
#CODIGO CON CORCHETES Y COMAS
listaPANA = []

while(True):
    agregar =input("Agrega una palabra de tu preferencia a la lista: ")
    listaPANA.append(agregar)
    continuaR = input("Deseas continuar?(si/no): ")
    if continuaR == "si":
        continue
    elif continuaR == "no":
        break
    else:
        print("No se ingreso una respuesta esperada, se continuara como si la respuesta hubiera sido 'si' ")
ordenarPalabras = sorted(listaPANA, key=lambda listaPANA: (len(listaPANA), listaPANA))
print(ordenarPalabras)
#CODIGO SIN CORCHETE NI COMAS
listaPANA = []

while(True):
    agregar =input("Agrega una palabra de tu preferencia a la lista: ")
    listaPANA.append(agregar)
    continuaR = input("Deseas continuar?(si/no): ")
    if continuaR == "si":
        continue
    elif continuaR == "no":
        break
    else:
        print("No se ingreso una respuesta esperada, se continuara como si la respuesta hubiera sido 'si' ")
ordenarPalabras = sorted(listaPANA, key=lambda listaPANA: (len(listaPANA), listaPANA))
for palabras in listaPANA:
    print(palabras)

#QUINTO PROBLEMA
inventario = {}

def agregarProducto(nombre, cantidad, precio):
    inventario[nombre] = (cantidad, precio)

def mostrarInventario():
    if not inventario:
        print("El inventario esta vacio\n")
    else:
        print("El inventario es el siguiente: \n")
        for producto, (cantidad, precio) in inventario.items():
            print(f'Producto: {producto}\nCantidad: {cantidad}\nPrecio: {precio} MXN ')

def consultarCantidadPrecio():
    if not inventario:
        print("El inventario esta vacio")
    else:
        productoConsultar = input("Que producto quieres consultar su cantidad y precio?: ")
        if productoConsultar in inventario:
            cantidad, precio = inventario[productoConsultar]
            print(f'El producto {productoConsultar} tiene un precio de {precio} MXN y hay {cantidad} disponibles')
        else:
            print("Proporcione un producto existente")

print("--BIENVENIDO AL STOCK DE INVENTARIO--")
while(True):
    accion = input("\n1 - Agregar producto\n2 - Mostrar inventario\n3 - Consultar el precio y cantidad de un producto\n4 - Finalizar\n ¿Que desea hacer?: ")
    if accion == "1":
        agregarAccion = input("Coloque el nombre del producto: ").lower()
        cantidadDef = int(input("Coloque la cantidad de este producto disponible: "))
        precioDEF = float(input("Coloque el precio de este producto: "))
        accionVerdadera = agregarProducto(agregarAccion, cantidadDef, precioDEF)
        mostrarInventario()
    if accion == "2":
        mostrarInventario()
    if accion == "3":
        consultarCantidadPrecio()
    if accion == "4":
        print("Esto ha sido el stock, termino el programa")
        break

#SEXTO PROBLEMA
def contarPalabras(texto):
    textos = texto.lower().split()
    frecuencia = {}
    for palabra in textos:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia
textoPana = input("Coloca cualquier texto: ")
contarFrecuencia = contarPalabras(textoPana)
for palabra, frecuencia in contarFrecuencia.items():
    print(f'La palabra {palabra} aparece {frecuencia} veces')

