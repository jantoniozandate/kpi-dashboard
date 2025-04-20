from pathlib import Path
import pandas as pd

class ExcelManager:
    _instance = None
    _cache = {}
    ventas_path = "data/ventas.xlsx"
    productos_path = "data/productos.xlsx"
    clientes_path = "data/clientes.xlsx"

    def __new__(cls, ventas_path="data/ventas.xlsx",
    productos_path="data/productos.xlsx", clientes_path="data/clientes.xlsx"):
        if cls._instance is None:
            cls._instance = super(ExcelManager, cls).__new__(cls)
            cls._instance.ventas_path = Path(ventas_path)
            cls._instance.productos_path = Path(productos_path)
            cls._instance.clientes_path = Path(clientes_path)
        return cls._instance

    def clear_cache(self, path):
        """Clears the cache for a specific path."""
        self._cache.pop(path, None)

    def leer(self):
        """Lee el archivo de ventas y guarda el DataFrame en caché."""
        return self._leer_archivo(self.ventas_path)

    def leer_productos(self):
        """Lee el archivo de productos y guarda el DataFrame en caché."""
        return self._leer_archivo(self.productos_path)

    def leer_clientes(self):
        """Lee el archivo de clientes y guarda el DataFrame en caché."""
        return self._leer_archivo(self.clientes_path)


    def guardar(self, df: pd.DataFrame):
        """Guarda el DataFrame de ventas en el archivo Excel y actualiza la caché."""
        df.to_excel(self.ventas_path, index=False)
        self._cache[self.ventas_path] = df

    def _leer_archivo(self, path: Path):
        if path not in self._cache:
            if path.exists():
                self._cache[path] = pd.read_excel(path)
            else:
                raise FileNotFoundError(f"No se encontró el archivo: {path}")
        return self._cache[path]


# Instancia reutilizable
excel_manager = ExcelManager()
