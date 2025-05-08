# ventas_por_canal.py

class VentasPorCanal:
    def execute(self, df):
        """
        Calcula las ventas por canal.
        Para simplificar: ventas por canal = suma de ventas por canal.
        """
        group = df.groupby('canal')
        result = ""
        for canal, data in group:
            result += f"Canal: {canal}, Ventas: {data.shape[0]}\n"
        return result