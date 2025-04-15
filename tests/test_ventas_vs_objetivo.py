# test_ventas_vs_objetivo.py

class VentasVSObjetivoTest:
    def test_execute(self, df):
        """
        Test para la clase VentasVSObjetivo.
        Crea un dataframe de ejemplo y verifica que el resultado sea correcto.
        """
        from kpi.ventas_vs_objetivo import VentasVSObjetivo

        # Crear un dataframe de ejemplo
        data = {
            "venta": [100, 200, 300],
            "objetivo": [150, 250, 350]
        }
        df = pd.DataFrame(data)

        # Crear una instancia de la clase
        ventas_vs_objetivo = VentasVSObjetivo()

        # Ejecutar el método
        resultado = ventas_vs_objetivo.execute(df)

        # Verificar el resultado esperado
        assert resultado == "Ventas vs objetivo: -50.00%"
        
