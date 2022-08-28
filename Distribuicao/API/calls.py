from dbm import error
from flask import Flask, request
from Distribuicao.Standalone.infra.connector_LogarRFID import LogarRFID

app = Flask()

class Calls:

    def run():
        app.run(host="0.0.0.0")
    
    @app.route("/SendRFID", methods=["POST"])
    def SendRFID():

        body = request.get_json()
    
        rfid = body.get("RFID")

        try:
            logIn = LogarRFID.logarUserPorRFID(rfid)
            if(logIn):
                print(f"Usário {logIn[1]} logado com sucesso")
                return logIn[1]
            else:
                print("Falha ao logar usuário")
            
        except:
            print("Falha ao se comunicar com o Banco de dados")               
            return "Falha ao se comunicar com o Banco de dados"               