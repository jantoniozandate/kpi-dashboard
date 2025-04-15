# generar_reporte_texto.py

class GenerarReporteTexto:
    def execute(self, df):
        """
        Genera un reporte de texto con las estadísticas de ventas.
        Usa todas las funciones de KPI para generar el reporte.
        """

        """
        Recibe los resultados de todos los métodos de KPI y los imprime en un reporte de texto en consola.
        
        :param resultados_kpi: Diccionario con los nombres de los KPI como claves y sus resultados como valores.
        """
        reporte = "Reporte de KPI:\n"
        reporte += "=" * 20 + "\n"
        for kpi, resultado in resultados_kpi.items():
            reporte += f"{kpi}: {resultado}\n"
        reporte += "=" * 20
        print(reporte)