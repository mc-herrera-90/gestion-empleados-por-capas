import pymysql

class Conexion:

    def __init__(self, user, password):
        self.host = 'localhost'
        self.user = user
        self.password = password
        self.database = 'ecotech_solutions_company'

    def conectar(self):
        # Aquí iría la lógica para conectar a la base de datos
        try:
            conexion = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                auth_plugin_map={'caching_sha2_password': pymysql.cursors.DictCursor}
            )
            print("Conexión exitosa a la base de datos")
            return conexion
        except pymysql.MySQLError as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None

if __name__ == '__main__':
    user = input("Ingrese el usuario de la base de datos: ")
    password = input("Ingrese la contraseña de la base de datos: ")
    conexion = Conexion(user, password)
    conexion.conectar()