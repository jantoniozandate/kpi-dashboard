# test_clientes_mas_rentables.py
import pandas as pd
from kpi.clientes_mas_rentables import ClientesMasRentables

def _execute(df):
    """
    Test para la clase ClientesMasRentables.
    Crea un dataframe de ejemplo y verifica que el resultado sea correcto.
    """
    # Crear un dataframe de ejemplo
    data = {
        "cliente_id": [1, 2, 3, 1, 2, 4],
        "venta": [100, 200, 300, 150, 250, 400]
    }
    df = pd.DataFrame(data)

    # Crear una instancia de la clase
    clientes_mas_rentables = ClientesMasRentables()

    # Ejecutar el método
    resultado = clientes_mas_rentables.execute(df)

    # Verificar el resultado esperado
    assert resultado == "Clientes más rentables: [4]"
