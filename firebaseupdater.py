"""
moves day1 -> day0
moves day2 -> day1 so scraper can scrape day3
Added: duplicate checker
"""

from firebase import *
from fixers import *

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
            curr_events.append(child_event["id"]) #Adds to curr events to make sure no clones are added
            if curr_events.count(child_event["id"]) > 1:
                pass
            else:
                addbranch = getbranch(child_event["date"])
                if addbranch == "passed": #if event is passed
                    pass
                else:
                    firebase.post('/events/{}'.format(addbranch),child_event) #moves day2 -> day1
    return curr_events

def approvedupdate(firebase):
    branches = ["day0","day1","day2"]
    alist = firebase.get('/approved',None)
    for id_key,event in alist.items():
        for key,val in event.items():
            key = key.encode("utf-8")
            if key == "date":
                branch = getbranch(val)
                if branch in branches:
                    firebase.post('/events/{}'.format(branch),event)
                    firebase.delete('/approved/{}'.format(id_key),None)
                else:
                    pass

    #look at approved events.
    #if event is within day range, add the event to the specific day, and move the approved event into branch

if __name__ == "__main__":
    firebase = firebase.FirebaseApplication('*******************',None)
    firebaseupdate(firebase)
