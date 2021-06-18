from member import *
import datetime
#http://tw.gitbook.net/postgresql/2013080998.html

# 先判斷是否註冊過
# 經由button按下傳來的msg(註冊)及line_id，判斷此使用者是否註冊過。
'''
已註冊(True)--->linebot進行更名流程(背後運行依然是註冊流程)
未註冊(False)--->linebot直接進行註冊流程
'''
# read member data from database
def read_from_member(line_id):
    conn = database_connect()
    cursor = conn.cursor()

    sql = f"""SELECT * FROM member WHERE student_id is NOT NULL AND line_id = %s"""
    cursor.execute(sql, (line_id,))
    register_or_not = cursor.fetchall()
    if register_or_not != []:
        # 已註冊
        return True
    else:
        # 未註冊
        return False
    conn.close()

def check_cancel_times(line_id):
    conn = database_connect()
    cursor = conn.cursor()

    sql = f"""SELECT cancel_times FROM member WHERE student_id is NOT NULL AND line_id = '{line_id}';"""
    cursor.execute(sql)

    cancel = cursor.fetchall()
    cancel_times = [i[0] for i in cancel][0]
    cursor.close()
    conn.close()
    return cancel_times

def changePub_people(pubId,user):
    conn=database_connect()
    cur = conn.cursor()
    cur.execute("UPDATE PUBLISH_D SET PUB_CONDITION='共乘失敗' WHERE PUB_ID='"+pubId+"' AND STUDENT_ID='"+user+"'") 
    conn.commit()
    conn.close()

def changePub_cancel(pubId,line_id):
    cancel=str(check_cancel_times(line_id))
    cancel=int(cancel)+1
    conn=database_connect()
    cur = conn.cursor()
    cur.execute("UPDATE MEMBER SET cancel_times="+str(cancel)+" WHERE LINE_ID='"+line_id+"'")
    conn.commit()
    conn.close()

def changePub_condition(pubId):
    conn=database_connect()
    cur = conn.cursor()
    cur.execute("UPDATE PUBLISH_D SET PUB_CONDITION='已滿' WHERE PUB_ID='"+pubId+"'")
    conn.commit()
    conn.close()
 
def getpeople(pubId):#取得共乘者名單，一定要
    conn=database_connect()
    cur = conn.cursor()
    cur.execute("SELECT STUDENT_ID FROM PUBLISH_D WHERE PUB_ID='"+pubId+"'")
    board_people = list(cur.fetchall())
    conn.close()
    return board_people

def getLocationId(startType,pub_end,mydict,line_id):#取得目的地，一定要
    conn=database_connect()
    cur = conn.cursor()
    cur2 = conn.cursor()
    getpubid=[]
    a=0
    while True:
        cur.execute("SELECT PUB_ID FROM PUBLISH_M WHERE PUB_END='"+pub_end+"' AND PUB_CONDITION='刊登中'")
        pub_id=cur.fetchone()
        cur2.execute("SELECT STUDENT_ID FROM PUBLISH_D WHERE PUB_ID='"+pub_id+"' AND BOARD_PEOPLE='發起'")
        student_id = cur.fetchone()
        line_id=getuser(student_id)
        if mydict[line_id]['call']['chooseservice'] == startType :
            getpubid.append(mydict[line_id]['call']['pub_id'])
            a=a+1
            if a == 5:
                break
    conn.close()
    return getpubid

def getuser(studentid):#使用者學號拿lineID，一定要
    conn=database_connect()
    cur = conn.cursor()
    cur.execute("SELECT LINE_ID FROM MEMBER WHERE STUDENT_ID ='"+studentid+"'")
    lineid = cur.fetchone()
    conn.commit()
    conn.close()
    return lineid

def checkPubId(pubId):#確認是否有訂單，一定要
    conn=database_connect()
    cur = conn.cursor()
    cur.execute("SELECT PUB_D_ID FROM PUBLISH_D WHERE PUB_ID = '"+pubId+"'")
    exits=cur.fetchone()
    if exits:
        return True
    else:
        return False

def addpeople(userdict,user,pubId,pub_number,mydict,lineid):#新增一筆訂單，一定要PUB_D_ID
    date=str(datetime.now().date().today()).split('-')
    date=date[0]+date[1]+date[2]
    if len(str(pub_number)) == 1:
        pub_d_number='00'+str(pub_number)
    elif len(str(pub_number))==2:
        pub_number='0'+str(pub_number)
    pubDId='P'+date+pub_number
    conn=database_connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO PUBLISH_D(PUB_D_ID,PUB_ID,STUDENT_ID,PREFERENCE,"+
                "BOARD_PEOPLE,BOARDING_TIME,PUB_CONDITION) "+
                "VALUES ('"+pubDId+"','"+mydict[user]['call']['pub_id']+"','"+user+
                mydict[lineid]['call']['preference']+"','共乘','"+"',"+mydict[lineid]['call']['time']+"','刊登中')")
    print(cur.rowcount)
    conn.commit()
    conn.close()

def getpeople(pubId):#取得共乘者名單，一定要
    conn=database_connect()
    cur = conn.cursor()
    cur.execute("SELECT LINE_ID FROM PUBLISH_D WHERE PUB_ID='"+pubId+"'")
    board_people = list(cur.fetchall())
    conn.commit()
    return board_people

def findcall(pubId):#取得發起人名單，一定要
    conn=database_connect()
    cur = conn.cursor()
    cur.execute("SELECT LINE_ID FROM PUBLISH_D WHERE PUB_ID='"+pubId+"' AND BOARD_PEOPLE='發起'")
    callperson = list(cur.fetchone())
    conn.commit()
    return callperson[0] 

def getCredit_index(user):
    conn=database_connect()
    cur = conn.cursor()
    cur.execute("SELECT CRDEIT_INDEX FROM MEMBER WHERE LINE_ID='"+user+"'")
    credit_index = cur.fetchone()
    conn.commit()
    conn.close()
    return credit_index

def changeCredit_index(user,pubId):
    conn=database_connect()
    cur = conn.cursor()
    cur.execute("UPDATE PUBLISH_D SET PUB_CONDITION='共乘失敗' WHERE PUB_ID='"+pubId+"' AND STUDENT_ID='"+user+"'")
    conn.commit()
    conn.close()

def database_publish_m(msg, line_id,pub_number, mydict):
    date=str(datetime.now().date().today()).split('-')
    date=date[0]+date[1]+date[2]
    if len(str(pub_number))==1:
        pub_number='00'+str(pub_number)
    elif len(str(pub_number))==2:
        pub_number='0'+str(pub_number)

    pub_id = 'P'+date+str(pub_number)
    pub_start = mydict[line_id]["call"]["pub_start"][4:]
    pub_end = mydict[line_id]["call"]["chooselocation"][3:]
    pub_date = date

    conn = database_connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO publish_m (pub_id, pub_start, pub_end, pub_date)"+
    "VALUES ("+pub_id+", "+pub_start+", "+pub_end+", "+pub_date+")")
    conn.commit()
    conn.close()

def database_publish_d(line_id,pub_number, mydict):
    date=str(datetime.now().date().today()).split('-')
    date=date[0]+date[1]+date[2]
    if len(str(pub_number))==1:
        pub_number='00'+str(pub_number)
    elif len(str(pub_number))==2:
        pub_number='0'+str(pub_number)
    pub_d_id = pub_number ##型態是int，可能會出錯
    pub_id = 'P'+date+str(pub_number)
    student_id = mydict[line_id]['register']['student_id']
    preference = mydict[line_id]["call"]["preference"][5:]
    board_people = mydict[line_id]['want']   
    boarding_time = mydict[line_id]["call"]["boarding_time"][3:]
    pub_condition = "刊登中"

    conn = database_connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO publish_d (pub_d_id, pub_id, student_id, preference, board_people, boarding_time, pub_condition)"+
    "VALUES ("+pub_d_id+", "+pub_id+", "+student_id+", "+preference+", "+board_people+", "+boarding_time+", "+pub_condition+")");
    conn.commit()
    conn.close()

def database_order_d(msg, line_id, pub_number, mydict):
    date=str(datetime.now().date().today()).split('-')
    date=date[0]+date[1]+date[2]
    if len(str(pub_number))==1:
        pub_number='00'+str(pub_number)
    elif len(str(pub_number))==2:
        pub_number='0'+str(pub_number)

    order_d_id = date+str(pub_number)
    order_id = date+str(pub_number)
    student_id = mydict[line_id]['register']['student_id']
    preference = mydict[line_id]["call"]["preference"][5:]
    board_people = mydict[line_id]['want']
    real_pay = mydict[line_id]['want']['checkmoney']
    boarding_time = mydict[line_id]["call"]["boarding_time"][3:]
    order_condition = "乘車中"

    conn = database_connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO order_d (order_d_id, order_id, student_id, preference, board_people, real_pay, boarding_time, order_condition)"+
    "VALUES ("+order_d_id+", "+order_id+", "+student_id+", "+preference+", "+board_people+", "+real_pay+", "+boarding_time+", "+order_condition+")")
    conn.commit()
    conn.close()

def database_order_m(msg, line_id, pub_number, mydict):
    date=str(datetime.now().date().today()).split('-')
    date=date[0]+date[1]+date[2]
    if len(str(pub_number))==1:
        pub_number='00'+str(pub_number)
    elif len(str(pub_number))==2:
        pub_number='0'+str(pub_number)

    order_id = date+str(pub_number, mydict)
    pub_id = 'P'+order_id
    car_dealer = mydict[line_id]["call"]["car_dealer"][3:]
    car_number = mydict[line_id]["call"]["car_number"][5:]
    board_start = mydict[line_id]["call"]["pub_start"][4:]
    board_end = mydict[line_id]["call"]["chooselocation"][3:]
    total_fare = 0
    order_date = date

    conn = database_connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO order_m (order_id, pub_id, car_dealer, car_number, board_start, board_end, total_fare, order_date)"+
    "VALUES ("+order_id+", "+pub_id+", "+car_dealer+", "+car_number+", "+board_start+", "+board_end+", "+total_fare+", "+order_date+")")
    conn.commit()
    conn.close()

def update_publish(msg, line_id):
    conn = database_connect()
    cur = conn.cursor()
    cur.execute("UPDATE publish_m SET pub_condition = '刊登完成' WHERE pub_condition = '刊登中'")
    conn.close()

def jointype(msg,line_id,mydict):
    msg=msg.replace('乘車類別_','')
    mydict[line_id]['want']['chooseservice']=msg
    
def joinplace(msg,line_id,mydict):
    msg=msg.replace('目的地_','')
    mydict[line_id]['want']['pub_end']=msg
    
def joinadd(msg,line_id,mydict,user,pubId):
    msg=msg.replace('共乘編號_','')
    mydict[line_id]['want']['join']=msg
    if mydict[line_id]['want']['chooseservice']=='湊滿人後叫車':
        mydict[line_id]['call']['passenger']+=1
    else:
        mydict[line_id]['call']['finalcheckpassenger']+=1
    addpeople(user,pubId)##寫入sql

##跑單用
def noshow(line_id,mydict):
    changePub_condition(mydict[line_id]['call']['pubId'],line_id)
    date=str(datetime.now().date().today()).split('-')
    date=date[0]+date[1]+date[2]
    mydict[line_id]['register']['prohibition_start']=date

def passenger(msg, line_id, mydict):
    mydict[line_id]["call"]["passenger"] = 0
    mydict[line_id]["call"]["finalcheckpassenger"] = 0
    mydict[line_id]['call']['checkmoney'] = 0
    