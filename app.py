import os
import webview

# Clase que conecta JS con Python
class Api:
    def search_file(self, query):
        results = []
        home_dir = os.path.expanduser("~")  # Carpeta home del usuario

        for root, dirs, files in os.walk(home_dir):
            for file in files:
                if query.lower() in file.lower():
                    results.append(os.path.join(file))

        counter = len(results)  # ahora sí cuenta al final

        return {
            "count": counter,
            "files": results if results else []
        }


# Inicializar la ventana con PyWebView
api = Api()
window = webview.create_window(
    "MyFiles",    # Título de la ventana
    "index.html", # Archivo HTML que se mostrará
    js_api=api    # Aquí conectamos la API (Python <-> JS)
)

# Iniciar la aplicación
if __name__ == "__main__":
    webview.start()
