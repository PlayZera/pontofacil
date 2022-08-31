from datetime import date, datetime
import json
import os


_configOut = []
key = "None"

class carregarConfigs:

    ## C:\Users\lucas\Desktop\PontoFacil\gui\infra\appConfig_cliente.json

    def carregar(_config) -> list:
        docJson = open(f'Distribuicao/Standalone/appConfig_{os.getenv(key)}.json', 'r')
        print(f"{datetime.now()} - appConfig carregado appConfig_{os.getenv(key)}")
        obj = json.load(fp=docJson)
        doc = obj['connectionString'][0]

        _configOut.append(doc['Host'])
        _configOut.append(doc['Database'])
        _configOut.append(doc['User'])
        _configOut.append(doc['Password'])

        return _configOut
