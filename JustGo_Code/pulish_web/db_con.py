import psycopg2 as ps

def database_connect():
    #connect heroku postgresql
    conn = ps.connect(host="ec2-3-218-71-191.compute-1.amazonaws.com",
                      user="pauvcxweyckeaf",
                      password="115d8ec87368c3b65453a2d2988a7cbfd8bcb7db61f75afbd35b4519b152e3f7",
                      database="d5251933te7fta",
                      port="5432")
    return conn
