class Vista:
    def mostrar_menu(self): # menu que se le muestra al usuario
        print("--- Menú de Calculadora ---")
        print("\033[34m1. Suma\033[0m")
        print("\033[34m2. Resta\033[0m")
        print("\033[34m3. Multiplicación\033[0m")
        print("\033[34m4. División\033[0m")
        print("\033[33m5. Ver historial\033[0m")
        print("\033[31m6. Salir\033[0m")

    def solicitar_numeros(self):
        while True:
            try:
                # Solicita al usuario los números y los convierte a flotantes
                numero1 = float(input("\033[33mIngrese el primer número: \033[0m"))
                while True:
                    try:
                        if numero1 is not None:
                            numero2 = float(input("\033[33mIngrese el segundo número: \033[0m"))
                            if numero2 is not None:
                                return numero1, numero2
                    except ValueError:
                        print("\033[31mError: Ingrese números válidos.\033[0m")
            except ValueError:
                # Muestra un mensaje de error si la entrada no es válida
                print("\033[31mError: Ingrese números válidos.\033[0m")

    def mostrar_resultado(self, resultado):
        print(f"\033[32mEl resultado de la operación es: {resultado}\033[0m") # Muestra el resultado de la operación

    def mostrar_historial(self, historial):
        if not historial:
            # Si no hay registros, muestra un mensaje indicando que no hay historial
            print("\033[31mNo hay historial disponible.\033[0m")
        else:
            # Muestra los registros del historial con un formato legible
            print("--- Historial de Operaciones ---")
            for registro in historial:
                print(f"ID: {registro[0]} | Operación: {registro[1]} | "
                      f"Números: {registro[2]}, {registro[3]} | Resultado: {registro[4]}")

    def mostrar_error(self, mensaje):
        print(f"\033[31mError: {mensaje}\033[0m") # Muestra si ocurrio un error en alguna acción
