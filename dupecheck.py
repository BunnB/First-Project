"""
duplicates checker
v0.11
"""
#FIX DUPE
from fixers import timesort
from firebase import *

def dupecheck(event,currlist):
    if len(currlist) == 0:
        return False
    for thing in currlist:
        if event["id"] in currlist:
            return True
        else:
            return False

"""
UNUSED BUT STILL KEPT
"""
def timecheck(event,thing):
    print event
    e_start = event[start_time]
    t_start = thing[start_time]
    e_end = event[end_time]
    t_end = thing[end_name]
    if e_start == t_start and e_end == e_start:
        return True
    else:
        return False

def namecheck(event,thing):
    e_name = event[name]
    t_name = thing[name]
    if e_name == t_name:
        return True
    else:
        return False



if __name__ == "__main__":
    firebase = firebase.FirebaseApplication('**************',None)
    thing = {"Hello":"sucker"}
    test = "test"
    firebase.post('events/test/',thing)
