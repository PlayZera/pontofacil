from datetime import datetime
from flask import Flask, request
from Distribuicao.Standalone.infra.connector_LogarRFID import LogarRFID
from Distribuicao.Standalone.infra.connector_MarcaPontoRFID import MarcaPontoRFID
from Distribuicao.Standalone.modules.Context import Context

app = Flask("API_PontoSimples")

class Calls:

    def run():
        app.run(host="0.0.0.0",
                debug=True)
    
    @app.route("/SendRFID", methods=["POST"])
    def SendRFID():

        body = request.get_json()
    
        rfid = body.get("RFID")

        try:
            logIn = LogarRFID.logarUserPorRFID(rfid)

            if(logIn):
                contexto = Context(logIn)
                print(f"{datetime.now()} - Usário {contexto.nome_User} logado com sucesso")
                pontoMarcado = MarcaPontoRFID(contexto)
                pontoMarcado.marcarPonto()
                return f"Ponto registrado para {contexto.nome_User}"
            else:
                print("Falha ao logar usuário")
                return "Falha ao logar usuário"
            
        except:
            print("Falha ao se comunicar com o Banco de dados")               
            return "Falha ao se comunicar com o Banco de dados"

