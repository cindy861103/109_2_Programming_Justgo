from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

#======這裡是呼叫的檔案內容=====
from message import *
from new import *
from Function import *
from member import *
from line_actions import *
from ride import *
from answer import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time
#======python的函數庫==========

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('W1GQoPRSo/Hi3jJfw9pglREQNhpSygVEwp5yyxXcwm2YuAqonpTV67KfjwFf8AZJDkMWeg5l7Cgjd6kFSG3UW1XJ/SPa32+S7RluUmsKZP+6H4LKL49PCw2XpLldy/zGJbo//NsiCWpK6Pl1AGs/+gdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('deb96d058e24db881550880d5808ad13')
global mydict
mydict={}
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


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    try:
        line_id=event.source.user_id
        line_bot_api.push_message('Uad5f20670570a6aad3f1f20c893fe5a2',TextSendMessage(text=line_id+'發了:'+msg))
    except:
        message = TextSendMessage(text="錯誤")
        line_bot_api.reply_message(event.reply_token, message)
    if '會員' in msg:
        message = membersystem()
        line_bot_api.reply_message(event.reply_token, message)
    elif '揪車情況/取消揪車' in msg:
        message = membe78rsystem1()
        line_bot_api.reply_message(event.reply_token, message)
    elif '使用說明/QA/其他' in msg:
        message = other12()
        line_bot_api.reply_message(event.reply_token, message)
    elif '尋找共乘' in msg:
        message = prohibit_or_not(line_id)
        if '【很抱歉_cancelcondtion】' in message:
            message=message.replace('很抱歉_cancelcondtion','')
            try:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
            except:
                line_bot_api.push_message(line_id,TextSendMessage(text="錯誤訊息"))
        mydict[line_id]['want']={}
        message = chooseleadtype()
        try:
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.push_message(line_id,TextSendMessage(text="錯誤訊息"))
#其他

    elif '使用說明_1' in msg:
        message = '''使用說明：\n1.本服務僅供用戶尋找共乘夥伴，不牽扯到商業利益。我們也不鼓勵轉賣、租借等行為。\n2.用戶需登入方能使用共乘服務，第一次使用本服務的用戶請點選會員→註冊進行註冊帳號，並上傳學生證照片認證身分。\n3.本服務的起始點和終點目前只有捷運士林站、捷運劍南路站、東吳大學外雙溪校區、東吳大學城中校區四個地點供選擇。\n4.用戶成功加入揪車後，發起人用戶將能看到乘客的學號及系級。\n
5.用戶發起揪車或加入揪車的情況，在發車三十分鐘前都能進行取消，取消成功後同車的用戶將會收到通知。若用戶沒做取消卻沒到現場，將視為跑單。第一次跑單將會限制用戶帳號一個月，第二次三個月，第三次永久封號。\n6.若有用戶跑單，發起人可在共乘完成後進入舉報系統舉報該用戶，系統核實後將針對該用戶進行處理。'''
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
    elif 'Q&A' in msg:
        message = '''Q：我想取消揪車，但取消時間已過，我還能取消嗎？\n
A：您好，在發車前三十分鐘都是能做取消的喔！如果超過時間，將會視為跑單。第一次跑單將會暫停用戶使用帳號一個月，第二次三個月，第三次永久封號，還請注意喔！
\nQ：我的學生證遺失，但我仍想認證帳號，請問有別的認證方法嗎？\n
A：您好，考慮到在校身分確認，我們目前暫不開放上傳學生證以外的途徑認證喔，還請見諒。
'''
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
    elif '其他_1' in msg:
        message = '''EMAIL: justgocarpool@gmail.com'''
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))  
    elif '註冊' in msg:
        try:
            if line_id not in mydict:
                mydict[line_id]={}
                mydict[line_id]["register"]={}
                line_bot_api.push_message(line_id,TextSendMessage(text='檢測到此id未註冊過，進行註冊程序'))
            else:
                line_bot_api.push_message(line_id,TextSendMessage(text='檢測到此id註冊過，進行更改資料程序'))
        except:
            line_bot_api.push_message(line_id,TextSendMessage(text="失敗"))
        message = register(msg, line_id,mydict)
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message))
    #測試用
    elif '呼叫字典' in msg:
        message = str(mydict)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
    #洪學姊部分
    elif '更改資料' in msg:
        message = update_info(line_id)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
    elif '查看信用值' in msg:
        message = credit_check(line_id)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
    elif '查看歷史記錄' in msg:
        message = id_log(line_id)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
    elif '_dbmbcheck' in msg: # 註冊 與否的回覆
        message = student_id(msg, line_id)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
    elif '_sid' in msg: # student_id的回覆
        message = name(msg, line_id,mydict)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
    elif '_name' in msg:  # name的回覆
        message = depart(msg, line_id,mydict)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
    elif '_depart' in msg: # depart的回覆
        message = sex(msg, line_id,mydict)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
    elif '_sex' in msg: # sex的回覆
        message = password(msg, line_id,mydict)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
    elif '_idpass' in msg: # password的回覆
        message = password_check(msg, line_id,mydict)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
    elif '_passchk' in msg: # password_check的回覆
        message = email_check(msg, line_id,mydict)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
    elif '_passchk' in msg: # email_check的回覆 _cknum
        message = password_match(msg, line_id,mydict) 
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
    elif '_upchk' in msg: # password_check的回覆
        message = update_mb()
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
    #管理員回訊息
    elif '回訊息' in msg:
        try:
            replayid=msg[:33]
            massage=msg[37:]
            #"\nby管理員"
            line_bot_api.push_message(replayid,TextSendMessage(text=massage))
        except:
            #line_bot_api.push_message(line_id,TextSendMessage(text="失敗"))
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='請點選圖文表單上的功能，進入服務喔！'))
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='訊息回覆成功'))
    elif '_upchky' in msg: # password_check的回覆
        message = update_mb()
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
    elif '乘車類別_' in msg:
        jointype(msg,line_id,mydict)
        message = chooselocation()
        try:
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.push_message(line_id,TextSendMessage(text="錯誤訊息"))     
            
    elif '目的地_' in msg:
        joinplace(msg,line_id,mydict)#list型態
        pub_id=getLocationId(mydict[line_id]['want']('chooseservice'),mydict[line_id]['want']('pub_end'),mydict,line_id)
        message = destination(pub_id,line_id,mydict)
        message=message+'================\n觀看該項詳細資\n觀看完整佈告欄\n請輸入您的選擇：\n'+'【格式｜都不想要／共乘編號_(需為完整編號)】'
        try:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message ))
        except:
            line_bot_api.push_message(line_id,TextSendMessage(text="錯誤訊息"))
        
    elif '共乘編號' or '重新輸入共乘' in msg:
        exist=checkPubId(int(pubId))
        if exist:
            try:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text="您要加入的共乘是編號xxx\n請進行確認\n"+
                                                                            "【格式｜確認共乘／重新輸入共乘】"))
            except:
                line_bot_api.push_message(line_id,TextSendMessage(text="錯誤訊息"))
        else:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="沒有此筆共乘，請重新輸入\n【格式｜共乘編號_(需為完整編號)】"))      

    elif '確認共乘_' in msg:
        joinadd(msg,line_id,pubId)
        line_bot_api.push_message(line_id,TextSendMessage(text="已加入共乘！請在規定時間內抵達現場！"))
        if startjoin(line_id):
            if mydict[line_id]['call']['chooseservice']=='湊滿人後叫車':
                changePub_condition(pubId)
                people=getpeople(pubId)
                for i in people:
                    try:
                        line_bot_api.push_message(callperson,TextSendMessage(text="此筆訂單已湊滿人\n請進行最後確認"))
                        message=comformtogo()
                        try:
                            line_bot_api.push_message(callperson,message)
                        except:
                            line_bot_api.push_message(callperson,TextSendMessage(text="錯誤訊息"))
                                                    
                    except:
                        line_bot_api.push_message(i,TextSendMessage(text="錯誤訊息"))
            else:
                callperson=findcall(pubId)
                try:
                    line_bot_api.push_message(callperson,TextSendMessage(text="你目前的訂單總共有"+
                    mydict[callperson]['call']['finalcheckpassenger']+"位共乘者\n若車子已抵達請輸入【車子已抵達】"))
                    ##finalcheckpassenger'+1?
                except:
                    line_bot_api.push_message(callperson,TextSendMessage(text="錯誤訊息"))
                    
    elif '狀態繼續' or '查看狀態' or '_cancelcondtion' in msg:
        message = prohibit_or_not(line_id)
        if '【很抱歉_cancelcondtion】' in message:
            message=message.replace('很抱歉_cancelcondtion','')
            try:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
            except:
                line_bot_api.push_message(line_id,TextSendMessage(text="錯誤訊息"))
        identity,message=now(line_id)#看到此訂單的詳細資訊
        if identity:
            line_bot_api.push_message(line_id,TextSendMessage(text=+'目前你是：'+identity+'者\n'+
                                                        message+'\n若要取消發車或共乘\n'+
                                                        '請輸入："【格式｜更改狀態_發車／更改狀態_共乘】'))
        else:
            line_bot_api.push_message(line_id,TextSendMessage(text=message))

    elif '更改狀態_' in msg:
        message = prohibit_or_not(line_id)
        if '【很抱歉_cancelcondtion】' in message:
            message=message.replace('很抱歉_cancelcondtion','')
            try:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
            except:
                line_bot_api.push_message(line_id,TextSendMessage(text="錯誤訊息"))
        try:
            line_bot_api.push_message(line_id, TextSendMessage(text='發起人最晚可接受的取消時間為發車時間前'+
                                                        mydict[line_id]['call']['acceptable_waiting_time']+'分鐘。\n'+
                                                        '若已超過規定時間則信用值將會-1。\n'))
            identity,message=now(line_id)
            #####程式邏輯
            if identity:
                credit_index=getCredit_index(line_id)
                try:
                    line_bot_api.push_message(line_id,TextSendMessage(text="你現在的信用值為："+str(credit_index)))
                except:
                    line_bot_api.push_message(line_id,TextSendMessage(text="錯誤訊息"))
                    
                message=deletejoin(identity)##按鈕
                try:
                    line_bot_api.reply_message(event.reply_token, message)
                except:
                    line_bot_api.push_message(line_id,TextSendMessage(text="錯誤訊息"))
            else:
                line_bot_api.push_message(line_id,TextSendMessage(text=message))
        except:
            line_bot_api.push_message(line_id,TextSendMessage(text="錯誤訊息"))

    elif '真的不要' in msg:
        situation=TimeOk(line_id)
        try:
            if situation:
                nojoin(line_id)
                line_bot_api.push_message(line_id, TextSendMessage(text='取消成功！\n目前您的信用值為：'+
                mydict[line_id]['register']['credit_index']+'\n'))
            else:
                line_bot_api.push_message(line_id,TextSendMessage(text='已過可取消之時間，您已無法取消共乘。\n'+
                                                        '請注意跑單將會被封禁帳號喔。\n'+
                                                        '(第一次一個月，第二次三個月，第三次永久)'))
            message=now(line_id)
            try:
                line_bot_api.push_message(line_id,TextSendMessage(text=message))
            except:
                line_bot_api.push_message(line_id,TextSendMessage(text="錯誤訊息"))
        except:
            line_bot_api.push_message(line_id,TextSendMessage(text="錯誤訊息"))
    elif '即時資訊' in msg:
        message = 'url'
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message) )
    elif '我要揪車' in msg:
        message = prohibit_or_not(line_id)
        if '【很抱歉_cancelcondtion】' in message:
            message=message.replace('很抱歉_cancelcondtion','')
            try:
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.push_message(line_id,TextSendMessage(text="錯誤訊息"))
        else:
            mydict[line_id]["call"] = {}
            message=chooseservice(msg, line_id)
            try:
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.push_message(line_id,TextSendMessage(text="錯誤訊息"))

    elif '服務項目_' in msg:
        mydict[line_id]["call"]["chooseservice"] = msg[5:]
        message = pub_start(msg, line_id)
        try:
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.push_message(line_id,TextSendMessage(text="錯誤訊息"))

    elif '起始點_' in msg:
        if "重新選擇" not in msg:
            mydict[line_id]["call"]["pub_start"] = msg[4:]
        else:
            message = chooselocation(msg, line_id)
            try:
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.push_message(line_id,TextSendMessage(text="錯誤訊息"))

    elif '地址_' in msg:
        try:
            line_bot_api.push_message(line_id,TextSendMessage(text="請輸入確認地址"))
        except:
            line_bot_api.push_message(line_id,TextSendMessage(text="錯誤訊息"))

    elif '自行輸入地址' in msg:
        message = chooselocation_others(msg, line_id)
        try:
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.push_message(line_id,TextSendMessage(text="錯誤訊息"))

    elif "確認地址" in msg:
        mydict[line_id]["call"]["chooselocation"] = msg[3:]
        message = boarding_time(msg, line_id)
        try:
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.push_message(line_id,TextSendMessage(text="錯誤訊息"))

    elif '_時間為_' in msg:
        mydict[line_id]["call"]["boarding_time"] = msg[3:]
        if mydict[line_id]["call"]["chooseservice"] == "湊滿人後叫車":
            message = acceptable_waiting_time(msg, line_id)    
            try:
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.push_message(line_id,TextSendMessage(text="錯誤訊息"))
        else:
            message = cancel_time(msg, line_id)
            try:
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.push_message(line_id,TextSendMessage(text="錯誤訊息"))

    elif '願意等待時間為_' in msg:
        mydict[line_id]["call"]["acceptable_waiting_time"] = msg[7:]
        message = minimum(msg, line_id)
        try:
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.push_message(line_id,TextSendMessage(text="錯誤訊息"))

    elif '取消時間為_' in msg:
        mydict[line_id]["call"]["cancel_time"] = msg[5:]
        message = minimum(msg, line_id)
        try:
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.push_message(line_id,TextSendMessage(text="錯誤訊息"))

    elif '最低發車人數_' in msg:
        mydict[line_id]["call"]["minimum"] = msg[7:]
        message = maximum(msg, line_id)
        try:
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.push_message(line_id,TextSendMessage(text="錯誤訊息"))

    elif '最多可承載人數_' in msg:
        mydict[line_id]["call"]["maximum"] = msg[8:]
        message = car_dealer(msg, line_id)
        try:
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.push_message(line_id,TextSendMessage(text="錯誤訊息"))
    elif '叫車方式_' in msg:
        mydict[line_id]["call"]["car_dealer"] = msg[3:]
        if car_dealer == "路邊攔車":
            mydict[line_id]["call"]["driver"] = "無"
            mydict[line_id]["call"]["car_number"] = "無"
        else:     
            message = driver(msg, line_id)
            try:
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.push_message(line_id,TextSendMessage(text="錯誤訊息"))
#攔車怎辦(進哪個迴圈)
    elif '司機名稱_' in msg:
        mydict[line_id]["call"]["driver"] = msg[5:]
        message = car_number(msg, line_id)    
        try:
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.push_message(line_id,TextSendMessage(text="錯誤訊息"))

    elif '車牌號碼_' in msg:
        if car_number[8] != "-" and car_number[8] != "－" and len(car_number) != 13:
            message="格式輸入錯誤，請重新輸入"
        else:
            mydict[line_id]["call"]["car_number"] = msg[5:]
            message = preference(msg, line_id)
        try:
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.push_message(line_id,TextSendMessage(text="錯誤訊息"))

    elif '乘車偏好_' in msg:
        mydict[line_id]["call"]["preference"] = msg[5:]
        message = checkinfo(msg, line_id,mydict)
        try:
            line_bot_api.push_message(line_id,TextSendMessage(text=message))
            message = checkinfo_button(msg, line_id)
            try:
                line_bot_api.reply_message(event.reply_token, message)    
            except:
                line_bot_api.push_message(line_id,TextSendMessage(text="錯誤訊息"))
        except:
            line_bot_api.push_message(line_id,TextSendMessage(text="錯誤訊息"))
    elif '確認資料_' in msg:
        database_publish_m(msg, line_id, mydict)
        message = database_publish_d(msg, line_id)
        try:
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.push_message(line_id,TextSendMessage(text="錯誤訊息"))
    elif "最終確認_" in msg:
        pub_id = mydict[line_id]['want']['join']
        callperson=findcall(pub_id)
        if "是" in msg:
            mydict[callperson]["call"]["finalcheckpassenger"]+=1
        else:                                                                                                                                                                                                                                                                                                                                                                                                                                                
            mydict[callperson]["call"]["finalcheckpassenger"]-=1
        if mydict[callperson]["call"]["finalcheckpassenger"] == mydict[callperson]["call"]["minimum"]:
            notice = getpeople(pub_id)
            for i in notice:
                try:
                    line_bot_api.push_message(i,TextSendMessage(text="此訂單已發車，請儘速抵達目的地"))
                    identity,message=now(line_id)#看到此訂單的詳細資訊
                    if identity:
                        line_bot_api.push_message(line_id,TextSendMessage(text='目前你是：'+identity +'者\n'+message+'\n若要取消發車或共乘\n'+'請輸入："【格式：更改狀態_發車／更改狀態_共乘】'))
                    else:
                        line_bot_api.push_message(line_id,TextSendMessage(text=message))
                except:
                    line_bot_api.push_message(line_id,TextSendMessage(text="錯誤訊息"))
    elif "車子已抵達" in msg:
        callperson = findcall(pubId)
        if callperson:
            try:
                line_bot_api.push_message(line_id,TextSendMessage(text="請填入車上人數：(格式：車上人數_阿拉伯數字，例如：車上人數_3)"))    
            except:
                line_bot_api.push_message(line_id,TextSendMessage(text="錯誤訊息"))
    elif "車上人數_" in msg:
        numberofpasssenger = msg.replace('車上人數_','')
        people = len(list(getpeople(pubId)))
        if numberofpasssenger != people:
            message = checkifontime(msg, line_id)
            people = list(getpeople(pubId))
            for i in people:
                try:
                    line_bot_api.push_message(line_id,TextSendMessage(message))    
                except:
                    line_bot_api.push_message(line_id,TextSendMessage(text="錯誤訊息"))    

    elif "我已上車" in msg:
        database_order_d(msg, line_id,mydict,pub_number)
        database_order_m(msg, line_id,mydict,pub_number)
        update_publish(msg, line_id)
        try:
            line_bot_api.push_message(line_id,TextSendMessage(text = "若已抵達目的地請輸入【共乘完畢】"))    
        except:
            line_bot_api.push_message(line_id,TextSendMessage(text="錯誤訊息"))  

    elif '共乘完畢' in msg:
        message = callperson_confirm_price(line_id,mydict[line_id]['call']['pub_id'])
        try:
            line_bot_api.push_message(line_id,TextSendMessage(text=message))    
        except:
            line_bot_api.push_message(line_id,TextSendMessage(text="錯誤訊息"))
        
    elif '確認金額_' in msg:
        money = msg.replace('確認金額_','')
        message = confirm_price(line_id,money)
        try:
            line_bot_api.push_message(line_id,TextSendMessage(text=message))    
        except:
            line_bot_api.push_message(line_id,TextSendMessage(text="錯誤訊息"))

    elif '金額_' in msg:
        pubid=mydict[line_id]['want']['pub_id']
        callperson=findcall(pubId)#取得發起人名單
        mydict[callperson]['call']['checkmoney']+=1
        if "金額_正確" in msg:
            if mydict[callperson]['call']['checkmoney']==mydict[callperson]['call']['finalcheckpassenger']:
                try:
                    line_bot_api.push_message(line_id,TextSendMessage(text="此筆訂單已完成"))
                except:
                    line_bot_api.push_message(line_id,TextSendMessage(text="錯誤訊息"))
    elif "金額_錯誤" in msg:     
        mydict[line_id]['call']['checkmoney'] =0
        message = callperson_confirm_price(msg, line_id)
        try:
            line_bot_api.push_message(line_id,TextSendMessage(text="金額輸入錯誤，請再試一遍"+message))
        except:
            line_bot_api.push_message(line_id,TextSendMessage(text="錯誤訊息"))

    else:
        message = TextSendMessage(text="請點選圖文表單上的功能，進入服務喔！")
        line_bot_api.reply_message(event.reply_token,message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)



"""elif '尋找共乘' in msg:
        message = chooseservice()
        line_bot_api.reply_message(event.reply_token, message)"""