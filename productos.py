class Producto:
    def __init__(self, id, nombre, precio_compra, precio_venta, stock):
        self.id = id
        self.nombre = nombre
        self.precio_compra = precio_compra
        self.precio_venta = precio_venta
        self.stock = stock

    def calcular_valor_unitario(self):
        ganancia = self.precio_compra * 0.30
        return round(self.precio_compra + ganancia, 2)
    
    @staticmethod
    def crear_producto(id, nombre, precio_compra, stock):
        # Calculamos el valor unitario del producto en un 30% de descuento
        precio_venta = round(precio_compra * 1.3, 2)
        return Producto(id, nombre, precio_compra, precio_venta, stock)