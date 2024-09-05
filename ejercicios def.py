#PRIMER PROBLEMA
def saludar(nombre):
    print("Hola", nombre)

saludar("Luis Marcelo")

#SEGUNDO PROBLEMA
def area_circulo(radio):
    return 3.14*radio**2

radioDEF = int(input("Ingresa el radio de un circulo: "))
area = area_circulo(radioDEF)
print(f'El area del circulo es de {area}')