"""
duplicates checker
v0.01
"""
from fixers import timesort
from firebase import *
#grabs firebase
#check name similarity
#check time similarity
#if time not same = notsame event
#elif name same enough, = same event
#else not same event
#remove same event

def dupecheck(event,eventlist):
    if len(eventlist) == 0:
        return False
    for thing in eventlist:
        if timecheck(event,thing) == False:
            return False
        elif namecheck(event,thing) == True:
            return True
        else:
            return False

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
    firebase = firebase.FirebaseApplication('https://mapapp-2a84b.firebaseio.com/',None)
    thing = {"Hello":"sucker"}
    test = "test"
    firebase.post('events/test/',thing)
