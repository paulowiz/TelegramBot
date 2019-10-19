import json
import pandas as pd
from pandas.io.json import json_normalize
import pandas.io.json as pd_json
import apiconsume as ap
from pandas.io.json import json_normalize
import pandas.io.json as pd_json
import datetime
import time
import os

ultdt = 0

while (True):
    apitel = ap.apiConsume()
    retorno = apitel.executaEndpoint('getUpdates')
    data = retorno['result']
    for reg in data:
        if reg['message']['date'] > ultdt:
            print(reg['update_id'])
            print(reg['message']['text'])
            print(reg['message']['from']['id'])
            print(reg['message']['from']['first_name'])
            print(reg['message']['date'])
            print('----------------------------------------------')
            chat_id = reg['message']['chat']['id']
            apitel.sendMessage(chat_id, 'Estou te respondendo')
            ultdt = (reg['message']['date'])

        print('Esperando alguém responder.........')
