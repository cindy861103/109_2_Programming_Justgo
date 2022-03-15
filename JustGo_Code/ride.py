import datetime
from db_actions import *
from dateutil.relativedelta import *
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

pub_number=3

def pub_start():
    return "請輸入起始點(格式：起始點_地址，例如：起始點_台北市A區B路C號)："

def chooselocation_others():
    return "請輸入地址(格式：_地址_目的地地址，例如：_地址_台北市A區B路C號)："

def boarding_time():
    boarding_time = input("請輸入最遲發車時間 (格式：時間為幾時幾分，例如：時間為0130,時間為0815,時間為1745)：")  
    boarding_timeminutes = int(boarding_time[3:5])*60+int(boarding_time[5:7])

    nowhour = str(datetime.now().time())[0:2]
    if int(nowhour) > 15:
        nowhour = int(nowhour)-16
    nowmin = str(datetime.now().time())[3:5]
    nowminutes = int(nowhour)*60+int(nowmin)

    due_timeminutes = 23*60 + 59

    if boarding_timeminutes > due_timeminutes:
        print("僅限今日24時前")
    if boarding_timeminutes < nowminutes:
        print("需晚於現在時間")
    return boarding_time

def cancel_time(msg, line_id, boarding_timeminutes):  
    cancel_time = input("請輸入最遲可接受的取消時間 (格式：取消時間為幾時幾分，例如：取消時間為0130,取消時間為0815,取消時間為1745)：")
    cancel_timeminutes = int(cancel_time[3:5])*60+int(cancel_time[5:7])

    nowhour = str(datetime.now().time())[0:2]
    if int(nowhour) > 15:
        nowhour = int(nowhour)-16
    nowmin = str(datetime.now().time())[3:5]
    nowminutes = int(nowhour)*60+int(nowmin)

    due_timeminutes = 23*60 + 59

    if cancel_timeminutes > due_timeminutes:
        print("僅限今日24時前")
    if cancel_timeminutes < nowminutes:
        print("需晚於現在時間")
    if cancel_timeminutes < boarding_timeminutes:
        print("需晚於最遲發車時間")
    return cancel_time

def minimum(msg, line_id):
    return "請輸入最低發車人數：(格式：最低發車人數_阿拉伯數字，例如：最低發車人數_2)"

def maximum(msg, line_id):
    return "請輸入最多可承載人數：(格式：最多可承載人數_阿拉伯數字，例如：最多可承載人數_4)"

def car_dealer(msg, line_id):
    return "請輸入叫車方式：(格式：叫車方式_方式，例如：叫車方式_臺灣大車隊)"

def driver(msg, line_id):
    return "請輸入司機名稱：(格式：司機名稱_名字，例如：司機名稱_王小明)"

def car_number(msg, line_id):
    return "請輸入車牌號碼 (格式：車牌號碼_英英英-數數數數，例如：車牌號碼_ABC-1234)："

def preference(msg, line_id):
    return "請輸入乘車偏好：(格式：乘車偏好_偏好1&偏好2&偏好3，例如：乘車偏好_安靜&無菸&限同性)："

#發起人id有問題
def checkinfo(msg, line_id ,mydict):
    if mydict[line_id]["call"]["chooseservice"] == "確定發車":
        msg=('發起人：'+mydict[line_id]['register']['name'][0]+'同學'+
             '\n起始點：'+mydict[line_id]['call']['pub_start']+
             '\n目的地：'+mydict[line_id]['call']['chooselocation']+
             '\n最遲發車時間：'+mydict[line_id]['call']['boarding_time']+
             '\n最遲可接受的取消時間：'+mydict[line_id]['call']['cancel_time']+
             '\n目前人數(成團基本人數/上限人數)：'+mydict[line_id]['call']['passenger']+'('+mydict[line_id]['call']['minimum']+'/'+mydict[line_id]['call']['maximum']+')'+
             '\n叫車方式：'+mydict[line_id]['call']['car_dealer']+
             '\n司機名稱：'+mydict[line_id]['call']['driver']+
             '\n車牌號碼：'+mydict[line_id]['call']['car_number']+
             '\n乘車偏好/備註：'+mydict[line_id]['call']['preference'])
    else:        
        msg=('發起人：'+mydict[line_id]['register']['name'][0]+'同學'+
             '\n起始點：'+mydict[line_id]['call']['pub_start']+
             '\n目的地：'+mydict[line_id]['call']['chooselocation']+
             '\n發車時間：'+mydict[line_id]['call']['boarding_time']+             
             '\n願意等待時間：'+mydict[line_id]['call']['acceptable_waiting_time']+
             '\n目前人數(成團基本人數/上限人數)：'+mydict[line_id]['call']['passenger']+'('+mydict[line_id]['call']['minimum']+'/'+mydict[line_id]['call']['maximum']+')'+
             '\n乘車偏好/備註：'+mydict[line_id]['call']['preference'])
    msg="請確認是否正確，格式：correct_正確\n"+msg
    return msg
#5



def callperson_confirm_price():
    return "請輸入此趟旅程的金額：(格式：確認金額_訂單總金額，例如：確認金額_300)"

def confirm_price(line_id, money, mydict, getpeople):
    pubId=mydict[line_id]['call']['pub_id']
    people = list(getpeople(pubId))
    if (money%len(people)) != 0:
        money = money-(money%len(people)) 
    pay = money/(len(people))
    for i in people: 
        try:
            line_bot_api.push_message(i,TextSendMessage(text="已到達目的地，此次搭乘金額為：【"+pay+"】元，請確認\n"+
                                                         "【格式：金額_確認／金額_錯誤】"))
        except:
            line_bot_api.push_message(line_id,TextSendMessage(text="錯誤訊息"))

def prohibit_or_not(line_id,mydict):
    # 取得棄單次數
    cancel_times = check_cancel_times(line_id)

    # 取得禁用日期
    pro_s = mydict[line_id]['register']['prohibition_start']

    # 取現在日期(日期格式)
    now_dt = datetime.now().today()

    #_cancelcondtion--->會員棄單的狀況
    if pro_s != '':
        pro_dt = datetime.strptime(pro_s, '%Y%m%d')
        if cancel_times == 1:
            pro_end = pro_dt + relativedelta(months=+ 1)  # 取得禁用1個月後的日期
            result = pro_end > now_dt  # 禁用結束日期是否小於現在日期
            if result == True:  # 禁用結束日期小於現在日期
                txt = f"很抱歉，\n您現在仍處於禁用階段，\n請等到{pro_end.year}年{pro_end.month}月{pro_end.day}日後再開始使用服務。【_cancelcondtion】"
            elif result == False:  # 禁用結束日期大於現在日期
                txt = f"恭喜您，\n您現在已解封，歡迎再次使用本平臺服務。\n請注意您只剩一次的棄單機會，\n累計滿三次，\n則永久封號。【_cancelcondtion】"
        elif cancel_times == 2:
            pro_end = pro_dt + relativedelta(months=+ 3)  # 取得禁用3個月後的日期
            result = pro_end > now_dt  # 禁用結束日期是否小於現在日期
            if result == True:  # 禁用結束日期小於現在日期
                txt = f"很抱歉，\n您現在仍處於禁用階段，\n請等到{pro_end.year}年{pro_end.month}月{pro_end.day}日後再開始使用服務。【_cancelcondtion】"
            elif result == False:  # 禁用結束日期大於現在日期
                txt = f"恭喜您，\n您現在已解封，歡迎再次使用本平臺服務。\n請注意您已無棄單額度，\n若下次再棄單，\n則永久封號。【_cancelcondtion】"
        elif cancel_times >= 3:
            txt = "很抱歉，\n您由於已經惡意棄單三次，\n故已永久封號，\n現無法使用本平臺服務。【_cancelcondtion】"
    else:
        txt = "您現在並沒有棄單紀錄，\n歡迎繼續使用本平臺服務。【_cancelcondtion】"
    return txt

