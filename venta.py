from datetime import datetime

class Venta:
    def __init__(self, id, fecha, cliente, vendedor, productos, cantidades):
        self.id = id
        self.fecha = fecha  # datetime.date
        self.cliente = cliente
        self.vendedor = vendedor
        self.productos = productos
        self.cantidades = cantidades
        self.total = self.calcular_total()

    @classmethod
    def crear_venta(cls, id_venta, fecha, cliente, vendedor, productos, cantidades):
        if isinstance(fecha, str):
            try:
                fecha = datetime.strptime(fecha, "%Y-%m-%d").date()
            except ValueError:
                raise ValueError("Formato de fecha inválido. Usa YYYY-MM-DD.")

        if not productos or not cantidades:
            raise ValueError("No se agregaron productos.")

        if len(productos) != len(cantidades):
            raise ValueError("Productos y cantidades no coinciden.")

        for producto, cantidad in zip(productos, cantidades):
            if cantidad <= 0:
                raise ValueError(f"La cantidad del producto '{producto.nombre}' debe ser mayor que cero.")
            if cantidad > producto.stock:
                raise ValueError(f"Stock insuficiente para el producto '{producto.nombre}'. Disponible: {producto.stock}, Solicitado: {cantidad}")

        # Descontar stock
        for producto, cantidad in zip(productos, cantidades):
            producto.stock -= cantidad

        return cls(id_venta, fecha, cliente, vendedor, productos, cantidades)

    def calcular_total(self):
        total = 0
        for producto, cantidad in zip(self.productos, self.cantidades):
            total += producto.precio_venta * cantidad
        return round(total, 2)

    def mostrar_detalle(self):
        print("ID de la venta:", self.id)
        print("Fecha:", self.fecha)
        print("Cliente:", self.cliente.nombre)
        print("Vendedor:", self.vendedor.nombre)
        print("Productos vendidos:")
        for producto, cantidad in zip(self.productos, self.cantidades):
            print("- Nombre del producto:", producto.nombre)
            print("  Precio unitario:", producto.precio_venta)
            print("  Cantidad:", cantidad)
            print("  Subtotal:", round(producto.precio_venta * cantidad, 2))
        print("Total de la venta:", self.total)

    @staticmethod
    def obtener_ventas_por_producto(lista_ventas, id_producto):
        ventas_filtradas = []
        total_recaudado = 0
        total_ganancia = 0

        for venta in lista_ventas:
            for producto, cantidad in zip(venta.productos, venta.cantidades):
                if producto.id == id_producto:
                    subtotal = cantidad * producto.precio_venta
                    ganancia = (producto.precio_venta - producto.precio_compra) * cantidad

                    ventas_filtradas.append({
                        "venta": venta,
                        "cantidad": cantidad,
                        "subtotal": subtotal,
                        "ganancia": ganancia,
                        "producto": producto
                    })

                    total_recaudado += subtotal
                    total_ganancia += ganancia

        # Ordenar por fecha si se desea
        ventas_filtradas.sort(key=lambda v: v["venta"].fecha)

        return ventas_filtradas, total_recaudado, total_ganancia

    @staticmethod
    def obtener_ventas_por_fecha(lista_ventas, fecha_buscada):
        ventas_filtradas = []
        total_recaudado = 0
        total_ganancia = 0

        for venta in lista_ventas:
            if venta.fecha == fecha_buscada:
                ventas_filtradas.append(venta)
                total_recaudado += venta.total

                for i in range(len(venta.productos)):
                    producto = venta.productos[i]
                    cantidad = venta.cantidades[i]
                    ganancia = (producto.precio_venta - producto.precio_compra) * cantidad
                    total_ganancia += ganancia

        return ventas_filtradas, total_recaudado, total_ganancia
    

    @staticmethod
    def obtener_ventas_por_vendedor(lista_ventas, id_vendedor):
        ventas_filtradas = []
        total_recaudado = 0
        total_ganancia = 0

        for venta in lista_ventas:
            if venta.vendedor.id == id_vendedor:
                ventas_filtradas.append(venta)
                total_recaudado += venta.total

                for i in range(len(venta.productos)):
                    producto = venta.productos[i]
                    cantidad = venta.cantidades[i]
                    ganancia = (producto.precio_venta - producto.precio_compra) * cantidad
                    total_ganancia += ganancia

        return ventas_filtradas, total_recaudado, total_ganancia
    
    @staticmethod
    def obtener_compras_por_cliente(lista_ventas, id_cliente):
        compras_filtradas = []
        total_recaudado = 0
        total_ganancia = 0

        for venta in lista_ventas:
            if venta.cliente.id == id_cliente:
                compras_filtradas.append(venta)
                total_recaudado += venta.total

                for i in range(len(venta.productos)):
                    producto = venta.productos[i]
                    cantidad = venta.cantidades[i]
                    ganancia = (producto.precio_venta - producto.precio_compra) * cantidad
                    total_ganancia += ganancia

        return compras_filtradas, total_recaudado, total_ganancia
    


