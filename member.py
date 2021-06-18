# -*- coding: utf-8 -*-

# 安裝相關的所有套件
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
import psycopg2
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from string import Template
from pathlib import Path
import random
import os

## 連線Database # 宣告db
'''db_connect'''
def database_connect():
    # connect heroku postgresql
    conn = psycopg2.connect(host="ec2-3-218-71-191.compute-1.amazonaws.com",
                      user="pauvcxweyckeaf",
                      password="115d8ec87368c3b65453a2d2988a7cbfd8bcb7db61f75afbd35b4519b152e3f7",
                      database="d5251933te7fta",
                      port="5432")
    return conn


'''call_db_action'''
# -*- coding: utf-8 -*-

# 經由button按下傳來的msg(註冊)及line_id，判斷此使用者是否註冊過。
'''
已註冊(True)--->linebot進行更名流程(背後運行依然是註冊流程)
未註冊(False)--->linebot直接進行註冊流程
'''
# read member data from database
def read_from_member(line_id):
    conn = database_connect()
    #database_connect()
    cursor = conn.cursor()

    sql = f"""SELECT * FROM member WHERE student_id is NOT NULL AND line_id = %s"""
    cursor.execute(sql, (line_id,))
    register_or_not = cursor.fetchall()
    if register_or_not != []:
        # 已註冊
        conn.close()
        return True
    else:
        # 未註冊
        conn.close()
        return False
    
    #cursor.close()
    #conn.close()

# write member data to database


def write_to_member(member):
    conn = database_connect()
    cursor = conn.cursor()
    insert_data = member
    table_columns = '(student_id, line_id, name, depart, sex, password, credit_index, cancel_times)'
    sql = f"""INSERT INTO member {table_columns} VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"""
    cursor.execute(sql, insert_data)
    conn.commit()
    cursor.close()
    conn.close()

# read member credit_index from database


def check_credit_index(line_id):
    conn = database_connect()
    cursor = conn.cursor()

#     # SQL-1
#     sql =f"""SELECT credit_index FROM member WHERE student_id is NOT NULL AND line_id = %s"""
#     cursor.execute(sql, (line_id,))
    # SQL-2
    sql = f"""SELECT credit_index FROM member WHERE student_id is NOT NULL AND line_id = '{line_id}';"""
    cursor.execute(sql)

    credit_index = cursor.fetchall()
    credit_score = [i[0] for i in credit_index][0]
    cursor.close()
    conn.close()
    return credit_score

# update member data to database


def update_member_info(update_member):
    conn = database_connect()
    cursor = conn.cursor()

    update_mb = update_member
    sql = f"""UPDATE member SET student_id = %s, name = %s, depart = %s, sex = %s, password = %s where line_id = %s;"""
    cursor.execute(sql, (update_mb[0], update_mb[2],
                         update_mb[3], update_mb[4], update_mb[5], update_mb[1]))
    conn.commit()

    cursor.close()
    conn.close()

# read member student_id from database


def get_sid_link(line_id):
    conn = database_connect()
    cursor = conn.cursor()

    sql = f"""SELECT student_id FROM member WHERE student_id is NOT NULL AND line_id = '{line_id}';"""
    cursor.execute(sql)

    student_id = cursor.fetchall()
    sid = [i[0] for i in student_id][0]

    link = '?'+'name =' + sid
    cursor.close()
    conn.close()
    return link


## 註冊Register

### 先判斷是否註冊過
### 開始進入註冊系統
# Q:new member check, A:none
# msg == '註冊'
def register(msg, line_id,mydict):
    db_result = read_from_member(line_id)
    if db_result == True: #呼叫更改資料的流程
        mydict[line_id]['register'] = {} #初始化['register]的dict
        txt = '''您好！
您已經是我們的會員，
不需再進行註冊。
那我們就視為資料更新的流程呦！
請輸入：【格式：Yes_更改資料】
'''
    elif db_result == False:
        txt = '''歡迎來到會員註冊系統，
本服務現僅供東吳在學學生使用，
一人限註冊一次，
還請特別注意囉！
以下請務必依照問題後的格式回答！
請輸入：【格式：Yes_dbmbcheck】
'''
    return txt


"""### 開始註冊流程(學號-->姓名-->系級-->性別-->密碼)"""
# Q:student_id, A:dbmbcheck(new member check)
def student_id(msg, line_id): #msg-->dbmbcheck的回覆
    txt = "請輸入您的學號：【格式：學號_sid】"
    return txt

# Q:name, A:student_id
def name(msg, line_id,mydict): #msg-->student_id的回覆
    '''try:
        line_bot_api.push_message(line_id,TextSendMessage(text='2'))
    except:
        line_bot_api.push_message(line_id,TextSendMessage(text='錯誤'))'''
    #mydict[line_id]['register']['student_id'] = msg[:msg.index('_')]
    msg=msg[:8]
    mydict[line_id]['register']['student_id']=msg
    txt = "請輸入您的姓名：【格式：姓名_name】"
    return txt

# Q:depart, A:name
def depart(msg, line_id,mydict): #msg-->name的回覆
    mydict[line_id]['register']['name'] = msg[:msg.index('_')]
    txt = "請輸入您的系級：【格式：系級_depart】"
    return txt

# Q:sex, A:depart
def sex(msg, line_id,mydict): #msg-->depart的回覆
    mydict[line_id]['register']['depart'] = msg[:msg.index('_')]
    txt = "請輸入您的性別：【格式：性別_sex】"
    return txt

# Q:password, A:sex
def password(msg, line_id,mydict): #msg-->sex的回覆
    mydict[line_id]['register']['sex'] = msg[:msg.index('_')]
    txt = "請輸入您的密碼：【格式：密碼_idpass】"
    return txt

# Q:password_check, A:password
def password_check(msg, line_id,mydict): #msg-->password的回覆
    mydict[line_id]['register']['password'] = msg[:msg.index('_')]

    regis_member = list(mydict[line_id]['register'].values())
    regis_member.insert(1, line_id)
    #regis_mb_t = tuple(regis_member)
    db_result = read_from_member(line_id)
    if db_result == True: #呼叫更改資料的流程
        txt = f'''
以下是您輸入的資料，請確認是否正確。
--------------------------
您的學號：{regis_member[0]}
您的姓名：{regis_member[2]}
您的系級：{regis_member[3]}
您的生理性別：{regis_member[4]}
您設定的密碼：{regis_member[5]}
--------------------------
【格式：正確或錯誤_upchk】
'''
    elif db_result == False:
        txt = f'''
以下是您輸入的資料，請確認是否正確。
--------------------------
您的學號：{regis_member[0]}
您的姓名：{regis_member[2]}
您的系級：{regis_member[3]}
您的生理性別：{regis_member[4]}
您設定的密碼：{regis_member[5]}
--------------------------
【格式：正確或錯誤_passchk】
'''
    random_num(line_id,mydict) # call random number
    return txt


"""### 開始驗證流程"""
#郵件發送函數
def sendMail(toAccount, name, random_num):
    subject = '東吳大學【揪車Go平臺】郵件驗證碼認證'
    SMTPHost = 'smtp.gmail.com'   # 郵件服務器
    fromAccount = 'justgocarpool@gmail.com'  # 寄件信箱
    fromPasswd = 'hjyffibbosdrpduj'  # 寄件郵件授權碼(不是郵箱登錄密碼)

    #建立郵件
    msg = MIMEMultipart()  # 建立MIMEMultipart物件
    msg['Subject'] = Header(subject, 'utf-8')  # 郵件標題
    msg['From'] = fromAccount  # 寄件者
    msg['To'] = toAccount  # 收件者
#     msg["Accept-Language"]="zh-TW"
#     msg["Accept-Charset"]="ISO-8859-1,utf-8"

    # 郵件正文
    template = Template(Path("email_content.html").read_text(encoding='utf-8'))
    body = template.substitute({"name": name,  # 收件人姓名
                                "random_num": random_num})  # 隨機驗證碼
    msg.attach(MIMEText(body, 'html', 'utf-8'))

    # 附件(圖片)
    xlsxpart = MIMEApplication(
        open('justgo.png', 'rb').read())  # 當前目錄下的附件文件
    xlsxpart.add_header('Content-Disposition',
                        'attachment', filename='justgo.png')
    msg.attach(xlsxpart)

    # 使用smtplib模塊發送郵件
    with smtplib.SMTP(host=SMTPHost, port="587") as smtp:  # 設定SMTP伺服器
        try:
            smtp.ehlo()  # 驗證SMTP伺服器
            smtp.starttls()  # 建立加密傳輸
            smtp.login(fromAccount, fromPasswd)  # 登入寄件者gmail
            smtp.send_message(msg)  # 寄送郵件
            return True
        except Exception as e:
            return False


def random_num(line_id,mydict):
    # 隨機驗證碼
    num = []
    for i in range(6):
        i = str(random.randint(0,9))
        num.append(i)
        value = ''.join(num)
    # 將random_num寫入dict
    #value = msg[:msg.index('_')] 
    mydict[line_id]['register']['random_num'] = value


# Q:email_check, A:password_check
def email_check(msg, line_id,mydict): #msg-->password_check的回覆
    random_num = mydict[line_id]['register']['random_num']
    flag = msg[:msg.index('_')]
    if flag == '正確':
        # call send email function
        name = mydict[line_id]['register']['name']
        student_id = mydict[line_id]['register']['student_id']
        student_id_email = str(student_id+'@scu.edu.tw')
        sendMail(student_id_email, name, random_num)
        txt = f'''現正進入帳號驗證的流程，
        我們會寄一封email給您，
        請您至{student_id}@scu.edu.tw收信並回傳驗證碼。
        【格式：驗證碼_cknum】'''
    else:
        txt = '由於資料確認錯誤，請重新進行註冊流程【輸入：註冊】'
    return txt

# Q:password_match, A:email_check
def password_match(msg, line_id,mydict): #msg-->email_check的回覆
    #random_num=mydict[line_id]['register']['random_num']
    msg = msg[:msg.index('_')]
    #if random_num == msg:
    txt = '恭喜您已註冊成功，可以開始使用我們提供的服務！'

        # write member into database
    regis_member = list(mydict[line_id]['register'].values())
    regis_member.insert(1, line_id)
    member = tuple(regis_member)
    write_to_member(member)
    """else:
        txt = '您的驗證碼有誤，請查詢後再輸入一次。【輸入：註冊】'"""
    return txt


"""## 更改資料"""
# Q:new member check, A:none
# msg == '更改資料'
def update_info(line_id):
    db_result = read_from_member(line_id)
    if db_result == True: #呼叫更改資料的流程
        txt = '''您好！
現已進入更改資料的流程，
--------------
以下項目是可以更改的，
1.學號：【格式：學號_sid】
2.姓名：【格式：姓名_name】
3.系級：【格式：系級_depart】
4.性別：【格式：性別_sex】
5.密碼：【格式：密碼_idpass】
--------------
請依照自己想要更改的項目，
對應後面的格式進行填寫。
'''
    elif db_result == False:
        txt = '''您目前不是我們的會員，
暫且無法使用更改資料的服務，
請先進行會員註冊。
之後請務必依照問題後的格式回答！
請輸入：【格式：Yes_dbmbcheck】
'''
    return txt

# Q:email_check, A:password_check(update)
def update_mb(msg, line_id,mydict): #msg-->password_check(update)的回覆
    #random_num = mydict[line_id]['register']['random_num']
    flag = msg[:msg.index('_')]
    if flag == '正確':
        # call update db function
        regis_member = list(mydict[line_id]['register'].values())
        regis_member.insert(1, line_id)
        update_mb = tuple(regis_member)
        update_member_info(update_mb)
        txt = '恭喜您已更新資料成功，歡迎您再次使用我們提供的服務！'
    else:
        txt = '由於資料確認錯誤，請重新進行更改資料流程【輸入：更改資料】'
    return txt


"""## 查看信用值"""
# Q:new member check, A:none
# msg == '查看信用值'
def credit_check(line_id):
    db_result = read_from_member(line_id)
    if db_result == True: #呼叫查看信用值
        score = check_credit_index(line_id)
        txt = f"您好！以下為您目前的信用值為：{score}分"

    elif db_result == False:
        txt = '''您目前不是我們的會員，
暫且無法使用查詢服務，
請先進行會員註冊。
之後請務必依照問題後的格式回答！
請輸入：【格式：Yes_dbmbcheck】
'''
    return txt


"""## 查看歷史記錄"""
# Q:new member check, A:none
# msg == '查看歷史記錄'
def id_log(line_id):
    link = 'https://www.google.com/?hl=zh_tw' #<--這裡要改成柏尹的佈告欄
    db_result = read_from_member(line_id)
    if db_result == True: #發送查看歷史記錄的連結
        txt = f'''您好！下方連結是整合型的記錄彙整佈告欄，\n{link}\n。'''
    elif db_result == False:
        txt = '''您目前不是我們的會員，
暫且無法使用查詢服務，
請先進行會員註冊。
之後請務必依照問題後的格式回答！
請輸入：【格式：Yes_dbmbcheck】
'''
    return txt

