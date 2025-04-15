# calcular_retencion_clientes.py

class CalcularRetencionClientes:
    def execute(self, df):
        """
        Calcula el porcentaje de retención de clientes.
        Para simplificar: retención = (# clientes que compraron más de una vez) / (# total de clientes únicos)
        """
        if "cliente_id" not in df.columns:
            return "El DataFrame no contiene la columna 'cliente_id'"

        total_clientes = df["cliente_id"].nunique()
        clientes_recurrentes = df["cliente_id"].value_counts()
        clientes_retenidos = (clientes_recurrentes > 1).sum()

        if total_clientes == 0:
            return "No hay clientes en el archivo."

        retencion = clientes_retenidos / total_clientes
        return f"Retención de clientes: {retencion:.2%}"
