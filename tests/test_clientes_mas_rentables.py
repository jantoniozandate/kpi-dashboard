# test_clientes_mas_rentables.py


def test_execute():
    """
    Test para la clase ClientesMasRentables.
    Crea un dataframe de ejemplo y verifica que el resultado sea correcto.
    """
    from kpi.clientes_mas_rentables import ClientesMasRentables
    import pandas as pd
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
