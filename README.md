# Sistema de Gestión de Ventas

## Descripción
Este sistema de gestión de ventas es una aplicación desarrollada en Python que permite administrar eficientemente las operaciones comerciales de un negocio. El sistema maneja la gestión integral de vendedores, clientes, productos y ventas, proporcionando una solución completa para el control y seguimiento de las operaciones comerciales.

## Características Principales

### Gestión de Vendedores
- Registro de vendedores con información personal
- Validación de edad (18-65 años)
- Modificación y eliminación de registros
- Control de datos personales (ID, nombre, teléfono, dirección)

### Gestión de Clientes
- Registro completo de información del cliente
- Sistema de identificación única
- Actualización de datos personales
- Seguimiento de historial de compras

### Gestión de Productos
- Control de inventario
- Precios de compra y venta
- Cálculo automático de margen de ganancia (30%)
- Seguimiento de stock
- Alertas de productos sin stock

### Sistema de Ventas
- Registro detallado de transacciones
- Validación de stock disponible
- Cálculo automático de totales
- Múltiples productos por venta
- Registro de fecha de transacción

### Reportes y Análisis
- Ventas por producto
- Ventas por fecha
- Desempeño de vendedores
- Historial de compras por cliente
- Cálculo de ganancias y recaudación

## Requisitos del Sistema
- Python 3.x
- Sistema operativo: Windows/Linux/MacOS

## Estructura del Proyecto
```
activity/
├── menu.py         # Interfaz principal del sistema
├── vendedor.py     # Gestión de vendedores
├── clientes.py     # Gestión de clientes
├── productos.py    # Gestión de productos
└── venta.py        # Procesamiento de ventas
```

## Uso del Sistema
1. Ejecute el archivo menu.py para iniciar el sistema
2. Seleccione la operación deseada del menú principal
3. Siga las instrucciones en pantalla para cada operación

## Validaciones del Sistema
- Control de duplicidad de IDs
- Validación de datos numéricos
- Verificación de stock disponible
- Control de fechas válidas
- Validación de datos obligatorios

## Características de Seguridad
- Validación de entrada de datos
- Prevención de registros duplicados
- Control de acceso a funciones críticas
- Confirmación para operaciones de eliminación

## Mantenimiento
El sistema incluye validaciones robustas y manejo de errores para garantizar la integridad de los datos y una operación fluida.