from datetime import datetime
class Venta:
    def __init__(self, id, fecha, cliente, vendedor, productos, cantidades):
        self.id = id
        self.fecha = fecha
        self.cliente = cliente
        self.vendedor = vendedor
        self.productos = productos
        self.cantidades = cantidades
        self.total = self.calcular_total()
    
    def calcular_total(self):
            total = 0
            for i in range(len(self.productos)):
                producto = self.productos[i]
                cantidad = self.cantidades[i]
                total += producto.precio_venta * cantidad
            return round(total, 2)

    def mostrar_detalle(self):
        print("ID de la venta:", self.id)
        print("Fecha:", self.fecha)
        print("Cliente:", self.cliente.nombre)
        print("Vendedor:", self.vendedor.nombre)
        print("Productos vendidos:")
        for i in range(len(self.productos)):
            producto = self.productos[i]
            cantidad = self.cantidades[i]
            print("- Nombre del producto:", producto.nombre)
            print("  Precio unitario:", producto.precio_venta)
            print("  Cantidad:", cantidad)
            print("  Subtotal:", producto.precio_venta * cantidad)
        print("Total de la venta:", self.total)