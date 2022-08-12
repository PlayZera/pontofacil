import json



_configOut = []

class carregarConfigs:


    def carregar(_config) -> list:
        docJson = open('Distribuicao/Standalone/appConfig.json', 'r')

        obj = json.load(fp=docJson)
        doc = obj['connectionString'][0]

        _configOut.append(doc['Host'])
        _configOut.append(doc['Database'])
        _configOut.append(doc['User'])
        _configOut.append(doc['Password'])

        return _configOut
