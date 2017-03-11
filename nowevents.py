"""
timenow;
checks to see if time if current time is
"""
#get current events going on today
#grab start and end time, -> grab their ranks
#grab now time -> convert to rank
# if now time rank > start , and, now time rank < end
#if they are add their ids to curr_events

#ALL DAY IS STILL BEING ADDED EVEN THOUGH ITS ALREADY IN THERE

from firebase import *
from fixers import *
from datetime import *
firebase = firebase.FirebaseApplication('*********************',None)
def eventsNow():
    branch = "now"
    now = datetime.today()
    now = [now.hour,now.minute]
    now = checktwelve(now)
    branch0 = firebase.get('/events/day0',None)
    branchnow = firebase.get('/events/now',None)
    curr_events = []
    end_list = []
    try:
        for id_key,event in branchnow.items(): #loops through list of now events
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
            if start == 0 and end == start: #If all day event, pass
                pass
            elif comp < start or comp > end: #if event hasnt happened or hasnt ended
                firebase.delete("/events/now/"+id_key.encode("utf-8"),None) #delete event from now
            clone[key] = val
            curr_events.append(clone["id"]) #Adds to curr events to make sure no clones are added
    except:
        pass
    print curr_events

    for id0_key,event in branch0.items(): #loops through list of branch0
        child_event = {}
        for key,val in event.items():
            key = key.encode("utf-8")
            try:
                val = val.encode("utf-8")
            except:
                pass
            child_event[key] = val
        try:
            start = child_event["sorted_time"]
        except:
            print("ERROR: SORTED TIME NOT FOUND")
        end = timesort(child_event["end_time"])
        comp = timesort(now)
        if start == 0 and end == 0: #if event is allday
            if child_event["id"] in curr_events:
                pass
            else:
                firebase.post('/events/{}'.format(branch),child_event)
        elif comp < end and comp > start: #if event is happening now
            if child_event["id"] in curr_events:
                pass
            else:
                pass
                firebase.post('/events/{}'.format(branch),child_event)
        elif comp > end and comp > start: #if event ended
            firebase.delete("/events/day0/{}".format(id0_key),None) #delete event from branch0
        else:
            pass

def checktwelve(now):
    """
    now is [hour,minute]
    """
    print now
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
