import botVector

def init():
    # person_location is the global Point variable that robot needs to keep track of when on duty
    # person_location is the location of a person when button is pressed 
    global person_location, is_button_pressed
    is_button_pressed = False
    person_location = botVector.Point()
    #buffer_event = []