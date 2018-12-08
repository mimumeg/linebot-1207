# -*- coding:utf-8 -*-
import json
import urllib.error

url = 'https://api.line.me/v2/bot/message/push'
channel_access_token = '[作成したchannel_access_token]'
user_id = '[Your user IDに表示されている値]'
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
