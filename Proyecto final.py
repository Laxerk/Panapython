# Tomas Dolado - AL03026542
# Luis Marcelo - 
# ----------------------------------- Introduccion -----------------------------------
print("Calculadora de costo beneficio para diversos productos dentro de un supermercado/empresa, estableciendo los precios de compra al proveedor y los precios de venta al consumidor, podras ingresar el producto y se calculara la compra/venta por kilogramo.")

#clase del producto, q es la parte mas complicada de todo creo yo
class Productos:
    def __init__(self):
        self.menu = {}
    
    #agregar producto y sus propiedades de precio
    def add_item(self, item, precio_compra, precio_venta):
        self.menu[item] = {'precio_compra': precio_compra, 'precio_venta': precio_venta}
    
    #funcion para remover el item de la lista de productos
    def remove_item(self, item):
        if item in self.menu:
            del self.menu[item]
    
    #funcion para modificar un item, cambiar nombre, precios, etc
    def modify_item(self, old_item, new_item, new_precio_compra, new_precio_venta):
        #definimos como elimiar el item
        if old_item in self.menu:
            del self.menu[old_item]#item a reemplazar
            self.add_item(new_item, new_precio_compra, new_precio_venta)#establecemos el nuevo item y los nuevos precios
    
    #simplificamos para despues y creamos una funcion para poder mostrar el menu mas facil
    def show_menu(self):
        print("\nLa lista de productos es:") #simple declaracion
        for item, precios in self.menu.items():
            print(f"{item}: Compra - ${precios['precio_compra']:.2f}, Venta - ${precios['precio_venta']:.2f}")
        print()
        #ciclo basico de toda la vida :v

#le asignamos una variable a nuestra class
supermercado = Productos()

# Bucle general
while True:

    # Opciones

    print("1. Agregar productos a la lista\n2. Eliminar productos de la lista\n3. Modificar algún elemento\n4. Finalizar la edición de lista y continuar a calcular el costo-beneficio de los productos")
    
    opcion = input("¿Que desea hacer?\n- ").lower() #cambiamos todo a minusculas para evitar problemas

    # Opción 1: Agregar productos

    if opcion in ["1", "agregar", "agregar a la lista", "agregar productos"]: #asi es mas facil testear los tipos

        productos_agregar = int(input("¿Cuantos productos desea agregar?\n- ")) #vemos la cantidad d productos a agregar

        for i in range(productos_agregar): #bucle para hacerlo un poco mas facil para el usuario

            add = input("Proporciona el producto a agregar\n- ").lower() #determinamos el item a agregar

            precio_compra = float(input(f"Proporciona el precio de compra por kg para {add}\n- ")) # establecemos tanto precio d compra como precio de venta

            precio_venta = float(input(f"Proporciona el precio de venta por kg para {add}\n- ")) 

            supermercado.add_item(add, precio_compra, precio_venta) #lo agregamos a la lista

        supermercado.show_menu() #mostramos el menu actualizado

    # Opción 2: Eliminar productos

    elif opcion in ["2", "eliminar", "eliminar producto", "eliminar productos"]:

        supermercado.show_menu() #mostramos el menu actual para refrescar la memoria

        productos_remover = int(input("¿Cuantos productos desea remover?\n- "))#seleccionamos la cantidad de items a remover

        #bucle para hacerlo mas facil para el usuario
        for i in range(productos_remover):

            remove = input("\nProporciona el nombre del producto que deseas eliminar\n- ").lower()#determinamos el item a remover del menu

            supermercado.remove_item(remove)#removemos por nombre

        supermercado.show_menu()#volvemos a mostrar el menu actualizado

    # Opción 3: Modificar algún elemento

    elif opcion in ["3", "modificar", "modificar elemento", "modificar algun elemento"]:

        supermercado.show_menu()#mostramos

        #elegimos el item para modificar
        modificar = input("Elemento a modificar\n- ").lower()

        #pedimos el nuevo elemento
        modificado = input("Por que elemento deseas reemplazarlo?\n- ").lower()
        
        #establecemos el precio de compra
        nuevo_precio_compra = float(input(f"Nuevo precio de compra por kg para {modificado}\n- "))
        
        #establecemos el precio de venta
        nuevo_precio_venta = float(input(f"Nuevo precio de venta por kg para {modificado}\n- "))

        #modificamos el item con todo lo nuevo que nos dieron
        supermercado.modify_item(modificar, modificado, nuevo_precio_compra, nuevo_precio_venta)

        supermercado.show_menu()#y mostramos nuevamente para q el usuario vea lo q hizo

    # Opción 4: Finalizar edición
    elif opcion in ["4", "finalizar", "finalizar edicion"]:
        break

    #por si el menso del usuario no sabe leer :b
    else:
        print("Opcion no valida. Por favor, elija una opción correcta.")

#-----------------------------------Costo Beneficio-----------------------------------

print("\nCalculadora de Costo-Beneficio")

#almacenamos los productos seleccionados
productos_seleccionados = []

#mostramos el menú de opciones al usuario
print("\nOpciones:")
print("1.Calcular costo beneficio para productos especificos")
print("2.Calcular costo beneficio para todos los productos")
opcion = input("Seleccione una opción: ")

opcion = opcion.lower()
print(opcion)

if opcion in ["1", "productos especificos", "especificos"]:
    #mostramos los productos disponibles
    print("\nProductos disponibles:")
    for i, item in enumerate(supermercado.menu, start=1):
        print(f"{i}. {item}")
    
    #pedimos al usuario que seleccione productos
    seleccion = input("Ingrese los numeros de los productos que desea calcular separados por comas y sin espacios: ")
    indices_seleccionados = seleccion.split(',')
    
    #agregamos los productos seleccionados a la lista
    for indice in indices_seleccionados:
        if indice.isdigit():  #revisamos si es que la entrada sea un numero

            #lo convertimos en un entero
            indice = int(indice)

            if 1 <= indice <= len(supermercado.menu):  #verificamos que el índice este en rango

                producto = list(supermercado.menu.keys())[indice - 1]

                productos_seleccionados.append(producto)#agregamos el producto a la lista de lo que queremos revisar
        else:
            print(f"'{indice}' no es un número valido.")

elif opcion in ["2", "todos", "todos los productos"]:
    #añadimos todos los productos
    productos_seleccionados = list(supermercado.menu.keys())#no se si lo explique pero para que quede documentado la parte esta de "keys" basicamente devuelve
                                                            #lo que almacena el item, o sea, las 2 varables de los precios que necesitamos

#en caso de que el usuario no seleccione ninguna opcion pasamos a calcular todo automaticamente
else:
    print("Opcion no valida, calculando todos los productos.")
    productos_seleccionados = list(supermercado.menu.keys())

#creamos una variable para el beneficio total
beneficio_total = 0

#creamos una variable para el costo total
costo_total = 0

#creamos una variable para la venta total
venta_total = 0

#un bucle para calcular todos los productos que seleccionamos
for item in productos_seleccionados:

    #mostramos el producto que estamos calculando
    print(f"\nProducto: {item}")
    
    #solicitamos la cantidad vendida
    cantidad_vendida = int(input(f"Ingrese la cantidad vendida de {item} en kg en el mes: "))
    
    #buscamos el precio de compra y venta en el item
    precio_compra = supermercado.menu[item]['precio_compra']
    precio_venta = supermercado.menu[item]['precio_venta']
    
    #calculamos el costo del producto
    costo_producto = precio_compra * cantidad_vendida
    
    #calculamos la venta total del producto
    venta_producto = precio_venta * cantidad_vendida
    
    #calculamos el beneficio del producto por separado
    beneficio_producto = (precio_venta - precio_compra) * cantidad_vendida
    
    #sumamos lo que calculamos arriba en el beneficio total, el costo total y la venta total
    beneficio_total += beneficio_producto
    costo_total += costo_producto
    venta_total += venta_producto
    
    #mostramos el costo, la venta y el beneficio del producto individual
    print(f"Costo de {item}: ${costo_producto:.2f}")
    print(f"Venta de {item}: ${venta_producto:.2f}")
    print(f"Beneficio de {item}: ${beneficio_producto:.2f}")

#mostramos el costo total, la venta total y el beneficio total
print(f"Venta total de los productos vendidos: ${venta_total:.2f}")
print(f"\nCosto de los productos comprados: ${costo_total:.2f}")
print(f"Beneficio total del mes: ${beneficio_total:.2f}")#tampoco se si lo explique pero el :.f se encarga de redondear los
                                                            #ultimos 2 decimales del resultado, es mas comodo que el round

print("-----------------------------------Programa finalizado-----------------------------------")