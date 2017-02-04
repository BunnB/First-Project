"""
event approval GUI
+
excel writer
"""
from firebase import *
from locDic import locDic
from fixers import *
import json
from openpyxl import *
#write approved events into excel file
#id serializer for events
#id for event so we can do cloning check/dupecheck/nowevents updaterby

def launchGUI():
    fireref = firebase.FirebaseApplication('https://mapapp-2a84b.firebaseio.com/',None)
    forms = fireref.get('/forms',None)
    for id_key,event in forms.items(): #loops through list of now events
        clone = {}
        for key,val in event.items():
            key = key.encode("utf-8")
            try:
                val = val.encode("utf-8")
            except:
                pass
            clone[key] = val
        clone["sorted_time"] = timesort(clone["start_time"])
        clone["message"] = " people are attending"
        clone["count"] = 0
        ltlng = locDic[clone["loc"]]
        clone["lat"] = ltlng[0]
        clone["lng"] = ltlng[1]
        ret = approve(clone)
        if ret == True:
            firebase.post('/approved',clone)
            firebase.delete('')
            writexl(clone)
        else:
            firebase.post('/not-approved',clone)


def approve(event):
    print event
    yn = raw_input("Approve? (y/n):")
    if yn == "y":
        return True
    else:
        return False

def writexl():
    wb = Workbook()
    ws = wb.active
    wb.save('balances.xlsx')

    pass

if __name__ == "__main__":
    writexl()
