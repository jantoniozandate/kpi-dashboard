# promedio_ventas_diarias.py
import pandas as pd

class PromedioVentasDiarias:
    def execute(self, df):

        df['fecha'] = pd.to_datetime(df['fecha'])  # Asegura que sea tipo fecha
        total_ventas = df["total"].sum()
        numero_dias = df["fecha"].dt.date.nunique()  # número de días distintos
        return round(total_ventas / numero_dias, 2)


        """
        Calcula el promedio de ventas diarias.
        Para simplificar: promedio = total de ventas / número de días.
        """

