import mysql.connector
from infra.carregarConfigs import carregarConfigs

configFile = carregarConfigs.carregar(_config='appConfig.json')

class Connector:

    def conectar():

        try:
            con = mysql.connector.connect(host=configFile[0], database=configFile[1], user=configFile[2], password=configFile[3])

            if con.is_connected():

                cursor = con.cursor()
                cursor.execute("select database();")
                linha = cursor.fetchone()
                print(f"Conectado ao banco de dados {linha}")

            return con

        except:
            raise mysql.connector.DatabaseError