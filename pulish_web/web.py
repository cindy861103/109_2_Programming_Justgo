from db_action import *
from web import *
def title(f):
    f.write('''    <center><table border="0" width="800" style="border:0px #005AB5;">
    <tr>
    <td valign="top">
         
        <table border="0" width="800" style="border:0px #005AB5;">
            <tr>
                <td align="center"><span style="font-family:cwTeXYen";><span style="font-size:50px;"><font color="#FFFFFF"><u>確定發車(已訂車)</font></u></h1></span></td>
            </tr>
        </table>
 ''')
def title2(f):
    f.write('''    <center><table border="0" width="800" style="border:0px #005AB5;">
    <tr>
    <td valign="top">
         
        <table border="0" width="800" style="border:0px #005AB5;">
            <tr>
                <td align="center"><span style="font-family:cwTeXYen";><span style="font-size:50px;"><font color="#FFFFFF"><u>人數達標後發車(尚未訂車)</font></u></h1></span></td>
            </tr>
        </table>
 ''')

def title3(f):
    f.write('''    <center><table border="0" width="800" style="border:0px #005AB5;">
    <tr>
    <td valign="top">
         
        <table border="0" width="800" style="border:0px #005AB5;">
            <tr>
                <td align="center"><span style="font-family:cwTeXYen";><span style="font-size:50px;"><font color="#FFFFFF"><u>歷史紀錄</font></u></h1></span></td>
            </tr>
        </table>
 ''')

def big_form(f,left):
    if left:
        
        f.write('''    <table border="0" width="800" style="border:0px #005AB5;">
            <tr>
        ''')
    else:
        f.write('    </td>\n')
        
    f.write('<td width="400" height="300" align="center">\n')
    

def small_form(f,left,form,member,publish2):
    max_min=str(get_max_min(form[0]))
    f.write('''
            <table style="border:3px #005AB5 solid;" cellpadding="10" border='1' align="center">
              <tr>
                <th bgcolor="#DBABFF">編號</th>
                <td bgcolor="#66B3FF" align="center" width=230px;><span style="font-family:Comic Sans MS;">'''+form[0]+'''</span></td>
              </tr>
              <tr>
                <th bgcolor="#DBABFF">出發時間</th>
                <td align="center" bgcolor="#66B3FF"><span style="font-family:Comic Sans MS;">'''+form[2][0]+'''：'''+form[2][1]+'''</span></td>
              </tr>
              <tr>
                <th bgcolor="#DBABFF">發起人/性別</th>
                <td align="center" bgcolor="#66B3FF"><span style="font-family: 'Noto Sans TC', sans-serif;">'''+member[2][0]+'''同學/'''+member[0]+'''</span></td>
              </tr>
              <tr>
                <th bgcolor="#DBABFF">出發地</th>
                <td align="center" bgcolor="#66B3FF"><span style="font-family: 'Noto Sans TC', sans-serif;">'''+publish2[0]+'''</span></td>
              </tr>
              <tr>
                <th bgcolor="#DBABFF">目的地</th>
                <td align="center" bgcolor="#66B3FF"><span style="font-family: 'Noto Sans TC', sans-serif;">'''+publish2[1]+'''</span></td>
              </tr>
              <tr>
                <th bgcolor="#DBABFF">上限人數</th>
                <td align="center" bgcolor="#66B3FF"><span style="font-family:Comic Sans MS;">'''+max_min[1]+'''</span></td>
              </tr>
              <tr>
                <th bgcolor="#DBABFF">發起人信用積分</th>
                <td align="center" bgcolor="#66B3FF"><span style="font-family:Comic Sans MS;">'''+str(member[1])+'''</span></td>
              </tr>
              <tr>
                <th bgcolor="#DBABFF">備註</th>
                <td align="center" bgcolor="#66B3FF"><span style="font-family: 'Noto Sans TC', sans-serif;">'''+form[1]+'''</span></td>
              </tr>
            </table>''')
    if left:
        left=False
    else:
        left=True
        f.write('''
        </td>
    </tr>
</table>
</td>
</tr>
</table>
</td>
</tr>
</table>
</center>''')
    return left
        
def historyform(f,left,history):
    f.write('''
<table style="border:3px #005AB5 solid;" cellpadding="10" border='1' align="center">
  <tr>
    <th bgcolor="#DBABFF">編號</th>
    <td bgcolor="#66B3FF" align="center" width=230px;><span style="font-family:Comic Sans MS;">'''+history[0]+'''</span></td>
  </tr>
  <tr>
    <th bgcolor="#DBABFF">車行</th>
    <td align="center" bgcolor="#66B3FF"><span style="font-family:Comic Sans MS;">'''+history[1]+'''</span></td>
  </tr>
  <tr>
    <th bgcolor="#DBABFF">車牌號碼</th>
    <td align="center" bgcolor="#66B3FF"><span style="font-family:Comic Sans MS;">'''+history[2]+'''</span></td>
  </tr>
  <tr>
    <th bgcolor="#DBABFF">上車地</th>
    <td align="center" bgcolor="#66B3FF"><span style="font-family: 'Noto Sans TC', sans-serif;">'''+history[3]+'''</span></td>
  </tr>
  <tr>
    <th bgcolor="#DBABFF">目的地</th>
    <td align="center" bgcolor="#66B3FF"><span style="font-family: 'Noto Sans TC', sans-serif;">'''+history[4]+'''</span></td>
  </tr>
  <tr>
    <th bgcolor="#DBABFF">行程總價</th>
    <td align="center" bgcolor="#66B3FF"><span style="font-family: 'Noto Sans TC', sans-serif;">'''+str(history[5])+'''</span></td>
  </tr>
</table><!--左邊?'''+str(left)+'''-->''')      
    if left:
        left=False
    else:
        left=True
        f.write('''
        </td>
    </tr>
</table>
</td>
</tr>
</table>
</td>
</tr>
</table>
</center>''')
        return left
        
