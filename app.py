# -*- coding: utf-8 -*-

#載入LineBot所需要的套件
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import re
import random
app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('1Lv9YGU+MIfp4gJW2+VoXeMSC0Mm2kpKEpCuHnaOTr+hRkQjoQaJ9Ny/96rOGfJQUhFojyRQRmcH6xqF/hdsqSxD+2ruvYHK4cmnqy/XAtXE5kGieEOjCmPhElWP2JX+wah4JDqHjPi8VcqhjcUHygdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('506a66aac492ad00be8255b1a78832cc')

line_bot_api.push_message('U198bd80fbfca4c91633aaf2d8fc8f919', TextSendMessage(text='您好,目前時間是 2024/10/10 14:00 ，請問需要什麼服務呢?'))

# 監聽所有來自 /callback 的 Post Request
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

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = text=event.message.text
    stickers = [
        {"package_id": "6136", "sticker_id": "10551376"},
        {"package_id": "6136", "sticker_id": "10551377"},
        {"package_id": "6136", "sticker_id": "10551378"},
        {"package_id": "6136", "sticker_id": "10551379"},
        {"package_id": "6136", "sticker_id": "10551380"},
    ]

    if event.message.text:
        # 隨機選擇一個貼圖
        sticker = random.choice(stickers)
        sticker_message = StickerSendMessage(
            package_id=sticker["package_id"],
            sticker_id=sticker["sticker_id"]
        )
        line_bot_api.reply_message(event.reply_token, sticker_message)
    else:
        reply_text = '很抱歉，我目前無法理解這個內容。'
        line_bot_api.reply_message(event.reply_token, TextSendMessage(reply_text))
    if message == '天氣':
            reply_text = '請稍等，我幫您查詢天氣資訊！'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(reply_text))

    elif message == '心情好':
            sticker_message = StickerSendMessage(
            package_id='446',
            sticker_id='1993'  # 開心的貼圖
        )
            line_bot_api.reply_message(event.reply_token, sticker_message)

    elif message == '心情不好':
            sticker_message = StickerSendMessage(
            package_id='446',
            sticker_id='2006'  # 傷心的貼圖
        )
            line_bot_api.reply_message(event.reply_token, sticker_message)

    elif message == '找美食':
            location_message = LocationSendMessage(
            title='著名餐廳',
            address='Hog Island Oyster Co.',
            latitude=24.222173760252893,
            longitude= 120.57809735647335
        )
            line_bot_api.reply_message(event.reply_token, location_message)

    elif message == '找景點':
            location_message = LocationSendMessage(
            title='熱門景點',
            address='Skarðsáfossur',
            latitude=24.22738843546918,
            longitude= 120.58362305469898
        )
            line_bot_api.reply_message(event.reply_token, location_message)

    elif message == '熱門音樂':
            audio_message = AudioSendMessage(
            original_content_url='https://youtu.be/OIBODIPC_8Y?si=RBSY2FvE1GqPiFzj',  # 替換為實際的音樂檔案網址
            duration=240000  # 音樂長度（毫秒）
        )
            line_bot_api.reply_message(event.reply_token, audio_message)

    elif message == '放鬆音樂':
            audio_message = AudioSendMessage(
            original_content_url='https://youtu.be/DtBoAqkIJzI?si=lkRIr501M7irKNbs',  # 替換為實際的音樂檔案網址
            duration=300000  # 音樂長度（毫秒）
        )
            line_bot_api.reply_message(event.reply_token, audio_message)

    elif message == '今天是我的生日':
            image_message = ImageSendMessage(
            original_content_url='https://media.istockphoto.com/id/1136810581/zh/%E7%85%A7%E7%89%87/%E7%94%A8%E4%BA%94%E9%A1%8F%E5%85%AD%E8%89%B2%E7%9A%84%E7%81%91%E6%B0%B4%E5%92%8C%E5%8D%81%E6%94%AF%E8%A0%9F%E7%87%AD%E8%A3%9D%E9%A3%BE%E7%9A%84%E7%94%9F%E6%97%A5%E8%9B%8B%E7%B3%95.jpg?s=1024x1024&w=is&k=20&c=od9sL0ND3HdifCJa5wWabXQE3e9dM641kUC9YKrar4k=',  # 替換為實際的圖片網址
            preview_image_url='https://media.istockphoto.com/id/1136810581/zh/%E7%85%A7%E7%89%87/%E7%94%A8%E4%BA%94%E9%A1%8F%E5%85%AD%E8%89%B2%E7%9A%84%E7%81%91%E6%B0%B4%E5%92%8C%E5%8D%81%E6%94%AF%E8%A0%9F%E7%87%AD%E8%A3%9D%E9%A3%BE%E7%9A%84%E7%94%9F%E6%97%A5%E8%9B%8B%E7%B3%95.jpg?s=1024x1024&w=is&k=20&c=od9sL0ND3HdifCJa5wWabXQE3e9dM641kUC9YKrar4k='  # 替換為實際的預覽圖片網址
        )
            text_message = TextSendMessage(text='生日快樂！')
            line_bot_api.reply_message(event.reply_token, [image_message, text_message])

    elif message in ['動作片', '動畫', '紀錄片']:
        # 根據類型傳送影片
        video_urls = {
            '動作片': 'https://youtu.be/JeZwLiw_aE0?si=RkoVZZysESKCLp3O',
            '動畫': 'https://youtu.be/3OYgu5D2cxU?si=lQVmfgqUlhTp9zwQ',
            '紀錄片': 'https://youtu.be/u-puPhw2qj8?si=-bPFtmcALNZFmdy5'
        }
        video_url = video_urls.get(message)
        if video_url:
            reply_text = f'這是您要的{message}：\n{video_url}'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(reply_text))
        else:
            reply_text = '抱歉，沒有這類型的影片'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(reply_text))

    elif message in ['科幻']:
            reply_text = '抱歉，沒有這類型的影片'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(reply_text))

    else:
            reply_text = '很抱歉，我目前無法理解這個內容。'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(reply_text))
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
