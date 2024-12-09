class Vista:
    def mostrar_menu(self): # menu que se le muestra al usuario
        print("--- Menú de Calculadora ---")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Ver historial")
        print("6. Salir")

    def solicitar_numeros(self):
        try:
            # Solicita al usuario los números y los convierte a flotantes
            numero1 = float(input("Ingrese el primer número: "))
            numero2 = float(input("Ingrese el segundo número: "))
            return numero1, numero2
        except ValueError:
            # Muestra un mensaje de error si la entrada no es válida
            print("Error: Ingrese números válidos.")
            return None, None

    def mostrar_resultado(self, resultado):
        print(f"El resultado de la operación es: {resultado}") # Muestra el resultado de la operación

    def mostrar_historial(self, historial):
        if not historial:
            # Si no hay registros, muestra un mensaje indicando que no hay historial
            print("No hay historial disponible.")
        else:
            # Muestra los registros del historial con un formato legible
            print("--- Historial de Operaciones ---")
            for registro in historial:
                print(f"ID: {registro[0]} | Operación: {registro[1]} | "
                      f"Números: {registro[2]}, {registro[3]} | Resultado: {registro[4]}")

    def mostrar_error(self, mensaje):
        print(f"Error: {mensaje}") # Muestra si ocurrio un error en alguna acción
