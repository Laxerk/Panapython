#PRIMER PROBLEMA
ent = []
contador = 0
while contador != 3:
    numEnt = int(input("Ingresa 3 numeros enteros: "))
    contador += 1
    ent.append(numEnt)
print(f'Los numeros escritos son: {ent}')

#SEGUNDO PROBLEMA
numeros = (10, 20, 30, 40, 50)
print(numeros[3])

#TERCER PROBLEMA
tupla_anidada = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(tupla_anidada[1][1])

#CUARTO PROBLEMA
tupla_par = (2, 4, 6, 8, 10)
tupla_impar = (1, 3, 5, 7, 9)
tupla_concatenada = tupla_par + tupla_impar
print(f'La tupla concatenada es {tupla_concatenada}')

#QUINTO PROBLEMA
colores = (('rojo', 'azul', 'verde', 'rojo', 'amarillo', 'rojo'))
contador2 = 0
for color in colores:
    if color == "rojo":
        contador2 += 1
print(f'El color rojo aparece {contador} veces')

#SEXTO PROBLEMA
nombres = ['Ana', 'Juan', 'Pedro', 'Luis']
tupla_nombres = tuple(nombres)
print(tupla_nombres)

#SEPTIMO PROBLEMA
tupla_larga = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
lista_tupla = []
contador = 0
while contador != 5:
    for num in tupla_larga:
        lista_tupla.append(num)
        contador += 1
tuplaNueva = tuple(lista_tupla)
print(tuplaNueva)
