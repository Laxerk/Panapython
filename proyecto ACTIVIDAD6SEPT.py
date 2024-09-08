#TERCER CODIGO-PROYECTO
#INTEGRANTES: lUIS Marcelo Moreno Camacho, Angel David Roque Castro
class proceso():
    def __init__(self):
        self.menu = {}
    def agregar_producto(self, nombre, cantidad, precio):
        self.menu[nombre] = {"Cantidad": cantidad, "Precio": precio,}

    def eliminar(self, nombre):
        if not self.menu:
            print("No hay ningun producto para eliminar")
        else:    
            if nombre in self.menu:
                del self.menu[nombre]

    def calcularTotal(self):
        total = 0
        for detalles in self.menu.values():
            total += detalles["Cantidad"] * detalles["Precio"]
        print(f'El valor total del inventario es de ${total} MXN')

            
    def actualizar(self, producto_anterior, producto_nuevo, nuevaCantidad, nuevoPrecio):
        if producto_anterior in self.menu:
            del self.menu[producto_anterior]
        self.agregar_producto(producto_nuevo, nuevaCantidad, nuevoPrecio)

    def mostrarInventario(self):
        if not self.menu:
            print("El inventario esta vacio")
        else:
            print("\nNuestro inventario es el siguiente: ")
            for nombre, detalles in self.menu.items():
                cantidad = detalles["Cantidad"]
                precio = detalles["Precio"]
                print(f'Producto: {nombre} \nCantidad: {cantidad} \nPrecio: ${precio} MXN')
    def modificarCantidadOPrecio(self, nombre):
        if nombre in self.menu:
            print(f'El producto "{nombre}" se modificara, pero..')
            accion2 = input("¿Que deseas hacer? \n1 - Modificar el precio \n2 - Modificar la cantidad \n3 - Modificar ambos\n")
            if accion2 == "1" or accion2 == "Modificar el precio" or accion2 == "precio":
                nuevoPrecio = float(input(f'¿Cual es el nuevo precio del producto "{nombre}"?\n'))
                self.menu[nombre]["Precio"] = nuevoPrecio
            elif accion2 == "2" or accion2 == "Modificar la cantidad" or accion2 == "cantidad":
                nuevaCantidad = int(input(f'¿Cual es la nueva cantidad del producto "{nombre}"?\n'))
                self.menu[nombre]["Cantidad"] = nuevaCantidad
            elif accion2 == "3" or accion2 == "Modificar ambos" or accion2 == "ambos":
                nuevoP = float(input(f'¿Cual es el nuevo precio del producto "{nombre}"?\n'))
                self.menu[nombre]["Precio"] = nuevoP
                nuevaC = int(input(f'¿Cual es la nueva cantidad del producto "{nombre}"?\n'))
                self.menu[nombre]["Cantidad"] = nuevaC
            else:
                print("Coloque una opcion valida")

        else:
            print("Agregue un producto a modificar existente")

inventario = proceso()


while(True):
    print("\nBienvenido al inventario")
    print("1 - Agregar producto\n 2 - Eliminar producto\n 3 - Calcular el total\n 4 - Actualizar o modificar\n 5 - Modificar cantidad/precio/ambos\n 6 - Mostrar inventario\n 7 - Finalizar")
    accion = input("¿Que deseas hacer?:\n ")

    if accion == "1" or accion == "Agregar producto" or accion == "agregar":
        agregar = input("Que producto deseas agregar?: ")
        cantidadWH = int(input("Coloca la cantidad del producto: "))
        precioWH = float(input("Coloca el precio del producto: "))
        inventario.agregar_producto(agregar, cantidadWH, precioWH)
        inventario.mostrarInventario()

    elif accion == "2" or accion == "Eliminar producto" or accion == "eliminar":
        if not inventario.menu:
            print("No hay productos a eliminar")
        else:    
            inventario.mostrarInventario()
            inventario.eliminar('nombre')
            eliminar = input("¿Que producto deseas eliminar?: ")
            inventario.eliminar(eliminar)
            print(f'El producto {eliminar} se ha eliminado correctamente del inventario')

    elif accion == "3" or accion == "Calcular el total" or accion == "calcular":
        inventario.calcularTotal()

    elif accion == "4" or accion == "Actualizar o modificar" or accion == "actualizar":
        if not inventario.menu:
            print("No hay productos a modificar")
        else:
            inventario.mostrarInventario()
            productoEliminar = input("Coloca el producto a modificar: ")
            productoNuevo = input("Coloca el producto a agregar: ")
            cantidadNueva = int(input("Coloca la nueva cantidad del producto: "))
            precioNuevo = float(input("Coloca el precio nuevo: "))
            inventario.actualizar(productoEliminar, productoNuevo, cantidadNueva, precioNuevo)
    
    elif accion == "5" or accion == "Modificar cantidad/precio/ambos":
        if not inventario.menu:
            print("No hay productos a modificar")
        else:
            inventario.mostrarInventario()
            modificarprecioOcantidad = input("Coloca el nombre del producto que deseas modificar: ")
            inventario.modificarCantidadOPrecio(modificarprecioOcantidad)
            inventario.mostrarInventario()

    elif accion == "6" or accion == "Mostrar inventario" or accion == "mostrar":
        inventario.mostrarInventario()
    
    elif accion == "7" or accion == "Finalizar" or accion == "finalizar":
        print("El programa finalizo")
        break
    
    else:
        print("Agregue una opcion valida")

        






       


 
        
        
