import mysql.connector

from Distribuicao.Standalone.infra.connector_infra import Connector


logarUser = f"""select * from database() where {user} and {password};"""

class LogarUser:

    def logarUser(self, con):
        con = Connector.conectar()

        cursor = con.cursor()
        cursor.execute(logarUser)

