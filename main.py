from controller.operacioncontroller import Controlador

# Punto de entrada principal de la aplicación
if __name__ == "__main__":
    app = Controlador()  # Instancia del controlador principal
    app.iniciar()        # Inicia la ejecución del flujo principal de la calculadora
