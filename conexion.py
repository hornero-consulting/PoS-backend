import psycopg2


class Conexion:
    def __init__(self, host, database, user, password) -> None:
        self._host = host
        self._database = database
        self._user = user
        self._password = password

    def cur(self):
        return self._conn.cursor()

    def connect(self) -> None:
        self._conn = psycopg2.connect(
            host=self._host,
            database=self._database,
            user=self._user,
            password=self._password,
        )
        self._conn.autocommit = True

    def close(self) -> None:  # cierra conexion
        self._conn.close()
