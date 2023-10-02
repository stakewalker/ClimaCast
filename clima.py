import requests
import json
from datetime import datetime

clima = "<climatempo-token>"
tl_key = "<telegram-api-key>"
chat_id = "<channel-chat_id>"
city_id = "<city_id>"

def call_tele(msg):
    requests.get('https://api.telegram.org/bot' + tl_key + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + msg)

now = requests.get(f"https://apiadvisor.climatempo.com.br/api/v1/weather/locale/{city_id}/current?token={clima}").json()['data']
all_temps = requests.get(f"http://apiadvisor.climatempo.com.br/api/v2/forecast/temperature/locale/{city_id}/hours/168?token={clima}").json()['temperatures']

temps = [[i['date'].split(" ")[1][:5], i['value']] for i in all_temps]

message = f"""🗓️ {datetime.now().strftime("%d/%m/%Y")}

Dia com {now['condition'].lower()}
🌡️ Sensação térmica: {now['sensation']}ºC

Temperaturas: 
🕗 {temps[0][0]}  {temps[0][1]}ºC
🕙 {temps[2][0]}  {temps[2][1]}ºC
🕛 {temps[4][0]}  {temps[4][1]}ºC
🕑 {temps[6][0]}  {temps[6][1]}ºC
🕓 {temps[8][0]}  {temps[8][1]}ºC
🕕 {temps[10][0]}  {temps[10][1]}ºC
🕗 {temps[12][0]}  {temps[12][1]}ºC
"""
