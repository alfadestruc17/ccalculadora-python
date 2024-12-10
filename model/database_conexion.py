import mysql.connector  
from mysql.connector import Error  


class DatabaseConnection:
    def __init__(self):
        try:
           
            self.conn = mysql.connector.connect(
                host='localhost',  
                user='root',       
                password=''       
            )

            self.cursor = self.conn.cursor()

            self.create_database('ccalculadora')
            
            self.conn.database = 'ccalculadora'

            self.create_tables()

        except Error as e:
            # Manejo de errores en caso de problemas con la conexión
            print(f"Error al conectar a la base de datos: {e}")

    def create_database(self, database):
        
        self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database};")

    def create_tables(self):
        """Crea las tablas `historial` y `operaciones` si no existen."""
        # Crear tabla historial
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS historial (
                id INT AUTO_INCREMENT PRIMARY KEY,
                operacion VARCHAR(45) NOT NULL,
                numero1 DECIMAL(10, 2) NOT NULL,
                numero2 DECIMAL(10, 2) NOT NULL,
                resultado DECIMAL(10, 2) NOT NULL
            );
        """)

        # Crear tabla operaciones
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS operaciones (
                id INT AUTO_INCREMENT PRIMARY KEY,
                operacion VARCHAR(45) NOT NULL
            );
        """)

        # Confirmar cambios en la base de datos
        self.conn.commit()

    def Close_conection(self):
        """Cierra la conexión a la base de datos."""
        if self.conn.is_connected():
            self.conn.close()  # Cierra la conexión
            print("Conexión cerrada.")


# Bloque principal para pruebas individuales
if __name__ == "__main__":
    # Crea una instancia de la clase y prueba abrir/cerrar la conexión
    db = DatabaseConnection()
    db.Close_conection()
