import json
import settings # initiate global variables
import botVector
from event_stream import *

url = "wss://dash.iiwari.cloud/api/v1/sites/017bcaaf-a074-f5fc-0b1e-083f26226deb/"
email =""
pw    ="" #add password
person_tag = "0d47-3234-0474-59a9" # change the 10-Hz tag here

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
      person_location = botVector.Point(settings.exponential_filter(d["x"], 'x'), settings.exponential_filter(d["y"], 'y'))
      settings.collector.addPersonLocation(person_location)
      print("{}".format(settings.collector.getPersonLocation()))
   else:
      print("Person doesn't move")    

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