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

                case "1":  # Opciones de operaciones
                    numero1, numero2 = self.vista.solicitar_numeros()
                    resultado = Operacion.suma(numero1, numero2)
                    self.vista.mostrar_resultado(resultado)
                    Operacion.guardar_historial(1, numero1, numero2, resultado)
                case "2":
                    numero1, numero2 = self.vista.solicitar_numeros()
                    resultado = Operacion.resta(numero1, numero2)
                    self.vista.mostrar_resultado(resultado)
                    Operacion.guardar_historial(2, numero1, numero2, resultado)

                case "3":
                    numero1, numero2 = self.vista.solicitar_numeros()
                    resultado = Operacion.multiplicacion(numero1, numero2)
                    self.vista.mostrar_resultado(resultado)
                    Operacion.guardar_historial(3, numero1, numero2, resultado)

                case "4": 
                    numero1, numero2 = self.vista.solicitar_numeros()
                    resultado = Operacion.division(numero1, numero2)
                    if resultado == False:
                        self.vista.mostrar_error("No se puede dividor por 0")
                    else:    
                        self.vista.mostrar_resultado(resultado)
                        Operacion.guardar_historial(4, numero1, numero2, resultado)

                case "5":  # Ver historial
                    historial = Operacion.obtener_historial()
                    self.vista.mostrar_historial(historial)
                case "6":  # Salir
                    print("Gracias por usar la calculadora. ¡Hasta luego!")
                    break
                case _:
                    print("Opción no válida. Intente nuevamente.")  # Manejo de entrada no válida
