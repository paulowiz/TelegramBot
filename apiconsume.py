import json
import requests
import pandas as pd
from pandas.io.json import json_normalize
import pandas.io.json as pd_json

url = "https://api.telegram.org/bot836761478:AAGNHIhV5o3WplgCf-Pqa1A8vYbZldygsmo/"


class apiConsume:

    def __init__(self):
        print('')

    # Executa query graphql

    def executaEndpoint(self, endPoint):
        dados = requests.get(url + endPoint)
        dados = dados.json()
        dados = json.dumps(dados, indent=4)
        retorno = json.loads(dados)
        return retorno

    def sendMessage(self, chat_id, message_text):
        params = {"chat_id":chat_id,"text": message_text}
        response = requests.post(url + "sendMessage", data=params)
        return print('Mensagem enviada com sucesso!')


pass
