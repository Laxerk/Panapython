#PRIMER EJERCICIO
abrir = open("notas.txt", "w")
abrir.write("#Lista de Tareas que hacer#\n")
abrir.write("Programacion - Ejercicios 'open'")
abrir.writelines("\nNube - Estudiar")
abrir.close()

#SEGUNDO EJERCICIO
nombres = ["Luis", "Pablo", "Gerson", "Tomas"]
crear = open("nombres.txt", "w")
for nombre in nombres:
    crear.write(f'{nombre}\n')

#TERCER EJERCICIO
import csv

titulos = ["Nombre", "Precio", "Cantidad"]

productos = []
print("Crearemos un archivo csv con datos de un producto\n Nota: Puede colocar los productos que requiera")
while(True):
    accion = input("Si desea continuar presione si, si desea finalizar coloque no: ").lower()
    if accion == "si":
        producto = input("Coloque el nombre del producto: ")
        precio = float(input("Coloque el precio del producto: "))
        cantidad = int(input("Coloque la cantidad del producto: "))
        productos.append([producto, precio, cantidad])
    elif accion == "no":
        break
    else:
        print("Coloque una opcion valida")
with open("productos.csv", mode="w", newline="") as archivo_csv:
    crear3 = csv.writer(archivo_csv)
    crear3.writerow(titulos)
    crear3.writerows(productos)
print("El archivo se ha creado con exito")

#CUARTO EJERCICIO
try:
    crear4 = open("archivotextoACTIVIDAD.txt", "a")
    crear4.write("Hola archivo de texto")
    crear4.write("Prueba y error")
except IOError:
    print("Ha habido un problema al escribir en este archivo")
except Exception as e:
    print("Ha ocurrido un problema en este archivo")