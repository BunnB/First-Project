"""
Should sep curr list generator and adder.
"""

from firebase import *

def firebaseupdate(firebase):
    curr_events = []
    branch0 = firebase.get('/events/day0',None)
    branch1 = firebase.get('/events/day1',None)  #Grabs branches
    branch2 = firebase.get('/events/day2',None)
    firebase.delete('/events/day0', None)
    firebase.delete('/events/day1', None) #delete branches
    firebase.delete('/events/day2', None)
    branches = [branch0,branch1,branch2]
    for branch in branches:
        for id_key,event in branch.items():
            child_event = {}
            for key,val in event.items():
                key = key.encode("utf-8")
                try:
                    val = val.encode("utf-8")
                except:
                    pass
                child_event[key] = val
            if branch == branches[1]:
                firebase.post('/events/day0',child_event) #moves day1 -> day0
            elif branch == branches[2]:
                 firebase.post('/events/day1',child_event) #moves day2 -> day1
            curr_events.append(child_event) #Adds to curr events to make sure no clones are added
    return curr_events
