from db_con import *
#connect heroku postgresql

def get_publish_D():
    conn = ps.connect(host="ec2-3-218-71-191.compute-1.amazonaws.com",
                      user="pauvcxweyckeaf",
                      password="115d8ec87368c3b65453a2d2988a7cbfd8bcb7db61f75afbd35b4519b152e3f7",
                      database="d5251933te7fta",
                      port="5432")
    cur = conn.cursor()
    cur.execute("SELECT PUB_ID,PREFERENCE,STUDENT_ID FROM PUBLISH_D WHERE PUB_CONDITION='刊登中'AND BOARD_PEOPLE='發起'")
    publish1=[]
    detail=list(cur.fetchone())
    while True:
        try:
            
            hour,minute=time(detail[0])
            detail.insert(2,(hour,minute))
            detail[2]=list(detail[2])
            publish1.append(detail)
            detail=list(cur.fetchone())
        except:
            break
    return publish1

def get_member(student_id):
    conn=database_connect()
    cur = conn.cursor()
    cur.execute("SELECT SEX,CREDIT_INDEX,NAME FROM MEMBER WHERE STUDENT_ID='"+student_id+"'")
    member = list(cur.fetchone())
    conn.commit()
    return member
def get_publish_M(pub_id):
    conn=database_connect()
    cur = conn.cursor()
    cur.execute("SELECT PUB_START,PUB_END FROM PUBLISH_M WHERE PUB_ID='"+pub_id+"'")
    publish2 = list(cur.fetchone())
    conn.commit()
    conn.close()
    return publish2
def get_order_M(user_id):
    conn=database_connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM ORDER_M WHERE USER_NAME='"+user_id+"'")
    order = list(cur.fetchall())
    conn.commit()
    conn.close()
    del order[2]
    del order[6]
    return order

def get_pub_id(user_id):
    conn=database_connect()
    cur = conn.cursor()
    cur2 = conn.cursor()
    historylist=[]
    cur.execute("SELECT ORDER_ID FROM ORDER_D WHERE STUDENT_ID='"+user_id+"'")
    order_id = list(cur.fetchall())
    for i in range(len(order_id)):
        orderid=str(order_id[i])[2:-3]
        cur2.execute("SELECT PUB_ID FROM ORDER_M WHERE ORDER_ID='"+orderid+"'")
        pub_id=cur2.fetchone()
        historylist.append(pub_id[0])
    conn.close()
    return historylist

def get_history(pubid):
    conn=database_connect()
    cur = conn.cursor()
    cur.execute("SELECT PUB_ID,CAR_DEALER,CAR_NUMBER,BOARD_START,BOARD_END,TOTAL_FARE FROM ORDER_M WHERE PUB_ID='"+pubid+"'")
    history = list(cur.fetchone())
    conn.commit()
    conn.close()
    return history

def get_max_min(pub_id):
    #max_min=[mydict[call][maxninum],mydict[call][minninum]]
    max_min=[3,0]
    return max_min

def time(pub_id):
    conn2 = ps.connect(host="ec2-3-218-71-191.compute-1.amazonaws.com",
                      user="pauvcxweyckeaf",
                      password="115d8ec87368c3b65453a2d2988a7cbfd8bcb7db61f75afbd35b4519b152e3f7",
                      database="d5251933te7fta",
                      port="5432")
    cur2 = conn2.cursor()
    cur2.execute("SELECT BOARDING_TIME FROM PUBLISH_D WHERE PUB_ID='"+pub_id+"'")
    datetime = str(cur2.fetchone())
    datetime=datetime.split(',')
    datetime[3]=datetime[3].replace(' ','')
    datetime[4]=datetime[4].replace(' ','')
    if int(datetime[3])>=16:
        datetime[3]=int(datetime[3])-16
    else:
        datetime[3]=int(datetime[3])+8
    return str(datetime[3]),str(datetime[4])
