# productos_mas_vendidos.py

class ProductosMasVendidos:
    def execute(self, df):
        """
        Obtiene los productos más vendidos.
        Para simplificar: se considera más vendido al producto con más unidades vendidas.
        Se agrupa por producto y se suma la cantidad vendida.
        Luego se ordena de mayor a menor y se seleccionan los primeros 10 productos.
        """
