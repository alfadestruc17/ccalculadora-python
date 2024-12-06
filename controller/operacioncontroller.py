from model.operacion import Operacion
from views.vista_calculadora import Vista


class Controlador:
    def __init__(self):
        self.vista = Vista()

    def iniciar(self):
        while True:
            self.vista.mostrar_menu()
            opcion = input("Seleccione una opción: ")

            if opcion in ["1", "2", "3", "4"]:
                self.realizar_operacion(opcion)
            elif opcion == "5":
                self.ver_historial()
            elif opcion == "6":
                print("Gracias por usar la calculadora. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

    def realizar_operacion(self, opcion):
        operaciones = {
            "1": "suma",
            "2": "resta",
            "3": "multiplicacion",
            "4": "division"
        }
        tipo_operacion = operaciones[opcion]

        numero1, numero2 = self.vista.solicitar_numeros()
        if numero1 is None or numero2 is None:
            return

        try:
            resultado = Operacion.realizar_operacion(numero1, numero2, tipo_operacion)
            self.vista.mostrar_resultado(resultado)
            Operacion.guardar_historial(tipo_operacion, numero1, numero2, resultado)
        except (ValueError, ZeroDivisionError) as e:
            self.vista.mostrar_error(str(e))

    def ver_historial(self):
        historial = Operacion.obtener_historial()
        self.vista.mostrar_historial(historial)
