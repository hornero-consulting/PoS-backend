from conexion import Conexion
from db import Base_De_Datos

conexion = Conexion("localhost", "pos-db-dev", "postgres", "admin")
db = Base_De_Datos(conexion)
