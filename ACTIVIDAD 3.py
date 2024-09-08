tamaño = 10 

def tabla_de_pitagoras():
    for numero in range(1, tamaño + 1):
        for numero2 in range(1, tamaño + 1):
            print(f'{numero * numero2: 4}', end = '')
        print()
#PODRIAMOS CREAR UNA MATRIZ VACIA EN LA QUE SE RECOPILE TODOS LOS NUMEROS DE LA TABLA, DE ESTA FORMA PARA PODER LLAMAR A LOS VALORES Y MULTIPLICARLOS

tabla_de_pitagoras()
def calcular(valore1, valore2):
    return valore1 * valore2
valor1 = int(input("Coloca el numero de fila: "))
valor2 = int(input("Coloca el numero de columna: "))
valor3 = int(input("Coloca el numero de fila: "))
valor4 = int(input("Coloca el numero de columna: "))
primValor = tabla_de_pitagoras([valor1][valor2])
segValor = tabla_de_pitagoras([valor3][valor4])
calcular(primValor, segValor)
