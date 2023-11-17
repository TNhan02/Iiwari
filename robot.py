#this is the 2nd python script to add robot's algorithm
import location_tracking_2023 as data_streaming
from Freenove_4WD_Smart_Car_Kit_for_Raspberry_Pi import robot

site = "017bcaaf-a074-f5fc-0b1e-083f26226deb" # savonia
token = data_streaming.login("savonia", "mAhti5aar1")

def calculate_delta_x():
    return 1

def calculate_delta_y():
    return 2
