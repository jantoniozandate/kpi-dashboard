import importlib
from pathlib import Path
from utils.excel_manager import ExcelManager

class CLIApp:
    def __init__(self):
        self.excel_manager = ExcelManager()
        self.df = None

    def start(self):
        print("CLI interactiva iniciada. Escribe 'salir' para terminar o presiona Ctrl+D.")
        while True:
            try:
                comando = input("app> ").strip()
                if comando.lower() == "salir":
                    break
                self.ejecutar_comando(comando)
            except EOFError:
                print("\nSaliendo con Ctrl+D.")
                break
            except Exception as e:
                print(f"Error: {e}")

    def ejecutar_comando(self, comando: str):
        partes = comando.split(" ", 1)
        if len(partes) != 2:
            print("Comando inválido. Uso: <verbo> <nombre_archivo>")
            return
        verbo, nombre_archivo = partes
        self._ejecutar_accion(verbo.lower(), nombre_archivo.strip())

    def _cargar_archivo(self, comando: str):
        partes = comando.split("path=")
        if len(partes) != 2:
            print("Uso correcto: cargar archivo path=archivo.xlsx tipo=tipo_de_dato")
            return

        path_part, tipo_part = partes[1].split("tipo=") if "tipo=" in partes[1] else (partes[1], "data")
        ruta = Path(path_part.strip())
        tipo = tipo_part.strip().lower()

        try:
            if tipo == "data":
                self.excel_manager.ventas_path = ruta
                self.df = self.excel_manager.leer()
            elif tipo == "productos":
                self.excel_manager.productos_path = ruta
                self.excel_manager.clear_cache(ruta)
                self.excel_manager.leer_productos()
            elif tipo == "clientes":
                self.excel_manager.clientes_path = ruta
                self.excel_manager.clear_cache(ruta)
                self.excel_manager.leer_clientes()
            else:
                print("Tipo no reconocido. Usa: data, productos o clientes")
                return

            print(f"Archivo cargado exitosamente desde: {ruta} como tipo '{tipo}'")
        except Exception as e:
            print(f"No se pudo cargar el archivo: {e}")

    def _ejecutar_accion(self, verbo: str, nombre_archivo: str):
        if verbo == "cargar" and nombre_archivo.startswith("archivo"):
            self._cargar_archivo(f"{verbo} {nombre_archivo}")
            return

        if self.df is None:
            print("Primero debes cargar un archivo con 'cargar archivo path=...'")
            return

        try:
            modulo = importlib.import_module(f"kpi.{verbo}_{nombre_archivo}")
            nombre_clase = ''.join(word.capitalize() for word in nombre_archivo.split("_"))
            clase = getattr(modulo, f"{verbo.capitalize()}{nombre_clase}")
            instancia = clase()
            resultado = instancia.execute(self.df)
            print(f"Resultado de {verbo} {nombre_archivo}:")
            print(resultado)
        except ModuleNotFoundError:
            print(f"No se encontró el módulo 'kpi.{verbo}_{nombre_archivo}'")
        except AttributeError as e:
            print(f"Error accediendo a la clase o método: {e}")
