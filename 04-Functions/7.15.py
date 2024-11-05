#A device in a door registers people entering and leaving a room.
#The + sign means a person entering a room and the -- sign a person leaving a room.
#Define the function f(detector) that returns True if at least 3 people were in the room at the same time, or False otherwise.
#Sample result:
def f(detector):
    people = 0
    for action in detector:
        if action == '+':
            people += 1
        elif action == '--':
            people -= 1

        if people >= 3:
            return True
    return False

detector = ['+', '+', '+', '+', '--'] 
print(f(detector))  # Output: True