#MCargarEstudio()
import sqlite3
"""
ESTAS SON PRUEBAS FALLIDAS PARA LLAMAR A LA CLASE (MODELO) Estudio
import sys
from ../Model import Estudio
sys.path.append(0, "C:/Users/Esteban/Desktop/Model")
import Estudio
estudio1 = Estudio()
printt(estudio1)
Paciente y MedicoSolicitante son claves foraneas
"""
miConexion = sqlite3.connect("mydb")
miCursor = miConexion.cursor()
miCursor.execute("""
        CREATE TABLE if not exists EM (
        ID_EM integer Primary key autoincrement,
        Tipo varchar (45),
        Fecha date,
        Paciente integer,
        MedicoSolicitante integer,
        Ubicacion varchar (150))
""")
#Aca se cargaria una instancia de la clase Estudio
#estudios = Estudio()
#estudios.cargar()
estudios = [
    ("RAYOSX", 2022, 1, 1, "Mi Ciudad"),
    ("RAYOSX2", 2022, 2, 2, "Mi Ciudad2"),
    ("RAYOSX3", 2022, 3, 3, "Mi Ciudad3"),
    ("RAYOSX4", 2022, 4, 4, "Mi Ciudad4")
]
miCursor.executemany("INSERT INTO EM VALUES (NULL, ?, ?, ?, ?, ?)", estudios)
miConexion.commit()
miConexion.close()