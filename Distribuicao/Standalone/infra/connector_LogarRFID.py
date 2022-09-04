from Distribuicao.Standalone.infra.connector_infra import Connector

class LogarRFID:

    def logarUserPorRFID(rfid) -> tuple:
        con = Connector.conectar()

        logarUser = f"""select * from app_user where RFID_USER = '{rfid}';"""
        cursor = con.cursor()
        cursor.execute(logarUser)
        retornoBanco = cursor.fetchone()
        print(retornoBanco)

        return retornoBanco

