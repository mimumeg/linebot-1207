import os

from flask import Flask
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.models import (
    MessageEvent, TextMessage)

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ["ACCESS_TOKEN"])
handler = WebhookHandler(os.environ["CHANNEL_SECRET"])

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    ### 相手のプロフィールを取得
    profile = line_bot_api.get_profile(event.source.user_id)

    ### コンファームテンプレートメッセージを作る

    confirm_template_message = TemplateSendMessage(
        alt_text='Confirm template',
        template=ConfirmTemplate(
            text=profile.display_name + 'さん\nアンケートにご協力ください。',
            actions=[
                PostbackAction(
                    label='YES',
                    data='yes',
                ),
                MessageAction(
                    label='NO',
                    text='no')
            ]
        )
    )

    ### コンファームテンプレートメッセージを送る
    line_bot_api.reply_message(
        event.reply_token, confirm_template_message
    )
