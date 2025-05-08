# conversion_porcentaje.py

class ConversionPorcentaje:
    def execute(self, df):
        """
        Calcula el porcentaje de conversión.
        Para simplificar: conversión = (# ventas) / (# visitas)
        """
        ventas = df["cantidad"].sum()
        visitas = df["visitas"].sum()

        return ventas / visitas
