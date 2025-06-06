# detectar_anomalias.py

class DetectarAnomalias:
    def execute(self, df):
        """
        Detecta anomalías en las ventas utilizando el método de Z-score.
        Se considera una anomalía si el Z-score es mayor a 3 o menor a -3.
        El Z-score se calcula como:
        Z = (X - media) / desviacion_estandar
        Donde:
        - X es el valor actual
        - media es la media de la serie
        - desviacion_estandar es la desviación estándar de la serie
        """
