from datetime import date, datetime
import json
import os


_configOut = []
key = "CUSTOM_NAME_CONFIG"

class carregarConfigs:

    #configurar variável de ambiente no windows

    def carregar(_config) -> list:
        docJson = open(f'../Standalone/appConfig_{os.getenv(key)}.json', 'r')
        print(f"{datetime.now()} - appConfig carregado appConfig_{os.getenv(key)}")
        obj = json.load(fp=docJson)
        doc = obj['connectionString'][0]

        _configOut.append(doc['Host'])
        _configOut.append(doc['Database'])
        _configOut.append(doc['User'])
        _configOut.append(doc['Password'])

        return _configOut
