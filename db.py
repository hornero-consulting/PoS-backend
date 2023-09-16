from conexion import Conexion


class Base_De_Datos:
    def __init__(self, conexion: Conexion) -> None:
        self.conexion = conexion
        self.conexion.connect()
        self._cur = self.conexion.cur()

    def crear_usuario(self, usuario, clave):
        self._cur.execute(
            f"INSERT INTO usuario(usuario, clave) values('{usuario}', '{clave}')"
        )
        return f"se creo el usuario {usuario} con exito"

    def usuarios(self):
        self._cur.execute("SELECT usuario FROM usuario")
        return self._depura_resultado(self._cur.fetchall())

    def _depura_resultado(self, lista):
        aux = []
        for i in lista:
            aux.append(i[0])
        return aux
