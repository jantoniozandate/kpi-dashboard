# productos_con_mayor_margen.py

class ProductosConMayorMargen:
    def execute(self, df):
        
        for producto in df:
            producto["margen"] = producto["precio_unitario"] - producto["costo_unitario"]

        productos_ordenados = sorted(df, key=lambda x: x["margen"], reverse=True)

        for producto in productos_ordenados[:3]:  #Los 3 productos con mayor margen
            print(f"ID: {producto['producto_id']}, Nombre: {producto['nombre_producto']}, Margen: {producto['margen']}")

        """
        Obtiene los productos con mayor margen de ganancia.
        Para simplificar: margen = precio de venta - costo
        """
