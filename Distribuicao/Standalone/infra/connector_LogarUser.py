import mysql.connector

from Distribuicao.Standalone.infra.connector_infra import Connector

class LogarUser:

    def logarUser(user, password) -> tuple:
        con = Connector.conectar()

        logarUser = f"""select * from app_user where USER_LOGIN = '{user}' and USER_PASSWORD = '{password}';"""
        cursor = con.cursor()
        cursor.execute(logarUser)
        retornoBanco = cursor.fetchone()
        print(retornoBanco)

        return retornoBanco

