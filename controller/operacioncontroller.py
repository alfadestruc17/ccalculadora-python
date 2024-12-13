from model.operacion import Operacion  # Importamos la clase Operacion que maneja la lógica de las operaciones y la interacción con la base de datos.
from views.vista_calculadora import Vista  # Importamos la clase Vista para manejar la interfaz con el usuario.


class Controlador:

    def __init__(self):
        self.vista = Vista()
    def iniciar(self):
        while True:
            # Muestra el menú principal al usuario
            self.vista.mostrar_menu()

            # opción ingresada por el usuario
            opcion = input("Seleccione una opción: ")

            # Manejo de opciones del menú
            match opcion:

                case "1" | "2" | "3" | "4":  # Opciones de operaciones
                    self.realizar_operacion(opcion)
                case "5":  # Ver historial
                    self.ver_historial()
                case "6":  # Salir
                    print("Gracias por usar la calculadora. ¡Hasta luego!")
                    break
                case _:
                    print("Opción no válida. Intente nuevamente.")  # Manejo de entrada no válida

    def realizar_operacion(self, opcion):
        # Opciones de los tipos de operación
        operaciones = {
            "1": "suma",
            "2": "resta",
            "3": "multiplicacion",
            "4": "division"
        }
        tipo_operacion = operaciones[opcion]  # Determina el tipo de operación

        # Solicita al usuario los números para realizar la operación
        numero1, numero2 = self.vista.solicitar_numeros()
        if numero1 is None or numero2 is None:  # Si hubo un error en la entrada, se detiene el flujo
            return

        try:
            # Realiza la operación utilizando el modelo
            resultado = Operacion.realizar_operacion(numero1, numero2, tipo_operacion)

            # Muestra el resultado al usuario
            self.vista.mostrar_resultado(resultado)

            # Guarda la operación en el historial de la base de datos
            Operacion.guardar_historial(tipo_operacion, numero1, numero2, resultado)

        except (ValueError, ZeroDivisionError) as e:
            # Captura y muestra errores como división por cero o valores no válidos
            self.vista.mostrar_error(str(e))

    def ver_historial(self):
        # Obtiene el historial desde el modelo
        historial = Operacion.obtener_historial()

        # Muestra el historial utilizando la vista
        self.vista.mostrar_historial(historial)
