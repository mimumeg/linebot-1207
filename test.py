import os

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)
talk = {
    "こんにちは": "こんにちは！",
    "好き": "私も❤️",
}

# 環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ[
    "qS9zXpoiYmzb7+dWfXM6+IDgFTfyNOinhOwrp3eBesBDyZLMJKUDPjhJBTn86sR1VGCDHQY15+RXx5YjLq3NR1jR5UmneTqlAMr3fxwyC3BWiPW0AKMl8ezgROVS5Iiv6j553vWEd1Qsq9jPgIs54AdB04t89/1O/w1cDnyilFU="]
YOUR_CHANNEL_SECRET = os.environ["9147ed6793ced76b51ecaca979f181aa"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)

    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text in talk:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=talk[event.message.text]))
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    #    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
