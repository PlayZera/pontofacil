from datetime import datetime

import mysqlx
from flask import Flask, request
from Distribuicao.Standalone.infra.connector_LogarRFID import LogarRFID
from Distribuicao.Standalone.infra.connector_MarcaPontoRFID import MarcaPontoRFID
from Distribuicao.Standalone.infra.connector_MarcaPonto import MarcaPonto
from Distribuicao.Standalone.modules.Context import Context

app = Flask("API_PontoSimples")

class Calls:

    def run():
        app.run(host="0.0.0.0",
                debug=True)

#region Chamadas API_Ponto Simples
    @app.route("/MakePoint", methods=["POST"])
    def MakePoint():
        body = request.get_json()

        context = body.get("contexto")

        try:
            contexto = Context(context)
            print(f"{datetime.now()} - Usário {contexto.nome_User} logado com sucesso")
            pontoMarcado = MarcaPonto(contexto)
            pontoMarcado.marcarPonto()
            return "Ponto Registrado pelo Client"

        except:
            return mysqlx.Error

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
#endregion
