import json
import settings # initiate global variables
import pyodbc as sql
import botVector
from event_stream import *

count = 0 # count for adding data rows to SQL server
url = "wss://dash.iiwari.cloud/api/v1/sites/017bcaaf-a074-f5fc-0b1e-083f26226deb/"
email ="savonia"
pw    ="mAhti5aar1"
person_tag = "0d47-3234-0474-8199"

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
   global count

   d = json.loads(message)

   if("x" in d and  "node" in d and d["node"] == person_tag):
      print(d)
      person_location = botVector.Point(settings.exponential_filter(d["x"]), settings.exponential_filter(d["y"]))
      settings.collector.addPersonLocation(person_location)
      print("{}".format(settings.collector.getPersonLocation()))

      #buffer.append(d)
      #count += 1

      #if(count == 5):
         #import_to_sql(buffer)
         #print("{} new rows of data inserted successfully".format(count))

         #buffer = []
         #count = 0
   else:
      print("Person doesn't move")
def sql_connection():
   connection = sql.connect('Driver={SQL Server};'
                      'Server=10.211.48.5;'
                      'Database=indoor_positioning;'
                      'UID=sa;'
                      'PWD=testPass_123_XX')
   cursor = connection.cursor()

   print("SQL server is connected")
   return cursor

def import_to_sql(list):
   db = sql_connection()
   
   # add each row in a list to server
   for content in list:
      db.execute("INSERT INTO position(ts, node, x, y, z, q, alg) VALUES (?,?,?,?,?,?,?)",
            content['ts'],
            content['node'],
            content['x'], 
            content['y'], 
            content['z'], 
            content['q'], 
            content['alg'])
   
   db.commit()       

def on_error(ws, error):
   print(error)

def on_close(ws, close_status_code, close_msg):
   print("### location streaming closed ###")

def on_open(ws):
   print("### location streaming opened ###")

def login(email,pw):
   H = {'Content-type': 'application/json', 'Accept': 'text/plain'}
   url="https://dash.iiwari.cloud/api/v1/users/login"
   L={ "Email" : email , "Password" : pw }
   r = requests.post(url,json=L,headers=H)
   print("Login success!")
   return r 

def person_streaming():
   r = login(email, pw)
   token = r.json()

   query = url + "locations/stream?token=" + token['token']
   cookies="; ".join(["%s=%s" %(i, j) for i, j in r.cookies.items()])

   wss = websocket.WebSocketApp( query,
                              on_open = on_open,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close,
                              cookie = cookies)

   wss.run_forever()


if __name__ == "__main__":
   person_streaming()