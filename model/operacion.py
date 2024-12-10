from mysql.connector import Error  # Librería para manejar errores específicos de MySQL
from model.database_conexion import DatabaseConnection  # Clase de conexión a la base de datos


class Operacion:
    #Operaciones
    @staticmethod
    def suma(numero1, numero2):
        return numero1 + numero2

    @staticmethod
    def resta(numero1, numero2):
        return numero1 - numero2

    @staticmethod
    def multiplicacion(numero1, numero2):
        return numero1 * numero2

    @staticmethod
    def division(numero1, numero2):
        if numero2 == 0:
            raise ZeroDivisionError("\033[31mEl divisor no puede ser cero.\033[0m")
        return numero1 / numero2

    @staticmethod
    def realizar_operacion(numero1, numero2, tipo_operacion):
        if tipo_operacion == "suma":
            return Operacion.suma(numero1, numero2)
        elif tipo_operacion == "resta":
            return Operacion.resta(numero1, numero2)
        elif tipo_operacion == "multiplicacion":
            return Operacion.multiplicacion(numero1, numero2)
        elif tipo_operacion == "division":
            return Operacion.division(numero1, numero2)
        else:
            raise ValueError("\033[31mOperación no válida.\033[0m")  # Tipo de operación no reconocido

    @staticmethod
    def guardar_historial(tipo_operacion, numero1, numero2, resultado):
        
        db = DatabaseConnection()  # Crea una conexión a la base de datos
        try:
            # Crea un cursor para ejecutar la consulta
            cursor = db.conn.cursor()

            # Consulta SQL para insertar datos en la tabla 'historial'
            consulta = """
                INSERT INTO historial (operacion, numero1, numero2, resultado)
                VALUES (%s, %s, %s, %s)
            """
            valores = (tipo_operacion, numero1, numero2, resultado)  # Valores a insertar
            cursor.execute(consulta, valores)  # Ejecuta la consulta
            db.conn.commit()  # Confirma los cambios en la base de datos
        except Error as e:
            # Muestra un error en caso de fallar la inserción
            print(f"Error al guardar en el historial: {e}")
        finally:
            # Cierra la conexión a la base de datos
            db.Close_conection()

    @staticmethod
    def obtener_historial():
        db = DatabaseConnection()  # Crea una conexión a la base de datos
        try:
            # Crea un cursor para ejecutar la consulta
            cursor = db.conn.cursor()

            # Consulta SQL para obtener los datos de la tabla 'historial'
            consulta = "SELECT * FROM historial"
            cursor.execute(consulta)  # Ejecuta la consulta
            historial = cursor.fetchall()  # Recupera todos los registros
            return historial  # Retorna el historial como una lista de tuplas
        except Error as e:
            # Muestra un error en caso de fallar la consulta
            print(f"Error al obtener el historial: {e}")
            return []  # Retorna una lista vacía en caso de error
        finally:
            # Cierra la conexión a la base de datos
            db.Close_conection()

