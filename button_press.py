import json
from location_tracking import *
from botVector import *
import threading

global is_button_pressed
buffer_event = []
alpha = 0.5 # alpha value for exponential filter
filtered_value = None

url = "wss://dash.iiwari.cloud/api/v1/sites/017bcaaf-a074-f5fc-0b1e-083f26226deb/"
email = "savonia"
pw    = "mAhti5aar1"
site  = "017bcaaf-a074-f5fc-0b1e-083f26226deb" #savonia AMK

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
   def run(*args):
      global is_button_pressed, buffer_event
      d = json.loads(message)
   
      if("type" in d and d["type"] == 10):
         print(d)
         buffer_event.append(d)
         is_button_pressed = True
   threading.Thread(target=run).start()

def on_error(ws, error):
   print(error)

def on_close(ws, close_status_code, close_msg):
   print("### event streaming closed ###")

def on_open(ws):
   print("### event streaming opened ###")

def event_streaming():
   r = login(email, pw)
   token = r.json()

   query = url + "events/stream?token=" + token['token']
   cookies="; ".join(["%s=%s" %(i, j) for i, j in r.cookies.items()])

   wss = websocket.WebSocketApp( query,
                                 on_open = on_open,
                                 on_message = on_message,
                                 on_error = on_error,
                                 on_close = on_close,
                                 cookie = cookies)

   wss.run_forever()

if __name__ == "__main__":
   event_streaming()