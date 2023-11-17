import json
import pyodbc as sql

buffer = [] # buffer for adding data rows to SQL server
count = 0 # count for adding data rows to SQL server
robot_tag = "0d47-3234-0474-81b9"
person_tag = "0d47-3234-0474-848b" # could be changed since this one doesn't work at all at 17.11.2023
url = "wss://dash.iiwari.cloud/api/v1/sites/017bcaaf-a074-f5fc-0b1e-083f26226deb"

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

def on_message(path, message):
   global buffer, count
   if(path == "locations/stream"):
      d = json.loads(message) # parse json data
      print(d)

      if("x" in d):
         buffer.append(d)
         count += 1

         if(count == 5):
            import_to_sql(buffer)
            print("{} new rows of data is inserted successfully".format(count))

         # reset buffer after each 5 rows
         buffer = []
         count = 0
      else:
         print("Key doesn't exist in JSON data")
   elif(path == "events/stream"):
      d = json.loads(message) # parse json data
      print("Button is pressed "+d)

      # type 10 = button press
      if(("type" in d) and (d['type'] == 10)):
         return True
      return False


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

def streaming(token):
   query = url + "/locations/stream?token=" + token['token']
   cookies="; ".join(["%s=%s" %(i, j) for i, j in r.cookies.items()])

   wss = websocket.WebSocketApp( query,
                                 on_open = on_open,
                                 on_message = on_message,
                                 on_error = on_error,
                                 on_close = on_close,
                                 cookie = cookies)

   wss.run_forever()

def button_pressed(site, token):
   query = url + "/events/stream?token=" + token['token']
   cookies="; ".join(["%s=%s" %(i, j) for i, j in r.cookies.items()])

   wss = websocket.WebSocketApp( query,
                                 on_open = on_open,
                                 on_message = on_message,
                                 on_error = on_error,
                                 on_close = on_close,
                                 cookie = cookies)
   
   wss.run_forever()

if __name__ == "__main__":
   
   email ="savonia"
   pw    ="mAhti5aar1"
   site  ="017bcaaf-a074-f5fc-0b1e-083f26226deb" #savonia AMK

   r=login(email,pw)
   token = r.json()

   streaming(site, token)
   button_pressed(site, token)
