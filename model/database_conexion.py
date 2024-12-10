import mysql.connector  # Importamos el módulo para conectarnos a bases de datos MySQL
from mysql.connector import Error  # Importamos la clase de errores para manejar excepciones


# Clase para manejar la conexión a la base de datos
class DatabaseConnection:
    def __init__(self):
        try:
            # Establecemos una conexión a MySQL
            self.conn = mysql.connector.connect(
                host='localhost',  # Nombre del host (servidor de la base de datos)
                user='root',       # Usuario de la base de datos
                password=''        # Contraseña del usuario (vacío por defecto en local)
            )

            self.cursor = self.conn.cursor()  # Creamos un cursor para ejecutar comandos SQL

            # Creamos la base de datos si no existe
            self.create_database('ccalculadora')

            # Seleccionamos la base de datos para usarla
            self.conn.database = 'ccalculadora'

            # Creamos las tablas necesarias
            self.create_tables()

        except Error as e:
            # Si hay un error al conectar, lo mostramos
            print(f"Error al conectar a la base de datos: {e}")

    # Método para crear la base de datos si no existe
    def create_database(self, database):
        self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database};")  # Comando SQL para crear la base de datos

    # Método para crear las tablas
    def create_tables(self):
        """
        Crea las tablas necesarias si no existen. 
        Aquí se crean dos tablas: `historial` y `operaciones`.
        """
        # Crear la tabla `historial` para guardar las operaciones realizadas
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS historial (
                id INT AUTO_INCREMENT PRIMARY KEY,  # Identificador único para cada registro
                operacion VARCHAR(45) NOT NULL,     # Tipo de operación (ej: suma, resta)
                numero1 FLOAT NOT NULL,    # Primer número
                numero2 FLOAT NOT NULL,    # Segundo número
                resultado FLOAT NOT NULL   # Resultado de la operación
            );
        """)

        # Crear la tabla `operaciones` para guardar los tipos de operaciones disponibles
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS operaciones (
                id INT AUTO_INCREMENT PRIMARY KEY,  # Identificador único para cada tipo de operación
                operacion VARCHAR(45) NOT NULL      # Nombre de la operación (ej: suma)
            );
        """)

        # Guardamos los cambios en la base de datos
        self.conn.commit()

    # Método para cerrar la conexión a la base de datos
    def Close_conection(self):
        """
        Cierra la conexión a la base de datos si está activa.
        """
        if self.conn.is_connected():  # Verifica si la conexión sigue activa
            self.conn.close()  # Cierra la conexión
            print("Conexión cerrada.")  # Mensaje para confirmar el cierre


# Bloque principal para probar el código
if __name__ == "__main__":
    # Creamos una instancia de la clase para probarla
    db = DatabaseConnection()  # Esto conecta a la base de datos, crea la base y las tablas
    db.Close_conection()  # Cerramos la conexión para finalizar

