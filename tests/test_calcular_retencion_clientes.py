# test_calcular_retencion_clientes.py

class CalcularRetencionClientesTest:
    def test_execute(self, df):
        """
        Test para la clase CalcularRetencionClientes.
        Crea un dataframe de ejemplo y verifica que el resultado sea correcto.
        """
        from kpi.calcular_retencion_clientes import CalcularRetencionClientes

        # Crear un dataframe de ejemplo
        data = {
            "cliente_id": [1, 2, 3, 1, 2, 4],
            "venta": [100, 200, 300, 150, 250, 400]
        }
        df = pd.DataFrame(data)

        # Crear una instancia de la clase
        calcular_retencion_clientes = CalcularRetencionClientes()

        # Ejecutar el método
        resultado = calcular_retencion_clientes.execute(df)

        # Verificar el resultado esperado
        assert resultado == "Retención de clientes: 50.00%"