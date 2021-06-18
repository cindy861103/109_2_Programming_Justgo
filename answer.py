from db_actions import *
import datetime
from new import *
def now(lineid,mydict):
    try:        
        pubId=mydict[lineid]['want']['join']
        lineid=findcall(pubId)
        return '共乘',pubdetail(lineid)

    except:
        
        try:
            pubId=mydict[lineid]['call']['pub_id']
            lineid=findcall(pubId)
            return '發起',pubdetail(lineid)
        
        except:
            return False,'目前沒有加入或發起共乘！'

def TimeOk(lineid,mydict):
    okh=str(mydict[lineid]['call']['cancel_time'])[0:2]
    okm=str(mydict[lineid]['call']['cancel_time'])[3:5]
    oksec=int(okh)*60+int(okm)

    nowh=str(datetime.now().time())[0:2]
    nowm=str(datetime.now().time())[3:5]
    nowsec=int(nowh)*60+int(nowm)
    
    if nowsec < oksec :
        return True
    else:
        return False

def nojoin(lineid,mydict,pubId,user):
    mydict[lineid]['register']['credit_index']=mydict[lineid]['register']['credit_index']-1
    changeCredit_index(lineid,mydict[lineid]['register']['credit_index'])
    del mydict[lineid]['want']
    mydict[lineid]['call']['passenger']-=1
    changePub_people(pubId,user)

def startjoin(lineid,mydict):
    if mydict[lineid]['call']['passenger']==mydict[lineid]['call']['minimum']:
        return True
    else:
        return False
        

