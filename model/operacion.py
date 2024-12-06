from mysql.connector import Error
from model.database_conexion import DatabaseConnection  


class Operacion:
    @staticmethod
    def realizar_operacion(numero1, numero2, tipo_operacion):
        if tipo_operacion == "suma":
            return numero1 + numero2
        elif tipo_operacion == "resta":
            return numero1 - numero2
        elif tipo_operacion == "multiplicacion":
            return numero1 * numero2
        elif tipo_operacion == "division":
            if numero2 == 0:
                raise ZeroDivisionError("El divisor no puede ser cero.")
            return numero1 / numero2
        else:
            raise ValueError("Operación no válida.")

    @staticmethod
    def guardar_historial(tipo_operacion, numero1, numero2, resultado):
        db = DatabaseConnection()
        try:
            cursor = db.conn.cursor()
            consulta = """
                INSERT INTO historial (operacion, numero1, numero2, resultado)
                VALUES (%s, %s, %s, %s)
            """
            valores = (tipo_operacion, numero1, numero2, resultado)
            cursor.execute(consulta, valores)
            db.conn.commit()
        except Error as e:
            print(f"Error al guardar en el historial: {e}")
        finally:
            db.Close_conection()

    @staticmethod
    def obtener_historial():
        db = DatabaseConnection()
        try:
            cursor = db.conn.cursor()
            consulta = "SELECT * FROM historial"
            cursor.execute(consulta)
            historial = cursor.fetchall()
            return historial
        except Error as e:
            print(f"Error al obtener el historial: {e}")
            return []
        finally:
            db.Close_conection()
