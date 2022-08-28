import mysql.connector

from infra.connector_infra import Connector

class LogarRFID:
    
    def __init__(self) -> None:
        pass

    def logarUserPorRFID(rfid) -> tuple:
        con = Connector.conectar()

        logarUser = f"""select * from app_user where RFID_USER = '{rfid}'';"""
        cursor = con.cursor()
        cursor.execute(logarUser)
        retornoBanco = cursor.fetchone()
        print(retornoBanco)

        return retornoBanco

