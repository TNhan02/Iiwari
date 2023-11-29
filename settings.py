import botVector

def init():
    global person_location, is_button_pressed
    is_button_pressed = False
    person_location = botVector.Point()
    #buffer_event = []