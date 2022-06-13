import mysql.connector

from Distribuicao.Standalone.infra.connector_infra import Connector

class LogarUser:

    def logarUser(user, password) -> str:
        con = Connector.conectar()

        logarUser = f"""select * from app_user where '{user}' and '{password}';"""

        cursor = con.cursor()
        cursor.execute(logarUser)
        retornoBanco = cursor.fetchone()
        con.close()

        return retornoBanco

