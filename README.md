# ccalculadora-python

Este proyecto es un sistema para una calculadora, en la cual gestionamos, las diferentes operaciones de SUMA, RESTA, MULTIPLICACIÓN, DIVISIÓN.
En la cual tambien es gestionada con una base de datos para el manejo de historial de operaciones realizadas

## Requisitos

- Python 3.x
- MySQL Connector para Python

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/alfadestruc17/ccalculadora-python.git
   ```

2. Instala las dependencias necesarias:
   ```bash
   pip install mysql-connector-python
   ```
## Estructura de la Base de Datos

El sistema crea automáticamente las siguientes tablas:

- **Operaciones**: Almacena información sobre los nombres de las operaciones.
- **Historial**: Almacena las operaciones realizadas, los numeros usados, la operacion usada y el resultado.

