# -*- coding:utf-8 -*-
import json
import urllib.error

url = 'https://api.line.me/v2/bot/message/push'
channel_access_token = '[qS9zXpoiYmzb7+dWfXM6+IDgFTfyNOinhOwrp3eBesBDyZLMJKUDPjhJBTn86sR1VGCDHQY15+RXx5YjLq3NR1jR5UmneTqlAMr3fxwyC3BWiPW0AKMl8ezgROVS5Iiv6j553vWEd1Qsq9jPgIs54AdB04t89/1O/w1cDnyilFU=]'
user_id = '[U723f832780a5c27a07e12c5797cf5c10]'
# 送信用のデータ
data = {
    'to': user_id,
    'messages': [
        {
            'type': 'text',
            'text': 'Hello, world! from api'
        }
    ]
}
jsonstr = json.dumps(data)
print(jsonstr)
# Content-Type:application/json
# Authorization:Bearer {channel access token}
# method:post
request = urllib.Request(url, data=jsonstr)
request.add_header('Content-Type', 'application/json')
request.add_header('Authorization', 'Bearer ' + channel_access_token)
request.get_method = lambda: 'POST'
# 送信実行
response = urllib.urlopen(request)
ret = response.read()
print('Response:', ret)
