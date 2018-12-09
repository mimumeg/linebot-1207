import os

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TemplateSendMessage, CarouselColumn, CarouselTemplate)

app = Flask(__name__)

LINE_CHANNEL_ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
LINE_CHANNEL_SECRET = os.environ["CHANNEL_SECRET"]

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def response_message(event):
    # notesのCarouselColumnの各値は、変更してもらって結構です。
    notes = [CarouselColumn(
        thumbnail_image_url="https://www.pokemon.co.jp/PostImages/71a75d97ded2bcf355e903390ea7a63948d2bad1.jpg",
        title="もふ？非もふ？",
        text="直感的にお答え下さい！",
        actions=[
                                {"type": "message", "label": "もふ💕", "text": "https://www.google.com"},
                                {"type": "message", "label": "非もふ⚡", "text": "https://www.google.com"}])

             # CarouselColumn(thumbnail_image_url="https://renttle.jp/static/img/renttle03.jpg",
             #                title="ReleaseNote】創作中の活動を報告する機能を追加しました。",
             #                text="創作中や考え中の時点の活動を共有できる機能を追加しました。",
             #                actions=[
             #                    {"type": "message", "label": "サイトURL", "text": "https://renttle.jp/notes/kota/6"}]),
             #
             # CarouselColumn(thumbnail_image_url="https://renttle.jp/static/img/renttle04.jpg",
             #                title="【ReleaseNote】タグ機能を追加しました。",
             #                text="「イベントを作成」「記事を投稿」「本を登録」にタグ機能を追加しました。",
             #                actions=[
             #                    {"type": "message", "label": "サイトURL", "text": "https://renttle.jp/notes/kota/5"}])
             ]

    messages = TemplateSendMessage(
        alt_text='template',
        template=CarouselTemplate(columns=notes),
    )

    line_bot_api.reply_message(event.reply_token, messages=messages)


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
