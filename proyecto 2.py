import random
numRandom = random.randint(1, 100)
contadorIntentos = 0
intentos = []
def rangoCercano(numR, numA):
    rango = abs(numR - numA)
    if rango <= 10:
        return "--Estas cerca--"
    else:
        return "--Estas lejos--"
print("Adivina el numero(entre el 1 al 100): \n")
while contadorIntentos != 5:
    numAdivinado = int(input("Cual numero escoges?: "))
    if numAdivinado == numRandom:
        print("Has adivinado el numero, felicidades!")
        break
    else:
        intentos.append(numAdivinado)
        contadorIntentos += 1
        print("No has acertado, aqui tienes pistas")
        if numAdivinado > numRandom:
            print("--Tu numero es mayor que el numero aleatorio--")
        else:
            print("--Tu numero es menor al numero aleatorio--")
        comprobarRANGO = rangoCercano(numRandom, numAdivinado)
        print(comprobarRANGO)
if contadorIntentos < 5:
    print("Felicidades! Has finalizado el juego, aqui tienes el historial de tus intentos\n", intentos)
elif contadorIntentos == 5:
    print("Buena suerte para la otra! aqui tienes el historial de tus intentos\n", intentos, "\nEl numero era: ", numRandom)


