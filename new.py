#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

def test():
    message = TemplateSendMessage(
        alt_text='圖片旋轉木馬',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/NkOCTRl.jpg",
                    action=URITemplateAction(
                        label="橘黃",
                        uri="https://plus.google.com/116237864387312784020/posts/S327kJKy6HG"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/tzpIEbX.jpg",
                    action=URITemplateAction(
                        label="橘紅",
                        uri="https://cdn.101mediaimage.com/img/file/1410464751urhp5.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/QXqpjZv.jpg",
                    action=URITemplateAction(
                        label="紅褐",
                        uri="http://imgm.cnmo-img.com.cn/appimg/screenpic/big/674/673928.JPG"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/ZL8mXUd.jpg",
                    action=URITemplateAction(
                        label="深褐",
                        uri="https://m-miya.net/wp-content/uploads/2014/07/0-065-1.min_.jpg"
                    )
                )
            ]
        )
    )
    return message
