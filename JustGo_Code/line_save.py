from db_actions import *
import datetime

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

def passenger(line_id, mydict):
    mydict[line_id]["call"]["passenger"] = 0
    mydict[line_id]["call"]["finalcheckpassenger"] = 0
    mydict[line_id]['call']['checkmoney'] = 0
    
