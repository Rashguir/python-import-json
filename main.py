import json
import mysql.connector
from mysql.connector import Error

class Distro:
    def __init__(self, data):
        self.__dict__ = data

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
    connection = mysql.connector.connect(host='db', database='db_name', user='db_user', password='db_password')

    if connection.is_connected():
        db_info = connection.get_server_info()
        print("You are connected db - version on ", db_info)

        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("you are connected to - ", record)
except (Exception, psycopg2.Error) as error:
    print("Error while attempting to connect to postgresql", error)
finally:
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

