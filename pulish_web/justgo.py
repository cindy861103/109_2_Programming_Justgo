##from flask import Flask
import psycopg2 as ps

#connect heroku postgresql
conn = ps.connect(host="ec2-3-218-71-191.compute-1.amazonaws.com",
                  user="pauvcxweyckeaf",
                  password="115d8ec87368c3b65453a2d2988a7cbfd8bcb7db61f75afbd35b4519b152e3f7",
                  database="d5251933te7fta",
                  port="5432")

if conn is not None:
    cursor = conn.cursor()
    conn.commit()  # commit the changes

##from flask import render_template
def get_name(uu):
    return 
@app.route("/")
def home():
    return render_template("justgoexample.html",name=uu)
app.run()
