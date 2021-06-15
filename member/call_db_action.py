# -*- coding: utf-8 -*-
import db_connect as db  # Connect to db

# 經由button按下傳來的msg(註冊)及line_id，判斷此使用者是否註冊過。
'''
已註冊(True)--->linebot進行更名流程(背後運行依然是註冊流程)
未註冊(False)--->linebot直接進行註冊流程
'''
# read member data from database
def read_from_member(line_id):
    conn = db.database_connect()
    cursor = conn.cursor()
    
    sql =f"""SELECT * FROM member WHERE student_id is NOT NULL AND line_id = %s"""
    cursor.execute(sql, (line_id,))
    register_or_not = cursor.fetchall()
    if register_or_not != []:
        # 已註冊
        return True
    else:
        # 未註冊
        return False
    
    cursor.close()
    conn.close()

# write member data to database
def write_to_member(member):
    conn = db.database_connect()
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
    conn = db.database_connect()
    cursor = conn.cursor()
    
#     # SQL-1
#     sql =f"""SELECT credit_index FROM member WHERE student_id is NOT NULL AND line_id = %s"""
#     cursor.execute(sql, (line_id,))
    # SQL-2
    sql =f"""SELECT credit_index FROM member WHERE student_id is NOT NULL AND line_id = '{line_id}';"""
    cursor.execute(sql)
    
    credit_index = cursor.fetchall()
    credit_score = [i[0] for i in credit_index][0]
    cursor.close()
    conn.close()
    return credit_score

# update member data to database
def update_member_info(update_member):
    conn = db.database_connect()
    cursor = conn.cursor()

    update_mb = update_member
    sql = f"""UPDATE member SET student_id = %s, name = %s, depart = %s, sex = %s, password = %s where line_id = %s;"""
    cursor.execute(sql, (update_mb[0], update_mb[2], update_mb[3], update_mb[4], update_mb[5], update_mb[1]))
    conn.commit()
    
    cursor.close()
    conn.close()

# read member student_id from database
def get_sid_link(line_id):
    conn = db.database_connect()
    cursor = conn.cursor()

    sql = f"""SELECT student_id FROM member WHERE student_id is NOT NULL AND line_id = '{line_id}';"""
    cursor.execute(sql)

    student_id = cursor.fetchall()
    sid = [i[0] for i in student_id][0]

    link = '?'+'name ='+ sid
    cursor.close()
    conn.close()
    return link
