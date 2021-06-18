#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

def cancelcheck():
    message = TemplateSendMessage(
        alt_text='是否確定取消共乘？',
        template=ConfirmTemplate(
            text="是否確定取消共乘？",
            actions=[
                PostbackTemplateAction(
                    label="確定取消",
                    text="確定取消",
                    data="確定取消"
                ),
                PostbackTemplateAction(
                    label="放棄取消",
                    text="放棄取消",
                    data="放棄取消"
                )
            ]
        )
    )
    return message

def chooselocation():
    message = TemplateSendMessage(
        alt_text='請選擇目的地',
        template=ButtonsTemplate(
            text="請選擇目的地",
            actions=[
                PostbackTemplateAction(
                    label="1.捷運士林站",
                    text="目的地:捷運士林站",
                    data="1"
                ),
                PostbackTemplateAction(
                    label="2.捷運劍南路站",
                    text="目的地:捷運劍南路站",
                    data="2"
                ),
                PostbackTemplateAction(
                    label="3.東吳大學外雙溪校區",
                    text="目的地:東吳大學外雙溪校區",
                    data="3"
                ),
                PostbackTemplateAction(
                    label="4.東吳大學城中校區",
                    text="目的地:東吳大學城中校區",
                    data="4"
                )
            ]
        )
    )
    return message


def justgosystem():
    message = TemplateSendMessage(
        alt_text='請選擇目的地',
        template=ButtonsTemplate(
            text="請選擇目的地",
            actions=[
                PostbackTemplateAction(
                    label="1.捷運士林站",
                    text="目的地:捷運士林站",
                    data="1"
                ),
                PostbackTemplateAction(
                    label="2.捷運劍南路站",
                    text="目的地:捷運劍南路站",
                    data="2"
                ),
                PostbackTemplateAction(
                    label="3.東吳大學外雙溪校區",
                    text="目的地:東吳大學外雙溪校區",
                    data="3"
                )
            ]
        )
    )
    return message

def membersystem():
    message = TemplateSendMessage(
        alt_text='請選擇會員功能',
        template=ButtonsTemplate(
            text="請選擇會員功能",
            actions=[
                PostbackTemplateAction(
                    label="註冊",
                    text="註冊",
                    data="1"
                ),
                PostbackTemplateAction(
                    label="更改會員資料",
                    text="更改資料",
                    data="3"
                ),
                PostbackTemplateAction(
                    label="查看信用值",
                    text="查看信用值",
                    data="2"
                ),
                PostbackTemplateAction(
                    label="查看歷史記錄",
                    text="查看歷史記錄",
                    data="4"
                )
            ]
        )
    )
    return message   
#TemplateSendMessage - ImageCarouselTemplate(圖片旋轉木馬)

def cancelcheck11():
    message = TemplateSendMessage(
        alt_text='是否確定取消共乘？',
        template=ConfirmTemplate(
            text="是否確定取消共乘？",
            actions=[
                PostbackTemplateAction(
                    label="確定取消",
                    text="確定取消",
                    data="確定取消"
                ),
                PostbackTemplateAction(
                    label="放棄取消",
                    text="放棄取消",
                    data="放棄取消"
                )
            ]
        )
    )
    return message



def acceptable_waiting_time():
    message = TemplateSendMessage(
        alt_text='請選擇願意等待時間',
        template=ButtonsTemplate(
            text="請選擇願意等待時間",
            actions=[
                PostbackTemplateAction(
                    label="5分鐘",
                    text="願意等待時間_5分鐘",
                    data="1"
                ),
                PostbackTemplateAction(
                    label="10分鐘",
                    text="願意等待時間_更改資料",
                    data="3"
                ),
                PostbackTemplateAction(
                    label="15分鐘",
                    text="願意等待時間_15分鐘",
                    data="2"
                ),
                PostbackTemplateAction(
                    label="20分鐘",
                    text="願意等待時間_20分鐘",
                    data="4"
                )
            ]
        )
    )
    return message 

def other12():
    message = TemplateSendMessage(
        alt_text='請選擇功能',
        template=ButtonsTemplate(
            text="請選擇功能",
            actions=[
                PostbackTemplateAction(
                    label="使用說明",
                    text="使用說明_1",
                    data="2"
                ),
                PostbackTemplateAction(
                    label="QA",
                    text="Q&A",
                    data="3"
                ),
                PostbackTemplateAction(
                    label="其他",
                    text="其他_1",
                    data="4"
                )
            ]
        )
    )
    return message
def membe78rsystem1():
    message = TemplateSendMessage(
        alt_text='請選擇功能',
        template=ButtonsTemplate(
            text="請選擇功能",
            actions=[
                PostbackTemplateAction(
                    label="揪車情況",
                    text="揪車情況_",
                    data="2"
                ),
                PostbackTemplateAction(
                    label="取消揪車",
                    text="取消揪車",
                    data="3"
                ),
                PostbackTemplateAction(
                    label=" ",
                    text=" ",
                    data=" "
                )
            ]
        )
    )
    return message


def chooseleadtype():
    message = TemplateSendMessage(
        alt_text='請選擇發車種類',
        template=ButtonsTemplate(
            text="請選擇發車種類",
            actions=[
                PostbackTemplateAction(
                    label="1.一定會發車",
                    text="乘車類別_確定發車",
                    data="否"
                ),
                PostbackTemplateAction(
                    label="2.湊滿人才發車",
                    text="乘車類別_湊滿人後叫車",
                    data="否"
                ),
                PostbackTemplateAction(
                    label=" ",
                    text=" ",
                    data=" "
                ),
            ]
        )
    )
    return message

def destination(pub_id,line_id,mydict):##簡要的
    msg=''
    for i in range(5):
        msg=msg+'編號：\n'+str(pub_id[i])
        msg=msg+'　起始點:'+mydict[line_id]['call']['pub_start']+'\n'
        msg=msg+'　目的地:'+mydict[line_id]['call']['chooselocation']+'\n'
        msg=str(msg+'　發車時間:'+mydict[line_id]['call']['time']+'\n')    
        msg=msg+'　目前人數(成團基本人數/上限人數)：'+str(mydict[line_id]['call']['passenger'])+ '('+str(mydict[line_id]['call']['minimum'])+'/'+str(mydict[line_id]['call']['maximum'])+')'
        msg=msg+'　備註'+mydict[line_id]['call']['preference']
    return msg

def pubdetail(line_id,mydict):##詳細的
    msg=('發起人：'+mydict[line_id]['register']['name'][0]+'同學'+
         '\n起始點：'+mydict[line_id]['call']['pub_start']+
         '\n目的地：'+mydict[line_id]['call']['chooselocation']+
         '\n發車時間：'+mydict[line_id]['call']['time']+
         '\n目前人數(成團基本人數/上限人數)：'+mydict[line_id]['call']['passenger']+'('+mydict[line_id]['call']['minimum']+'/'+mydict[line_id]['call']['maximum']+')'+
         '\n叫車方式：'+mydict[line_id]['call']['car'][0]+
         '\n司機名稱：'+mydict[line_id]['call']['car'][1]+
         '\n車牌號碼：'+mydict[line_id]['call']['car'][2]+
         '\n乘車偏好/備註：'+mydict[line_id]['call']['preference'])
    return msg

def deletejoin(identity):
    if identity == '發起':
        message = TemplateSendMessage(
            alt_text='確定取消發起請按"確定取消"，不然請按"不取消"',
            template=ButtonsTemplate(
                text='確定取消發起請按"確定取消"，不然請按"不取消"',
                actions=[
                    PostbackTemplateAction(
                        label="確定取消",
                        text="真的不要",
                        data="123"
                        ),
                    PostbackTemplateAction(
                        label="不取消",
                        text="狀態繼續",
                        data="123"
                        ),
                    PostbackTemplateAction(
                            label=" ",
                            text=" ",
                            data=" "
                        ),
                    ]
                )
            )
        return message
    else:
        message = TemplateSendMessage(
            alt_text='確定取消共乘請按"確定取消"，不然請按"不取消"',
            template=ButtonsTemplate(
                text='確定取消共乘請按"確定取消"，不然請按"不取消"',
                actions=[
                    PostbackTemplateAction(
                        label="確定取消",
                        text="真的不要",
                        data="123"
                    ),
                    PostbackTemplateAction(
                        label="不取消",
                        text="狀態繼續",
                        data="123"
                    ),
                    PostbackTemplateAction(
                        label=" ",
                        text=" ",
                        data=" "
                    ),
                ]
            )
        )
        return message

def comformtogo():
    message = TemplateSendMessage(
        alt_text='是否要搭乘',
        template=ButtonsTemplate(
            text="是否要搭乘",
            actions=[
                PostbackTemplateAction(
                    label="是",
                    text="最終確認_是",
                    data="否"
                ),
                PostbackTemplateAction(
                    label="否",
                    text="最終確認_否",
                    data="否"
                ),
                PostbackTemplateAction(
                    label=" ",
                    text=" ",
                    data=" "
                ),
            ]
        )
    )
    return message

def chooseservice():
    message = TemplateSendMessage(
        alt_text='請選擇服務項目',
        template=ButtonsTemplate(
            text="請選擇服務項目",
            actions=[
                PostbackTemplateAction(
                    label="確定發車",
                    text="服務項目_確定發車",
                    data="1"
                ),
                PostbackTemplateAction(
                    label="湊滿人後叫車",
                    text="服務項目_湊滿人後叫車",
                    data="2"
                ),
                PostbackTemplateAction(
                    label=" ",
                    text=" ",
                    data=" "

                )
            ]
        )
    )
    return message

def chooselocation():
    message = TemplateSendMessage(
        alt_text='請選擇目的地',
        template=ButtonsTemplate(
            text="請選擇目的地",
            actions=[
                PostbackTemplateAction(
                    label="1.東吳大學外雙溪校區",
                    text="地址_台北市士林區臨溪路70號",
                    data=" 2"
                ),
                PostbackTemplateAction(
                    label="2.捷運士林站",
                    text="地址_台北市士林區中正路",
                    data=" 2"
                ),
                PostbackTemplateAction(
                    label="3.捷運劍南路站",
                    text="地址_台北市中山區北安路",
                    data=" 2"
                ),
                PostbackTemplateAction(
                    label="4.東吳大學城中校區",
                    text="地址_台北市中正區貴陽街一段56號",
                    data=" 2"
                ),
                PostbackTemplateAction(
                    label="5.其他",
                    text="自行輸入地址",
                    data=" 2"
                )
            ]
        )
    )
    return message

def location_confirm():
    message = TemplateSendMessage(
        alt_text='請確認地址',
        template=ButtonsTemplate(
            text="請確認地址",
            actions=[
                PostbackTemplateAction(
                    label="確認",
                    text="確認地址",
                    data=" 2"
                ),
                PostbackTemplateAction(
                    label="重新選擇",
                    text="起始點_重新確認", 
                    data=" 2"
                ),
                PostbackTemplateAction(
                    label=" ",
                    text=" ", 
                    data=" "
                )

            ]
        )
    )
    return message

def checkinfo_button():
    message = TemplateSendMessage(
        alt_text='請確認資料',
        template=ButtonsTemplate(
            text="請確認資料",
            actions=[
                PostbackTemplateAction(
                    label="確定無誤",
                    text="確認資料_正確", 
                    data=" 2"
                ),
                PostbackTemplateAction(
                    label="資料有誤，重新填寫",
                    text="確認資料_錯誤", 
                    data=" 2"
                ),
                PostbackTemplateAction(
                    label=" ",
                    text=" ", 
                    data=" "
                )
            ]
        )
    )
    return message

def checkifontime():
    message = TemplateSendMessage(
        alt_text='若已上車時請按',
        template=ButtonsTemplate(
            text="若已上車時請按",
            actions=[
                PostbackTemplateAction(
                    label="我已上車",
                    text="我已上車", 
                    data=" "
                ),
                PostbackTemplateAction(
                    label=" ",
                    text=" ", 
                    data=" "
                ),
                PostbackTemplateAction(
                    label=" ",
                    text=" ", 
                    data=" "
                ),
            ]
        )
    )
    return message

