from web import *
from header import head
from footer import foot
from db_con import *
from db_action import *


user_id='09170109'

def web():
    if not database_connect():
        print("連線未成功 網頁未成功開啟")
    f=open('justgo.html','w',encoding='UTF-8')
    head(f)
    publish1=get_publish_D()
    sure=[]
    not_sure=[]
    for i in list(publish1):
        max_min=get_max_min(i[0])
        if max_min[0]==0:
            sure.append(i[0])
        else:
            not_sure.append(i[0])
            
    left=True
    f.write('\n<p class="flip"><font color="#FFFFFF">確定發車(已訂車)</p></font>\n<div class="panel">\n')
    if len(sure)==0:
        f.write("<span style='font-family:cwTeXYen';><font color='#FFFFFF'><h3><p>目前並無訂單<br></span>\n")
    else:
        #title(f)
        for i in range(len(sure)):
            if i%2 ==0:
                f.write('''
    <center><table border="0" width="800" style="border:0px #005AB5;">
        <tr>
            <td valign="top">\n''')
            big_form(f,left)
            member=get_member(i[3])
            publish2=get_publish_M(i[0])
            left=small_form(f,left,publish1[i],member,publish2)
            
    left=True    
    f.write('</div>\n<p class="flip2"><font color="#FFFFFF">人數達標後發車(尚未訂車)</p></font>\n<div class="panel2">\n')
    if len(not_sure)==0:
        f.write("<span style='font-family:cwTeXYen';><font color='#FFFFFF'><h3><p>目前並無訂單<br></span>\n")
    else:
        #title2(f)
        for i in range(len(not_sure)):
            if i%2 ==0:
                f.write('''
    <center><table border="0" width="800" style="border:0px #005AB5;">
        <tr>
            <td valign="top">\n''')
            big_form(f,left)
            member=get_member(publish1[i][3])
            publish2=get_publish_M(publish1[i][0])
            left=small_form(f,left,publish1[i],member,publish2)
            
    left=True
    f.write('</div>\n<p class="flip3"><font color="#FFFFFF">查看歷史紀錄</p></font>\n<div class="panel3">\n')
    historylist=get_pub_id(user_id)
    if len(historylist)==0:
        f.write("<span style='font-family:cwTeXYen';><font color='#FFFFFF'><h3><p>目前並無歷史紀錄<br></span>\n")
    else:
        #title3(f)
        for i in range(len(historylist)):
            if i%2 ==0:
                f.write('''
    <center><table border="0" width="800" style="border:0px #005AB5;">
        <tr>
            <td valign="top">\n''')
            big_form(f,left)
            history_detail=get_history(historylist[i])
            left=historyform(f,left,history_detail)
    f.write("</div>\n")
    f.close()

web()
f=open('justgo.html','a',encoding='UTF-8')
foot(f)
f.close()
