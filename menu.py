from os import system
from vendedor import Vendedor
from clientes import Cliente
from productos import Producto
from venta import Venta
from datetime import datetime, date
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
                print("Error - La edad debe estar entre 18 y 65 años")
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
            if nombre == "" or any(char.isdigit() for char in nombre):
                print("Error - El nombre no puede estar vacío ni contener números")
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
            
            # Calculate selling price with 30% markup
            precio_venta = precio_compra * 1.30
            print(f"Precio de venta calculado (30% sobre costo): ${precio_venta:.2f}")
            stock = int(input("Stock (Cantidad) disponible: "))
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
        print("4. Stock (Cantidad) disponible:", producto.stock)    
        opcion = input("Seleccione qué desea modificar (1-4) o Enter para cancelar: ")
        if opcion == "1":
            nuevo_nombre = input("Nuevo nombre: ")
            if nuevo_nombre:
                producto.nombre = nuevo_nombre
                print("Nombre modificado correctamente")
        elif opcion == "2":
            try:
                nuevo_precio_compra = float(input("Nuevo precio de compra: "))
                if nuevo_precio_compra <= 0:
                    print("El precio debe ser mayor a 0")
                    input("Presione Enter para continuar...")
                    return
                producto.precio_compra = nuevo_precio_compra
                # Update selling price with 30% markup when purchase price changes
                producto.precio_venta = nuevo_precio_compra * 1.30
                print("Precio de compra modificado correctamente")
                print(f"Nuevo precio de venta (30% markup): ${producto.precio_venta:.2f}")
            except ValueError:
                print("Error - Debe ingresar un número válido")
                input("Presione Enter para continuar...")
                return
        elif opcion == "3":
            try:
                nuevo_precio_venta = float(input("Nuevo precio de venta: "))
                if nuevo_precio_venta <= 0:
                    print("El precio debe ser mayor a 0")
                    input("Presione Enter para continuar...")
                    return
                producto.precio_venta = nuevo_precio_venta
                print("Precio de venta modificado correctamente")
            except ValueError:
                print("Error - Debe ingresar un número válido")
                input("Presione Enter para continuar...")
                return
        elif opcion == "4":
            try:
                nuevo_stock = int(input("Nuevo stock disponible: "))
                if nuevo_stock <= 0:
                    print("El stock debe ser mayor a 0")
                    input("Presione Enter para continuar...")
                    return
                producto.stock = nuevo_stock
                print("Stock (Cantidad) modificado correctamente")
            except ValueError:
                print("Error - Debe ingresar un número válido")
                input("Presione Enter para continuar...")
                return
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
        print("=== Registrar Venta ===")
        id_venta = input("ID de la venta: ").strip()
        if any(v.id == id_venta for v in self.ventas):
            print(" Ya existe una venta con ese ID.")
            return
        try:
            dia = int(input("Día (DD): "))
            mes = int(input("Mes (MM): "))
            anio = int(input("Año (YYYY): "))
            fecha = datetime(anio, mes, dia).date() 
            if fecha > date.today():
                print(" No se puede registrar ventas futuras.")
                return
        except:
            print(" Fecha inválida.")
            return
        try:
            id_vendedor = int(input("ID del vendedor: "))
            vendedor = next(v for v in self.vendedores if v.id == id_vendedor)
        except:
            print("Vendedor no encontrado.")
            return
        try:
            id_cliente = int(input("ID del cliente: "))
            cliente = next(c for c in self.clientes if c.id == id_cliente)
        except:
            print(" Cliente no encontrado.")
            return
        productos = []
        cantidades = []
        while True:
            try:
                id_producto = int(input("ID del producto: "))
                producto = next(p for p in self.productos if p.id == id_producto)
                cantidad = int(input(f"Cantidad de {producto.nombre} (Stock: {producto.stock}): "))
                productos.append(producto)
                cantidades.append(cantidad)
            except:
                print(" Error al agregar producto.")
                continue
            if input("¿Agregar otro producto? (s/n): ").lower() != 's':
                break
        try:
            venta = Venta.crear_venta(id_venta, fecha, cliente, vendedor, productos, cantidades)
            self.ventas.append(venta)
            print("Venta registrada con éxito.")
            venta.mostrar_detalle()
        except ValueError as err:
            print(f" Error: {err}")
    def listar_ventas(self):
        system("cls")
        print("=== Lista de Ventas ===")
        if not self.ventas:
            print("No hay ventas registradas.")
        else:
            total_general = 0  # acumulador
            for venta in self.ventas:
                print(f"\nID Venta: {venta.id}")
                print(f"Fecha: {venta.fecha}")
                print(f"Cliente: {venta.cliente.nombre}")
                print(f"Vendedor: {venta.vendedor.nombre}")
                print("Productos vendidos:")
                for prod, cant in zip(venta.productos, venta.cantidades):
                    print(f"  - {prod.nombre} x{cant} @ ${prod.precio_venta:,.2f} c/u")
                print(f"Total de la venta: ${venta.total:,.2f}")
                print("---------------------------------------------------------------")
                total_general += venta.total
            # Mostrar total acumulado de todas las ventas
            print(f"\nTOTAL GENERAL DE VENTAS: ${total_general:,.2f}")
        input("\nPresione Enter para continuar...")
    def modificar_venta(self):
        system("cls")
        print("=== Modificar Venta ===\n")
        if not self.ventas:
            print("No hay ventas registradas.")
            input("Presione Enter para continuar...")
            return
        id_venta = input("ID de la venta a modificar: ")
        # Buscar venta
        venta = next((v for v in self.ventas if str(v.id) == id_venta), None)
        if not venta:
            print("Venta no encontrada.")
            input("Presione Enter para continuar...")
            return
        print(f"\nFecha actual: {venta.fecha}")
        dia = input("Nuevo día: ")
        mes = input("Nuevo mes: ")
        anio = input("Nuevo año: ")
        venta.fecha = f"{dia}/{mes}/{anio}"
        print("\nClientes disponibles:")
        for c in self.clientes:
            print(f"ID: {c.id} | Nombre: {c.nombre}")
        id_cliente = input("Nuevo ID cliente: ")
        if id_cliente.isdigit():
            id_cliente = int(id_cliente)
            cliente = next((c for c in self.clientes if c.id == id_cliente), None)
            if cliente:
                venta.cliente = cliente
                print("Cliente actualizado.")
            else:
                print("Cliente no encontrado. Se conserva el actual.")
        else:
            print("ID inválido. Se conserva el actual.")
        nuevas_cantidades = []
        print("\nActualizar cantidades:")
        for producto, actual in zip(venta.productos, venta.cantidades):
            entrada = input(f"{producto.nombre} (actual: {actual}): ")
            if entrada.isdigit():
                nuevas_cantidades.append(int(entrada))
            else:
                nuevas_cantidades.append(actual)
        venta.cantidades = nuevas_cantidades
        venta.total = venta.calcular_total()
        print("Venta actualizada con éxito.")
        input("Presione Enter para continuar...")
    def mostrar_ventas_por_producto(self):
        print("=== Ventas por Producto ===")
        if not self.productos:
            print("No hay productos registrados.")
            return
        for p in self.productos:
            print(f"ID: {p.id} | Nombre: {p.nombre}")
        try:
            id_producto = int(input("\nIngrese el ID del producto: "))
        except ValueError:
            print("ID inválido.")
            return
        producto = next((p for p in self.productos if p.id == id_producto), None)
        if not producto:
            print("Producto no encontrado.")
            return
        ventas_filtradas, total_recaudado, total_ganancia = Venta.obtener_ventas_por_producto(self.ventas, id_producto)
        if not ventas_filtradas:
            print("No hay ventas registradas para este producto.")
            return
        print(f"\n Detalle de ventas para el producto: {producto.nombre}\n")
        for v in ventas_filtradas:
            venta = v["venta"]
            producto_vendido = v["producto"]
            print(f"ID Venta: {venta.id}")
            print(f"Fecha: {venta.fecha}")
            print(f"Cliente: {venta.cliente.nombre}")
            print(f"Vendedor: {venta.vendedor.nombre}")
            print(f"Cantidad vendida: {v['cantidad']}")
            print(f"Precio unitario: ${producto_vendido.precio_venta:.2f}")
            print(f"Subtotal: ${v['subtotal']:.2f}")
            print(f"Ganancia: ${v['ganancia']:.2f}")
            print("------------------------------------------------------" )
        # 
        print(f"\nMonto total recaudado: ${total_recaudado:.2f}")
        print(f"Ganancia total obtenida: ${total_ganancia:.2f}")
    def mostrar_ventas_por_fecha(self):
        print("=== Ventas por Fecha ===")
        try:
            entrada = input("Ingrese la fecha (formato: YYYY-MM-DD): ").strip()
            fecha_buscada = datetime.strptime(entrada, "%Y-%m-%d").date()
            if fecha_buscada > date.today():
                print(" No se permiten fechas futuras.")
                return
        except ValueError:
            print(" Fecha inválida. el formato es : YYYY-MM-DD y que sea una fecha real.")
            return
        ventas_filtradas, total_recaudado, total_ganancia = Venta.obtener_ventas_por_fecha(self.ventas, fecha_buscada)
        if not ventas_filtradas:
            print("No hay ventas registradas para esa fecha.")
            return
        print(f"Ventas realizadas el día {fecha_buscada}: ")
        for venta in ventas_filtradas:
            print(f"ID Venta: {venta.id}")
            print(f"Cliente: {venta.cliente.nombre}")
            print(f"Vendedor: {venta.vendedor.nombre}")
            print("Productos vendidos:")
            for i in range(len(venta.productos)):
                producto = venta.productos[i]
                cantidad = venta.cantidades[i]
                subtotal = producto.precio_venta * cantidad
                ganancia = (producto.precio_venta - producto.precio_compra) * cantidad
                print(f"- {producto.nombre} | Precio: ${producto.precio_venta} | Cantidad: {cantidad} | Subtotal: ${subtotal:.2f} | Ganancia: ${ganancia:.2f}")
            print(f"Total de la venta: ${venta.total:.2f}")
            print("--------------------------------------------------------------------------------------------------------")
        print(f" Monto total recaudado ese día: ${total_recaudado:.2f}")
        print(f"Ganancia total del día: ${total_ganancia:.2f}")
    def mostrar_ventas_por_vendedor(self):
        print("=== Ventas por Vendedor ===")
        try:
            id_vendedor = int(input("Ingrese el ID del vendedor: "))
        except ValueError:
            print("ID inválido. Debe ser un número.")
            return
        ventas_filtradas, total_recaudado, total_ganancia = Venta.obtener_ventas_por_vendedor(self.ventas, id_vendedor)
        if not ventas_filtradas:
            print("No hay ventas registradas para este vendedor.")
            return
        print(f"\n Ventas realizadas por el vendedor con ID {id_vendedor}:\n")
        for venta in ventas_filtradas:
            print(f"ID Venta: {venta.id}")
            print(f"Fecha: {venta.fecha}")
            print(f"Cliente: {venta.cliente.nombre}")
            print("Productos vendidos:")
            for i in range(len(venta.productos)):
                producto = venta.productos[i]
                cantidad = venta.cantidades[i]
                subtotal = producto.precio_venta * cantidad
                ganancia = (producto.precio_venta - producto.precio_compra) * cantidad
                print(f"- {producto.nombre} | Precio: ${producto.precio_venta} | Cantidad: {cantidad} | Subtotal: ${subtotal:.2f} | Ganancia: ${ganancia:.2f}")
            print(f"Total de la venta: ${venta.total:.2f}")
            print("-" * 40)
        print(f"\n Monto total recaudado por el vendedor: ${total_recaudado:.2f}")
        print(f" Ganancia total generada por el vendedor: ${total_ganancia:.2f}")
    def mostrar_compras_por_cliente(self):
        print("=== Compras por Cliente ===")
        try:
            id_cliente = int(input("Ingrese el ID del cliente: "))
        except ValueError:
            print("ID inválido. Debe ser un número.")
            return
        compras, total_recaudado, total_ganancia = Venta.obtener_compras_por_cliente(self.ventas, id_cliente)
        if not compras:
            print("No hay compras registradas para este cliente.")
            return
        print(f"\nCompras realizadas por el cliente con ID {id_cliente}:\n")
        for venta in compras:
            print(f"ID Venta: {venta.id}")
            print(f"Fecha: {venta.fecha}")
            print(f"Vendedor: {venta.vendedor.nombre}")
            print("Productos comprados:")
            for i in range(len(venta.productos)):
                producto = venta.productos[i]
                cantidad = venta.cantidades[i]
                subtotal = producto.precio_venta * cantidad
                ganancia = (producto.precio_venta - producto.precio_compra) * cantidad
                print(f"- {producto.nombre} | Precio: ${producto.precio_venta} | Cantidad: {cantidad} | Subtotal: ${subtotal:.2f} | Ganancia: ${ganancia:.2f}")
            print(f"Total de la compra: ${venta.total:.2f}")
            print("-" * 40)
        print(f"\nMonto total de compras del cliente: ${total_recaudado:.2f}")
        print(f"Ganancia generada por el cliente: ${total_ganancia:.2f}")
        input("Presione Enter para continuar...")
# Inversiones 
    def reporte_inversion_total(self):
        system("cls")
        print("=== Reporte de Inversión Total ===")
        
        if not self.productos:
            print("No hay productos registrados para calcular la inversión")
            input("Presione Enter para continuar...")
            return
            
        inversion_total = 0
        print("\nDesglose por producto:")
        print("-" * 50)
        
        for producto in self.productos:
            inversion_producto = producto.precio_compra * producto.stock
            inversion_total += inversion_producto
            print(f"Producto: {producto.nombre}")
            print(f"Precio de compra: ${producto.precio_compra:,.2f}")
            print(f"Stock: {producto.stock}")
            print(f"Inversión: ${inversion_producto:,.2f}")
            print("-" * 50)
            
        print(f"\nLa inversión total en inventario es: ${inversion_total:,.2f}")
        input("Presione Enter para continuar...")

    def mostrar_inversion_por_producto(self):
        system("cls")
        print("=== Reporte de Inversión por Producto ===")
        
        if not self.productos:
            print("No hay productos registrados")
            input("Presione Enter para continuar...")
            return
            
        try:
            id_producto = int(input("Ingrese el ID del producto: "))
            if id_producto <= 0:
                print("El ID debe ser un número positivo")
                input("Presione Enter para continuar...")
                return
                
            producto = next((p for p in self.productos if p.id == id_producto), None)
            
            if producto:
                print("\nDetalles de inversión:")
                print("-" * 50)
                print(f"Producto: {producto.nombre}")
                print(f"Precio de compra: ${producto.precio_compra:,.2f}")
                print(f"Stock actual: {producto.stock}")
                inversion = producto.precio_compra * producto.stock
                print(f"Inversión Total: ${inversion:,.2f}")
            else:
                print("Producto no encontrado")
                
        except ValueError:
            print("Error: El ID debe ser un número entero")
            
        input("Presione Enter para continuar...")

    def mostrar_ganancias_totales(self):
        """Calculate and display total profits from all sales"""
        system("cls")
        print("=== Reporte de Ganancias Totales ===")
        
        if not self.ventas:
            print("No hay ventas registradas para calcular ganancias")
            input("Presione Enter para continuar...")
            return
            
        total_ganancias = 0
        print("\nDesglose de ganancias por venta:")
        print("-" * 50)
        
        for venta in self.ventas:
            ganancia_venta = 0
            print(f"Venta ID: {venta.id}")
            print(f"Fecha: {venta.fecha}")
            
            for i in range(len(venta.productos)):
                producto = venta.productos[i]
                cantidad = venta.cantidades[i]
                ganancia_producto = (producto.precio_venta - producto.precio_compra) * cantidad
                ganancia_venta += ganancia_producto
                
                print(f"Producto: {producto.nombre}")
                print(f"Cantidad: {cantidad}")
                print(f"Ganancia: ${ganancia_producto:,.2f}")
                
            total_ganancias += ganancia_venta
            print(f"Ganancia de la venta: ${ganancia_venta:,.2f}")
            print("-" * 50)
            
        print(f"\nGanancia total de todas las ventas: ${total_ganancias:,.2f}")
        input("Presione Enter para continuar...")
    def mostrar_ganancias_por_producto(self):
        try:
            id_producto = int(input("Ingrese el ID del producto: "))
        except ValueError:
            print("ID inválido.")
            return
        nombre_producto = ""
        total_ganancia = 0
        for venta in self.ventas:
            for i in range(len(venta.productos)):
                producto = venta.productos[i]
                cantidad = venta.cantidades[i]
                if producto.id == id_producto:
                    nombre_producto = producto.nombre
                    ganancia = (producto.precio_venta - producto.precio_compra) * cantidad
                    total_ganancia += ganancia
        if nombre_producto:
            print(f"{nombre_producto}: Ganancia total = ${total_ganancia:.2f}")
        else:
            print("Producto no encontrado en las ventas.")
    def mostrar_menu_principal(self):        
        while True:
            system("cls")
            print("╔══════════════════════════════════╗")
            print("║      TIENDA CARLOS ANDRES        ║")
            print("╠══════════════════════════════════╣")
            print("║         MENÚ PRINCIPAL           ║")
            print("╠══════════════════════════════════╣")
            print("║ [A] Registrar Vendedor           ║")
            print("║ [B] Listar Vendedores            ║")
            print("║ [C] Modificar Vendedor           ║")
            print("║ [D] Eliminar Vendedor            ║")
            print("╠══════════════════════════════════╣")
            print("║ [E] Registrar Cliente            ║")
            print("║ [F] Listar Clientes              ║")
            print("║ [G] Modificar Cliente            ║")
            print("║ [H] Eliminar Cliente             ║")
            print("╠══════════════════════════════════╣")
            print("║ [I] Registrar Producto           ║")
            print("║ [J] Listar Productos             ║")
            print("║ [K] Productos con Stock          ║")
            print("║ [L] Productos sin Stock          ║")
            print("║ [M] Modificar Producto           ║")
            print("║ [N] Eliminar Producto            ║")
            print("╠══════════════════════════════════╣")
            print("║ [O] Registrar Venta              ║")
            print("║ [P] Listar Ventas                ║")
            print("║ [Q] Modificar Venta              ║")
            print("╠══════════════════════════════════╣")
            print("║ [R] Ventas por Producto          ║")
            print("║ [S] Ventas por Fecha             ║")
            print("║ [T] Ventas por Vendedor          ║")
            print("║ [U] Compras por Cliente          ║")
            print("╠══════════════════════════════════╣")
            print("║ [V] Reporte Inversión Total      ║")
            print("║ [W] Inversión por Producto       ║")
            print("║ [X] Ganancias Totales            ║")
            print("║ [Y] Ganancias por Producto       ║")
            print("╠══════════════════════════════════╣")
            print("║ [Z] Salir                        ║")
            print("╚══════════════════════════════════╝")
            opcion = input("Seleccione una opción: ").lower()
            if opcion == "a":
                self.registrar_vendedor()
            elif opcion == "b":
                self.listar_vendedores()
            elif opcion == "c":
                self.modificar_vendedor()
            elif opcion == "d":
                self.eliminar_vendedor()
            elif opcion == "e":
                self.registrar_cliente()
            elif opcion == "f":
                self.listar_clientes()
            elif opcion == "g":
                self.modificar_cliente()
            elif opcion == "h":
                self.eliminar_cliente()
            elif opcion == "i":
                self.registrar_producto()
            elif opcion == "j":
                self.listar_productos()
            elif opcion == "k":
                self.listar_productos_con_stock()
            elif opcion == "l":
                self.listar_productos_sin_stock()
            elif opcion == "m":
                self.modificar_producto()
            elif opcion == "n":
                self.eliminar_producto()
            elif opcion == "o":
                self.registrar_venta()
            elif opcion == "p":
                self.listar_ventas()
            elif opcion == "q":
                self.modificar_venta()
            elif opcion == 'r':
                self.mostrar_ventas_por_producto()
            elif opcion == "s":
                self.mostrar_ventas_por_fecha()
            elif opcion == "t":
                self.mostrar_ventas_por_vendedor()
            elif opcion == "u":
                self.mostrar_compras_por_cliente()
            elif opcion == "v":
                self.reporte_inversion_total()
            elif opcion == "w":
                self.mostrar_inversion_por_producto()
            elif opcion == "x":
                self.mostrar_ganancias_totales()
            elif opcion == "y":
                self.mostrar_ganancias_por_producto()
            elif opcion == "z":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida")
            input("Presione Enter para continuar...")
if __name__ == '__main__':
    menu = Menu()
    menu.mostrar_menu_principal()