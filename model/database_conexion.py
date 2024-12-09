import mysql.connector  # Librería para manejar la conexión a MySQL
from mysql.connector import Error  # Clase para manejar errores específicos de MySQL


class DatabaseConnection:
    def __init__(self):
        try:
            # Configuración de la conexión a la base de datos
            self.conn = mysql.connector.connect(
                host='localhost',  # Dirección del servidor MySQL
                user='root',       # Usuario de la base de datos
                password='',       # Contraseña del usuario
                database='calculadora'  # Nombre de la base de datos
            )

            # Verifica si la conexión fue exitosa
            if self.conn.is_connected():
                print()  # Mensaje de éxito

        except Error as e:
            # Manejo de errores en caso de problemas con la conexión
            print(f"Error al conectar la base de datos: {e}")

    def Close_conection(self):
        if self.conn.is_connected():
            self.conn.close()  # Cierra la conexión
            print()  # Mensaje de confirmación


# Bloque principal para pruebas individuales
if __name__ == "__main__":
    # Crea una instancia de la clase y prueba abrir/cerrar la conexión
    db = DatabaseConnection()
    db.Close_conection()
