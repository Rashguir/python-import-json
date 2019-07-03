import json
# ModuleNotFoundError: No module named 'mysql'
import mysql.connector
from mysql.connector import Error

class Distro:
    def __init__(self, data):
        self.__dict__ = data

    def forInsert(self):
        return (self.Name, self.Version, self.Install, self.Owner, self.Kernel)

sqlCreateTableDistros = """CREATE TABLE IF NOT EXISTS Distros (
    name VARCHAR(20),
    version VARCHAR(20),
    install VARCHAR(10),
    owner VARCHAR(50),
    kernel VARCHAR(10)
)"""
sqlInsertDistro = """INSERT INTO Distros (name, version, install, owner, kernel)
VALUES (%s, %s, %s, %s, %s)"""

try:
    with open('distros.json', 'r') as f:
        distro_dict = json.load(f)
except ValueError:
    print("error loading JSON")

distroObjects = []

for distro_array in distro_dict:
    d = Distro(distro_array)
    distroObjects.append(d)

print(distroObjects[0].Name)

try:
    connection = mysql.connector.connect(
        host='db', 
        database='db_name', 
        user='db_user', 
        password='db_password',
        auth_plugin='mysql_native_password'
    )

    if connection.is_connected():
        db_info = connection.get_server_info()
        print("You are connected db - version on ", db_info)

        cursor = connection.cursor()
        cursor.execute(sqlCreateTableDistros)

        for distroObject in distroObjects:
            cursor.execute(sqlInsertDistro, distroObject.forInsert())

        connection.commit()
except Error as e:
    print("Error while attempting to connect to mysql", e)
