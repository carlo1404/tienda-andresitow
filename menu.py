from os import system
from vendedor import Vendedor
from clientes import Cliente
from productos import Producto
from venta import Venta
class Menu:
    def __init__(self):
        self.vendedores = []
        self.clientes = []
        self.productos = []
        self.ventas = []
    def registrar_vendedor(self):
        system("cls")
        try:
            print("=== Registro de Vendedor ===")
            id_vendedor = int(input("ID del vendedor: "))
            if id_vendedor <= 0:
                print("Error - El ID debe ser mayor a cero")
                input("Presione Enter para continuar...")
                return
            id_existente = False
            for v in self.vendedores:
                if v.id == id_vendedor:
                    id_existente = True
                    break
            if id_existente:
                print("Error - El ID ya existe")
                input("Presione Enter para continuar...")
                return
            nombre = input("Nombre: ")
            if nombre == "":
                print("Error - El nombre no puede estar vacío")
                input("Presione Enter para continuar...")
                return
            telefono = input("Teléfono: ")
            if telefono == "" or not telefono.isdigit() or int(telefono) <= 0:
                print("Error - El teléfono debe ser un número positivo")
                input("Presione Enter para continuar...")
                return
            direccion = input("Domicilio: ")
            if direccion == "":
                print("Error - La dirección no puede estar vacía")
                input("Presione Enter para continuar...")
                return
            edad = int(input("Edad: "))
            if edad <= 17 or edad > 66:
                print("Error - La edad debe estar entre 18 y 60 años")
                input("Presione Enter para continuar...")
                return
            vendedor = Vendedor(id_vendedor, nombre, telefono, direccion, edad)
            self.vendedores.append(vendedor)
            print("Vendedor registrado correctamente")
        except ValueError:
            print("Error - Se esperaba un número válido")
        input("Presione Enter para continuar...")

    def listar_vendedores(self):
        system("cls")
        print("=== Lista de Vendedores ===")
        if not self.vendedores:
            print("No hay vendedores registrados")
        else:
            for v in self.vendedores:
                print(f"ID: {v.id}")
                print(f"Nombre: {v.nombre}")
                print(f"Teléfono: {v.telefono}")
                print(f"Domicilio: {v.direccion}")
                print(f"Edad: {v.edad}")
                print("----------------------------------------" )
        input("Presione Enter para continuar...")

    def modificar_vendedor(self):
        system("cls")
        print("=== Modificar Vendedor ===")
        id_vendedor = input("ID del vendedor a modificar: ")
        if not id_vendedor.isdigit():
            print("El ID debe ser un número")
            input("Presione Enter para continuar...")
            return
        id_vendedor = int(id_vendedor)
        vendedor = None
        for v in self.vendedores:
            if v.id == id_vendedor:
                vendedor = v
                break
        if not vendedor:
            print("Vendedor no encontrado")
            input("Presione Enter para continuar...")
            return
        print(f"Datos actuales del vendedor {vendedor.nombre}:")
        print("1. Nombre:", vendedor.nombre)
        print("2. Teléfono:", vendedor.telefono) 
        print("3. Dirección:", vendedor.direccion)
        print("4. Edad:", vendedor.edad)
        opcion = input("Seleccione qué desea modificar (1-4) o Enter para cancelar: ")
        if opcion == "1":
            nuevo_nombre = input("Nuevo nombre: ")
            if nuevo_nombre:
                vendedor.nombre = nuevo_nombre
                print("Nombre modificado correctamente")
        elif opcion == "2":
            nuevo_telefono = input("Nuevo teléfono: ")
            if nuevo_telefono.isdigit() and int(nuevo_telefono) > 0:
                vendedor.telefono = nuevo_telefono
                print("Teléfono modificado correctamente")
            else:
                print("Error: El teléfono debe ser un número positivo")
        elif opcion == "3":
            nueva_direccion = input("Nueva dirección: ")
            if nueva_direccion:
                vendedor.direccion = nueva_direccion
                print("Dirección modificada correctamente")
        elif opcion == "4":
            try:
                nueva_edad = int(input("Nueva edad: "))
                if 18 <= nueva_edad <= 66:
                    vendedor.edad = nueva_edad
                    print("Edad modificada correctamente")
                else:
                    print("Error: La edad debe estar entre 18 y 60 años")
            except ValueError:
                print("Error: La edad debe ser un número")
        else:
            print("Modificación cancelada")

    def eliminar_vendedor(self):
        system("cls")
        print("=== Eliminar Vendedor ===")
        try:
            # Get vendor ID to delete
            id_vendedor = int(input("Ingrese el ID del vendedor a eliminar: "))
            index_to_delete = -1
            for i, vendedor in enumerate(self.vendedores):
                if vendedor.id == id_vendedor:
                    index_to_delete = i
                    break
            if index_to_delete >= 0:
                vendedor = self.vendedores[index_to_delete]
                confirmacion = input(f"¿Está seguro de eliminar al vendedor {vendedor.nombre}? (s/n): ").lower()
                if confirmacion == 's':
                    self.vendedores.pop(index_to_delete)
                    print("Vendedor eliminado exitosamente")
                else:
                    print("Operación cancelada")
            else:
                print("Error: No se encontró un vendedor con ese ID")
        except ValueError:
            print("Error: El ID debe ser un número entero")

    def registrar_cliente(self):
        system("cls")
        try:
            print("=== Registro de Cliente ===")
            id_cliente = int(input("Ingrese el id o tu numero de identificacion para ser registrado: "))
            if id_cliente <= 0:
                print("Error - El ID debe ser mayor a cero")
                input("Presione Enter para continuar...")
                return

            id_existente_cliente = False
            for c in self.clientes:
                if c.id == id_cliente:
                    id_existente_cliente = True
                    break
            if id_existente_cliente:
                print("Error - El ID ya existe")
                input("Presione Enter para continuar...")
                return

            nombre = input("Nombre: ")
            if nombre == "":
                print("Error - El nombre no puede estar vacío")
                input("Presione Enter para continuar...")
                return

            telefono = input("Teléfono: ")
            if telefono == "" or not telefono.isdigit() or int(telefono) <= 0:
                print("Error - El teléfono debe ser un número positivo")
                input("Presione Enter para continuar...")
                return

            direccion = input("Domicilio: ")
            if direccion == "":
                print("Error - La dirección no puede estar vacía")
                input("Presione Enter para continuar...")
                return
            cliente = Cliente(id_cliente, nombre, telefono, direccion)
            self.clientes.append(cliente)
            print("Cliente registrado correctamente")
        except ValueError:
            print("Error - Se esperaba un número válido")

    def listar_clientes(self):
        system("cls")
        print("=== Listas de Clientes ===")
        if not self.clientes:
            print("No hay clientes registrados")
        else:
            for c in self.clientes:
                print(f"ID: {c.id}")
                print(f"Nombre: {c.nombre}")
                print(f"Teléfono: {c.telefono}")
                print(f"Domicilio: {c.direccion}")
                print("----------------------------------------" )
        input("Presione Enter para continuar...")
    def modificar_cliente(self):
        from os import system
        system("cls")
        print("=== Modificar Cliente ===")
        id_cliente = input("ID del cliente a modificar: ")
        if not id_cliente.isdigit():
            print("El ID debe ser un número")
            input("Presione Enter para continuar...")
            return
        id_cliente = int(id_cliente)
        cliente = None
        for c in self.clientes:
            if c.id == id_cliente:
                cliente = c
                break
        if not cliente:
            print("Cliente no encontrado")
            input("Presione Enter para continuar...")
            return
        print(f"Datos actuales del cliente {cliente.nombre}:")
        print("1. Nombre:", cliente.nombre)
        print("2. Teléfono:", cliente.telefono)
        print("3. Dirección:", cliente.direccion)
        opcion = input("Seleccione qué desea modificar (1-3) o Enter para cancelar: ")
        if opcion == "1":
            nuevo_nombre = input("Nuevo nombre: ")
            if nuevo_nombre:
                cliente.nombre = nuevo_nombre
                print("Nombre modificado correctamente")
        elif opcion == "2":
            nuevo_telefono = input("Nuevo teléfono: ")
            if nuevo_telefono.isdigit() and int(nuevo_telefono) > 0:
                cliente.telefono = nuevo_telefono
                print("Teléfono modificado correctamente")
            else:
                print("Error: El teléfono debe ser un número positivo")
        elif opcion == "3":
            nueva_direccion = input("Nueva dirección: ")
            if nueva_direccion:
                cliente.direccion = nueva_direccion
                print("Dirección modificada correctamente")
        else:
            print("Modificación cancelada")

    def eliminar_cliente(self):
        system("cls")
        print("=== Eliminar Cliente ===")        
        try:
            # Get vendor ID to delete
            id_cliente = int(input("Ingrese el ID del cliente a eliminar: "))
            index_to_delete = -1
            for i, Cliente in enumerate(self.clientes):
                if Cliente.id == id_cliente:
                    index_to_delete = i
                    break
            if index_to_delete >= 0:
                Cliente = self.clientes[index_to_delete]
                confirmacion = input(f"¿Está seguro de eliminar al cliente {Cliente.nombre}? (s/n): ").lower()
                if confirmacion == 's':
                    self.clientes.pop(index_to_delete)
                    print("Cliente eliminado exitosamente")
                else:
                    print("Operación cancelada")
            else:
                print("Error: No se encontró un cliente con ese ID")
        except ValueError:
            print("Error: El ID debe ser un número entero")
    def registrar_producto(self):
        system("cls")
        try:
            print("=== Registro de Producto ===")
            id_producto = int(input("ID del producto: "))
            if id_producto <= 0:
                print("Error - El ID debe ser mayor a cero")
                input("Presione Enter para continuar...")
                return
            id_existente_producto = False
            for p in self.productos:
                if p.id == id_producto:
                    id_existente_producto = True
                    break
            if id_existente_producto:
                print("Error - El ID ya existe")
                input("Presione Enter para continuar...")
                return
            nombre = input("Nombre: ")
            if nombre == "":
                print("Error - El nombre no puede estar vacío")
                input("Presione Enter para continuar...")
                return
            precio_compra = float(input("Precio de compra: "))
            if precio_compra <= 0:
                print("Error - El precio de compra debe ser mayor a cero")
                input("Presione Enter para continuar...")
                return
            precio_venta = float(input("Precio de venta: "))
            if precio_venta <= 0:
                print("Error - El precio de venta debe ser mayor a cero")
                input("Presione Enter para continuar...")
                return
            stock = int(input("Stock disponible: "))
            if stock <= 0:
                print("Error - El stock disponible debe ser mayor a cero")
                input("Presione Enter para continuar...")
                return
            producto = Producto(id_producto, nombre, precio_compra, precio_venta, stock)
            self.productos.append(producto)
            print("Producto registrado correctamente")
        except ValueError:
            print("Error - Se esperaba un número válido")

    def listar_productos(self):
        system("cls")
        print("=== Lista de Productos ===")
        if not self.productos:
            print("No hay productos registrados")
        else:
            for p in self.productos:
                print(f"ID: {p.id}")
                print(f"Nombre: {p.nombre}")
                print(f"Precio de compra: {p.precio_compra}")
                print(f"Precio de venta: {p.precio_venta}")
                print(f"Stock disponible: {p.stock}")
                print("----------------------------------------" )
        input("Presione Enter para continuar...")  

    def listar_productos_con_stock(self):
        system("cls")
        print("=== Lista de Productos con Stock ===")
        if not self.productos:
            print("No hay productos registrados")
        else:
            for p in self.productos:
                if p.stock > 0:
                    print(f"ID: {p.id}")
                    print(f"Nombre: {p.nombre}")
                    print(f"Precio de compra: {p.precio_compra}")
                    print(f"Precio de venta: {p.precio_venta}")
                    print(f"Stock disponible: {p.stock}")
                    print("----------------------------------------" )
    
    def listar_productos_sin_stock(self):
        system("cls")
        print("=== Lista de Productos sin Stock ===")
        if not self.productos:
            print("No hay productos registrados")
        else:
            for p in self.productos:
                if p.stock <= 0:
                    print(f"ID: {p.id}")
                    print(f"Nombre: {p.nombre}")
                    print(f"Precio de compra: {p.precio_compra}")
                    print(f"Precio de venta: {p.precio_venta}")
                    print(f"Stock disponible: {p.stock}")
                    print("----------------------------------------" )
    
    def modificar_producto(self):
        system("cls")
        print("=== Modificar Producto ===")
        id_producto = input("ID del producto a modificar: ")
        if not id_producto.isdigit():
            print("El ID debe ser un número")
            input("Presione Enter para continuar...")
            return
        id_producto = int(id_producto)
        producto = None
        for p in self.productos:
            if p.id == id_producto:
                producto = p
                break
        if not producto:
            print("Producto no encontrado")
            input("Presione Enter para continuar...")
            return
        print(f"Datos actuales del producto {producto.nombre}:")
        print("1. Nombre:", producto.nombre)
        print("2. Precio de compra:", producto.precio_compra)
        print("3. Precio de venta:", producto.precio_venta)
        print("4. Stock disponible:", producto.stock)
        opcion = input("Seleccione qué desea modificar (1-4) o Enter para cancelar: ")
        if opcion == "1":
            nuevo_nombre = input("Nuevo nombre: ")
            if nuevo_nombre:
                producto.nombre = nuevo_nombre
                print("Nombre modificado correctamente")
        elif opcion == "2":
            nuevo_precio_compra = float(input("Nuevo precio de compra: "))
            if nuevo_precio_compra:
                producto.precio_compra = nuevo_precio_compra
                print("Precio de compra modificado correctamente")
        elif opcion == "3":
            nuevo_precio_venta = float(input("Nuevo precio de venta: "))
            if nuevo_precio_venta:
                producto.precio_venta = nuevo_precio_venta
                print("Precio de venta modificado correctamente")
        elif opcion == "4":
            nuevo_stock = int(input("Nuevo stock disponible: "))
            if nuevo_stock:
                producto.stock = nuevo_stock
                print("Stock modificado correctamente")
        else:
            print("Modificación cancelada")

    def eliminar_producto(self):
        system("cls")
        print("=== Eliminar Producto ===")
        try:
            id_producto = int(input("Ingrese el ID del producto a eliminar: "))
            index_to_delete = -1
            for i, producto in enumerate(self.productos):
                if producto.id == id_producto:
                    index_to_delete = i
                    break
            if index_to_delete >= 0:
                producto = self.productos[index_to_delete]
                confirmacion = input(f"¿Está seguro de eliminar el producto {producto.nombre}? (s/n): ").lower()
                if confirmacion == 's':
                    self.productos.pop(index_to_delete)
                    print("Producto eliminado exitosamente")
                else:
                    print("Operación cancelada")
            else:
                print("Error: No se encontró un producto con ese ID")
        except ValueError:            
            print("Error: El ID debe ser un número entero") 

    def registrar_venta(self):
        system("cls")
        print("=== Registrar Venta ===")

        try:
            id_venta = input("ID de la venta: ")

            dia = input("Día de la venta (DD): ")
            mes = input("Mes de la venta (MM): ")
            anio = input("Año de la venta (YYYY): ")
            fecha = f"{dia}/{mes}/{anio}"

            # Buscar Vendedor
            id_vendedor = int(input("ID del vendedor: "))
            vendedor = None
            for v in self.vendedores:
                if v.id == id_vendedor:
                    vendedor = v
                    break
            if not vendedor:
                print("Vendedor no encontrado.")
                return
            print(f"Nombre del vendedor: {vendedor.nombre}")

            # Buscar Cliente
            id_cliente = int(input("ID del cliente: "))
            cliente = None
            for c in self.clientes:
                if c.id == id_cliente:
                    cliente = c
                    break
            if not cliente:
                print("Cliente no encontrado.")
                return
            print(f"Nombre del cliente: {cliente.nombre}")

            # Producto
            id_producto = int(input("ID del producto: "))
            producto = None
            for p in self.productos:
                if p.id == id_producto:
                    producto = p
                    break
            if not producto:
                print("Producto no encontrado.")
                return
            print(f"Nombre del producto: {producto.nombre}")
            print(f"Valor unitario: {producto.precio_venta}")

            cantidad = int(input("Cantidad del producto: "))

            if cantidad > producto.stock:
                print("No hay suficiente stock disponible.")
                return

            # Actualizar stock
            producto.stock -= cantidad

            from venta import Venta
            nueva_venta = Venta(id_venta, fecha, cliente, vendedor, [producto], [cantidad])
            self.ventas.append(nueva_venta)

            print("Venta registrada exitosamente.")
            print("----------------------------------")
            nueva_venta.mostrar_detalle()

        except ValueError:
            print("Error: Ingresaste un valor no válido.")

    def listar_ventas(self):
        system("cls")
        print("=== Lista de Ventas ===")

        if not self.ventas:
            print("No hay ventas registradas.")
        else:
            for venta in self.ventas:
                print(f"\nID Venta: {venta.id}")
                print(f"Fecha: {venta.fecha}")
                print(f"Cliente: {venta.cliente.nombre}")
                print(f"Vendedor: {venta.vendedor.nombre}")
                print("Productos vendidos:")

                for prod, cant in zip(venta.productos, venta.cantidades):
                    print(f"  - {prod.nombre} x{cant} @ ${prod.precio_venta:,.2f} c/u")

                print(f"Total de la venta: ${venta.total:,.2f}")
                print("-" * 30)

        input("\nPresione Enter para continuar...")

    def modificar_venta(self):
        system("cls")
        print("=== Modificar Venta ===\n")

        if not self.ventas:
            print("No hay ventas registradas.")
            input("Enter para continuar...")
            return

        id_venta = input("ID de la venta a modificar: ")
        venta = next((v for v in self.ventas if v.id == id_venta), None)

        if not venta:
            print("Venta no encontrada.")
            input("Enter para continuar...")
            return

        # Nueva fecha
        print("\nFecha actual:", venta.fecha)
        dia = input("Nuevo día: ")
        mes = input("Nuevo mes: ")
        anio = input("Nuevo año: ")
        venta.fecha = f"{dia}/{mes}/{anio}"

        # Nuevo cliente
        id_cliente = input("Nuevo ID cliente: ")
        cliente = next((c for c in self.clientes if c.id == id_cliente), None)
        if cliente:
            venta.cliente = cliente
        else:
            print("Cliente no encontrado. Se conserva el actual.")

        # Nuevas cantidades
        nuevas_cantidades = []
        print("\nActualizar cantidades:")
        for producto, actual in zip(venta.productos, venta.cantidades):
            entrada = input(f"{producto.nombre} (actual: {actual}): ")
            try:
                cantidad = int(entrada)
            except:
                cantidad = actual
            nuevas_cantidades.append(cantidad)

        venta.cantidades = nuevas_cantidades
        venta.total = venta.calcular_total()

        print("\nVenta actualizada con éxito.")
        input("Enter para continuar...")



# Inversiones 
    def reporte_inversion_total(self):
        system("cls")
        print("=== Reporte de Inversión Total ===")
        inversion_total = 0

        for producto in self.productos:
            inversion_total += producto.precio_compra * producto.stock

        print(f"La inversión total en productos es: ${inversion_total:,.2f}")
        input("Presione Enter para continuar...")


    def mostrar_menu_principal(self):        
        while True:
            system("cls")
            print("+*******************************+")
            print("=================================")
            print("|     Tienda Carlos Andres      |")
            print("=================================")
            print("******** Menu Principal *********")
            print("| a. Registrar Vendedor         |")
            print("| b. Listar Vendedores          |")
            print("| c. Modificar Vendedor         |")
            print("| d. Eliminar Vendedor          |")
            print("| e. Registrar Cliente          |")
            print("| f. Listar Clientes            |")
            print("| g. Modificar Cliente          |")
            print("| h. Eliminar Cliente           |")
            print("| i. Registrar Producto         |")
            print("| j. Listar Productos           |")
            print("| k. Productos con Stock        |")
            print("| l. Productos sin Stock        |")
            print("| m. Modificar Producto         |")
            print("| n. Eliminar Producto          |")
            print("| o. Registrar Venta            |")
            print("| p. Listar Ventas              |")
            print("| q. Modificar Venta            |")
            print("| r. Ventas por Producto        |")
            print("| s. Ventas por Fecha           |")
            print("| t. Ventas por Vendedor        |")
            print("| u. Compras por Cliente        |")
            print("| v. Reporte Inversión Total    |")
            print("| w. Inversión por Producto     |")
            print("| x. Ganancias Totales          |")
            print("| y. Ganancias por Producto     |")
            print("| z. Salir                      |")
            print("\-------------------------------/")
            opcion = input("Seleccione una opción: ").lower()
            if opcion == "a" or opcion == "A":
                print("Registro de vendedor hecho satisfactoriamente")
                self.registrar_vendedor()
            elif opcion == "b" or opcion == "B":
                print("Lista de vendedores hecho satisfactoriamente")
                self.listar_vendedores()
            elif opcion == "c" or opcion == "C":
                print("Modificado el vendedor hecho satisfactoriamente")
                self.modificar_vendedor()
            elif opcion == "d" or opcion == "D":
                print("El Vendedor fue eliminado con exito")
                self.eliminar_vendedor()
            elif opcion == "e" or opcion == "E":
                print("El Cliente fue registrado con exito")
                self.registrar_cliente()
            elif opcion == "f" or opcion == "F":
                print("Se listaron los clientes") 
                self.listar_clientes()
            elif opcion == "g" or opcion == "G":
                print("Se modificó el cliente")
                self.modificar_cliente()
            elif opcion == "h" or opcion == "H":
                print("Eliminar Cliente")
                self.eliminar_cliente()
            elif opcion == "i" or opcion == "I":
                print("Se registro el producto")
                self.registrar_producto()
            elif opcion == "j" or opcion == "J":
                print("Listas de productos")
                self.listar_productos()
            elif opcion == "k" or opcion == "K":
                print("Productos con Stock")
                self.listar_productos_con_stock()
            elif opcion == "l" or opcion == "L":
                print("Productos sin Stock")
                self.listar_productos_sin_stock()
            elif opcion == "m" or opcion == "M":
                print("Productos Modificados")
                self.modificar_producto()
            elif opcion == "n" or opcion == "N":
                print("Productos Eliminados")
                self.eliminar_producto()
            elif opcion == "o" or opcion == "O":
                print("venta  registrada con exito")
                self.registrar_venta()
            elif opcion == "p" or opcion == "P":
                self.listar_ventas()
            elif opcion == "q" or opcion == "Q":
                self.modificar_venta()
            elif opcion == "r":
                print("Ventas por Producto (no implementado)")
            elif opcion == "s":
                print("Ventas por Fecha (no implementado)")
            elif opcion == "t":
                print("Ventas por Vendedor (no implementado)")
            elif opcion == "u":
                print("Compras por Cliente (no implementado)")
            elif opcion == "v" or opcion == "V":
                self.reporte_inversion_total()
            elif opcion == "w":
                print("Inversión por Producto (no implementado)")
            elif opcion == "x":
                print("Ganancias Totales (no implementado)")
            elif opcion == "y":
                print("Ganancias por Producto (no implementado)")
            elif opcion == "z" or opcion == "Z":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida")
            input("Presione Enter para continuar...")
if __name__ == '__main__':
    menu = Menu()
    menu.mostrar_menu_principal()