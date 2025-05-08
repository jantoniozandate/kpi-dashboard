# clientes_nuevos.py

class CalcularRetencionClientes:
    def execute(self, df):
        """
        Regresa los clientes nuevos.
        Para simplificar: nuevos = (# clientes que compraron por primera vez)
        """

   if "clientes_id" not in df.columns:
        return "El DataFrame no contiene la columna clientes_id"

    frecuencia_clientes = df["clientes_id "].value_counts()

    clientes_nuevos = (frecuencia_clientes == 1).sum()

   if frecuencia_clientes.empty:
       return"No hhay clientes en el archivo"
       return f"Numero de clientes nuevos [Clientes_nuevos]"