"""
timenow;
checks to see if time if current time is
"""
#get current events going on today
#grab start and end time, -> grab their ranks
#grab now time -> convert to rank
# if now time rank > start , and, now time rank < end
#if they are add them to curr_events

from firebase import *
from fixers import timesort
from datetime import *
firebase = firebase.FirebaseApplication('https://mapapp-2a84b.firebaseio.com/',None)
def eventsNow():
    branch = "now"
    now = datetime.today()
    now = [now.hour,now.minute]
    now = checktwelve(now)
    branch0 = firebase.get('/events/day0',None)
    branchnow = firebase.get('/events/now',None)
    curr_events = []
    for id_key,event in branchnow.items():
        clone = {}
        for key,val in event.items():
            key = key.encode("utf-8")
            try:
                val = val.encode("utf-8")
            except:
                pass
            clone[key] = val
        start = clone["sorted_time"]
        end = timesort(clone["end_time"])
        comp = timesort(now)
        if start == 0 and end == start:
            firebase.delete("/events/now/"+id_key.encode("utf-8"),None)
        if comp < start or comp > end:
            firebase.delete("/events/now/"+id_key.encode("utf-8"),None)
        clone[key] = val
        curr_events.append(clone) #Adds to curr events to make sure no clones are added
    for id_key,event in branch0.items():
        child_event = {}
        for key,val in event.items():
            key = key.encode("utf-8")
            try:
                val = val.encode("utf-8")
            except:
                pass
            child_event[key] = val
        start = child_event["sorted_time"]
        end = timesort(child_event["end_time"])
        comp = timesort(now)
        if start == 0 and end == 0:
            if child_event in curr_events:
                pass
            else:
                firebase.post('/events/{}'.format(branch),child_event) #moves day1 -> day0
        elif comp < end and comp > start:
            if child_event in curr_events:
                pass
            else:
                firebase.post('/events/{}'.format(branch),child_event) #moves day1 -> day0
        else:
            pass

def checktwelve(now):
    now[1] = str(now[1])
    if now[0] > 12:
        if len(now[1]) == 1:
            now[1] = "0" + now[1]
        now[0] -= 12
        now.append(" PM")
        return str(now[0])+":"+now[1]+now[2]
    else:
        if len(now[1]) == 1:
            now[1] = "0" + now[1]
        now.append(" AM")
        return str(now[0])+":"+now[1]+now[2]

if __name__ == "__main__":
        eventsNow()
