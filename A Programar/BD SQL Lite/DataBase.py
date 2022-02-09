import sqlite3

def Conectar():
    conexion = sqlite3.connect("MiBD.db")
    cursor = conexion.cursor()
    return conexion,cursor

def CrearTabla():
    conexion,cursor = Conectar()
    sql = """
            CREATE TABLE IF NOT EXISTS Agenda(
            Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            Nombre VARCHAR(20) not NULL,
            Telefono varchar(8) not NULL
            )
    """
    if cursor.execute(sql):
        print("Tabla creada")
    else:
        print("Error al crear tabla")

    conexion.close()

CrearTabla()
