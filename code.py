from flask import Flask, request, jsonify
import sqlite3
con = sqlite3.connect("sample.db")
cur = con.cursor()
cur.execute("CREATE TABLE if not exists user (user_id TEXT, password TEXT)")
con.commit()
con.close()

app = Flask(__name__)


@app.route ( '/' )
def car():
    return "I am speed lightning Mcqueen Kachhoowwww"

@app.route('/register',methods=['POST'])
def register():
  data = request.get_json()
  con = sqlite3.connect("sample.db")
  cur = con.cursor()
  cur.execute("INSERT INTO user VALUES('{}','{}')".format(data['user_id'], data['password']))
  con.commit()
  con.close()
  print(data)

  return "Logged in successfully"

@app.route ("/showall")
def showall():
  con = sqlite3.connect("sample.db")
  cur = con.cursor()
  data = cur.execute("SELECT * from user")
  data = cur.fetchall()
  con.commit()
  con.close()
  return dict(data)

@app.route ('/login', methods=['POST'])
def login():
  data = request.get_json()
  con= sqlite3.connect("sample.db")
  cur = con.cursor()
  data = cur.execute("SELECT * from user where user_id = '{}'".format(data['user_id']))
  data = cur.fetchall()
  con.commit()
  con.close()
  if len(data) > 0:
    return " Login done "
  else:
    return "Error"

@app.route ('/update', methods=['POST'])
def update():
  data = request.get_json()
  con = sqlite3.connect("sample.db")
  cur = con.cursor()
  data = cur.execute("UPDATE user set password = '{}' where user_id = '{}'".format(data['user_id'], data['password']))
  data = cur.fetchall()
  con.commit()
  con.close()
  return "Done"

@app.route ('/delete', methods=['POST'])
def delete():
 data = request.get_json()
 con = sqlite3.connect("sample.db")
 cur = con.cursor()
 data = cur.execute("DELETE from user where user_id = '{}'".format(data['user_id']))
 data = cur.fetchall()
 con.commit()
 con.close()
 return "Deleted Successfully"

app.run(port = 5000)