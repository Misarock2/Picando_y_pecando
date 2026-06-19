import sqlite3
from pathlib import Path

DB_FILE = Path(__file__).parent / 'productos.db'

PRODUCTOS = [
    ('Tostada Especial', 'Tostada de platano con carne desmechada, pollo, maiz tierno, queso y salsas al gusto', 20000, 'asset/img/productos/tostada.jpg'),
    ('Pollo a la Plancha', 'Delicioso pollo a la plancha, sazonado con hierbas y especias. Salsa de la casa.', 18000, 'asset/img/productos/pollo a la plancha.png'),
    ('Salchipapa Suprema', 'Papas crujientes, salchicha, queso y salsas de la casa.', 15000, 'asset/img/salchipapa.jpg'),
    ('Papas a la Francesa', 'Porcion generosa de papas crujientes, sal y acompañamientos al gusto.', 8000, 'asset/img/productos/papas_francesa.jpg'),
    ('Perro Caliente Especial', 'Pan tostado, salchicha artesanal, queso rallado y salsas caseras.', 12000, 'asset/img/productos/perro_caliente.jpg'),
    ('Pizza Individual', 'Base crujiente, salsa napolitana, queso mozzarella y toppings a eleccion.', 22000, 'asset/img/productos/pizza_individual.jpg'),
]

CREATE_TABLE_SQL = '''
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    precio INTEGER NOT NULL,
    imagen TEXT NOT NULL
);
'''

INSERT_SQL = '''
INSERT INTO productos (nombre, descripcion, precio, imagen)
VALUES (?, ?, ?, ?);
'''


def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(CREATE_TABLE_SQL)
    cursor.executemany(INSERT_SQL, PRODUCTOS)
    conn.commit()
    conn.close()
    print(f'Base de datos creada en: {DB_FILE}')


if __name__ == '__main__':
    init_db()
