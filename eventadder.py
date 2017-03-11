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
from nowevents import checktwelve
#write approved events into excel file
#id serializer for events
#id for event so we can do cloning check/dupecheck/nowevents updaterby
#we only add events in scraper object, and nowevents

def launchGUI():
    fireref = firebase.FirebaseApplication('https://swatevents-2341b.firebaseio.com/',None)
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
            for loc, cordin in locDic.items():
                if loc in key:
                    clone["lat"] = locDic[loc][0]
                    clone["lng"] = locDic[loc][1]
                else:
                    clone["lat"] = 39.907261
                    clone["lng"] = -75.355670
        clone["id"] = idfixer(clone["date"],clone["name"])
        clone["sorted_time"] = miltimefixer(clone["start_time"])
        clone["count"] = 0
        stime = clone["start_time"].split(":") ##MIL TO CHANGES TO AM/PM FORMAT
        stime.pop()
        for i in range(len(stime)-1): #time format is mili
            stime[i] = int(stime[i])
        etime = clone["end_time"].split(":")
        etime.pop()
        for i in range(len(etime)-1):
            etime[i] = int(etime[i])
        clone["start_time"] = checktwelve(stime)
        clone["end_time"] = checktwelve(etime)
        ret = approve(clone)
        if ret == True:
            fireref.post('/approved',clone)
            fireref.delete('/forms/{}'.format(id_key),None)
            writexl(clone)
        else:
            fireref.post('/not-approved',clone)
            fireref.delete('/forms/{}'.format(id_key),None)


def approve(event):
    for key, value in event.items():
        print("{}:{}".format(key,value))
    yn = raw_input("Approve? (y/n):")
    if yn == "y":
        return True
    else:
        return False

def writexl(event):
    try:
        wb = load_workbook(filename = 'swag.xlsx')
    except:
        wb = Workbook()
    ws = wb.active
    submit = [event["date"],event["name"],event["description"],event["start_time"],event["end_time"],event["location"]]
    ws.append(submit)
    wb.save('swag.xlsx')
    pass

if __name__ == "__main__":
    launchGUI()
    """
    eyed = idfixer("02-11-2017","E,A,T Presents: Sweet Escape (from the Awkwardness)")
    print(eyed)
    eyed = idfixer("02-13-2017","US in STEM meeting")
    print(eyed)
    """
