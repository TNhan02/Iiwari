import json
import pandas as pd
import pyodbc as sql

def module_info(mod):
   print(mod+" module  missing")
   print("pip3 install "+mod)
   exit(-1)

try:
   import websocket
except:
   module_info("websocket-client")

try:
   import requests
except:
   module_info("requests")

def on_message(ws, message):
   d = json.loads(message)
   print(d)

   if("x" in d):
      import_csv_to_sql(d)
   else:
      print("Key doesn't exist in JSON data")

def sql_connection():
   connection = sql.connect('Driver={SQL Server};'
                      'Server=10.211.48.5;'
                      'Database=indoor_positioning;'
                      'UID=sa;'
                      'PWD=testPass_123_XX')
   cursor = connection.cursor()

   print("SQL server is connected")
   return cursor

def import_csv_to_sql(content):
   db = sql_connection()
   db.execute("INSERT INTO position(ts, node, x, y, z, q, alg) VALUES (?,?,?,?,?,?,?)",
             content['ts'], content['node'], content['x'], content['y'], content['z'], content['q'], content['alg'])
   db.commit()
   print("CSV file is imported successfully!")                 

def on_error(ws, error):
   print(error)

def on_close(ws, close_status_code, close_msg):
   print("### closed ###")

def on_open(ws):
   print("### opened ###")

def login(email,pw):
   H = {'Content-type': 'application/json', 'Accept': 'text/plain'}
   url="https://dash.iiwari.cloud/api/v1/users/login"
   L={ "Email" : email , "Password" : pw }
   r = requests.post(url,json=L,headers=H)
   print("Login success!")
   return r

if __name__ == "__main__":
   
   email ="savonia"
   pw    ="mAhti5aar1"
   site  ="017bcaaf-a074-f5fc-0b1e-083f26226deb" #savonia AMK

   r=login(email,pw)

   token = r.json()

   query="wss://dash.iiwari.cloud/api/v1/sites/"+site+"/locations/stream?token="+token['token']
   cookies="; ".join(["%s=%s" %(i, j) for i, j in r.cookies.items()])

   wss = websocket.WebSocketApp( query,
                                 on_open=on_open,
                                 on_message=on_message,
                                 on_error=on_error,
                                 on_close=on_close,
                                 cookie=cookies)

   wss.run_forever()
