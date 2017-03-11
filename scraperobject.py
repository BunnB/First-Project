"""
BunnB 2k17
Happy new year nerds HEHheHEheHhEhE


"""
#LPAC List gall = List gall

import json
from sortedcollections import OrderedDict
from fixers import *
from firebase import *
from firebaseupdater import *
from locDic import locDic
from dupecheck import *

firebase = firebase.FirebaseApplication('******************',None)

"""
PRE-SCRAPE PROTOCOL
"""

try:
    curr_events = firebaseupdate(firebase) #if crash or bug, delete day branches and rerun
except:
    curr_events = []
try:
    approvedupdate(firebase)
except:
    pass

class SwatScraper():
    def __init__(self, string):
        """
        contains master string and current "reading" string
        contains keywords to identify Locations, Days, and Times
        """
        self.string = string
        self.curr = None
        self.locations = ['Clothier','Bond Complex','Black Cultural Center','Kohlberg','No Location','Lang Music Building','Lang Performing Arts Center','McCabe Library','Friends Meeting House','Parrish','Matchbox','Lamb-Miller Fieldhouse','Trotters','Science Center','Alice Paul','Lang Center']
        self.days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        self.times = ['AM','PM','All Day']
        self.events = curr_events
        self.currloc = "" #Hotfix

    def checkTime(self,line):
        for time in self.times:
            if time in line:
                return True
            else:
                pass
        return False

    def checkLoc(self,line):
        for loc in self.locations:
            if loc in line:
                self.currloc = loc
                return True
            else:
                pass
        return False

    def checkDay(self,line):
        for day in self.days:
            if day in line:
                return True
            else:
                pass
        return False

    def findEvents(self):
        """
        grabs events
        """
        while len(self.string) > 0:
            self.readline()
            print self.curr
            if self.checkLoc(self.curr) == True:
                loc = self.currloc
                location = self.curr
            elif self.checkDay(self.curr) == True:
                try:
                    masterday = dateformat(self.curr) #Returns formatted date and Day queue (Day1,Day2,Day3)
                    day = masterday[0] #date
                    child = masterday[1] #queue
                except:
                    pass
            elif self.checkTime(self.curr) == True:
                if "Application Deadline" in self.curr:
                    pass
                else:
                    time_name = stringfix(self.curr) #Returns list of start/end time and name from time string
                    if len(time_name) == 3:
                        try:
                            event = {"sorted_time": time_name[2], "name":time_name[1], "start_time":time_name[0], "end_time":" ", "location":location, "lat":locDic[loc][0], "lng":locDic[loc][1], "date":day, "description":"", "count": 0, "id": idfixer(day,time_name[1])}
                        except:
                            event = {"sorted_time": time_name[2], "name":time_name[1], "start_time":time_name[0], "end_time":" ", "location":"No Location", "lat":locDic["No Location"][0], "lng":locDic["No Location"][1], "date":day, "description":"", "count": 0, "id": idfixer(day,time_name[1])}
                        #elike = {idfixer(day,time_name[1]):0}
                        #firebase.post("/likes/", elike)
                        if dupecheck(event,curr_events) == False:
                            firebase.post("/events/" + child,event)
                        else:
                            pass
                    else:
                        try:
                            event = {"sorted_time": time_name[3], "name":time_name[2], "start_time":time_name[0], "end_time":time_name[1], "location":location, "lat":locDic[loc][0], "lng":locDic[loc][1], "date":day, "description":"", "count": 0, "id": idfixer(day,time_name[2])}
                        except:
                            event = {"sorted_time": time_name[2], "name":time_name[1], "start_time":time_name[0], "end_time":" ", "location":"No Location", "lat":locDic["No Location"][0], "lng":locDic["No Location"][1], "date":day, "description":"", "count": 0, "id": idfixer(day,time_name[1])}
                        #elike = {idfixer(day,time_name[2]):0}
                        #firebase.post("/likes/", elike)
                        if dupecheck(event,curr_events) == False:
                            firebase.post("/events/" + child,event)
                        else:
                            pass
            else:
                pass

    def readline(self):
        """
        reads a line from string
        upates current "read" string
        makes master string shorter
        """
        newstring = ''
        substring = ''
        for x in self.string:
            if x!= '\n':
                substring += x
            else:
                index = len(substring) + 1 ## +1 takes into account newline char
                newstring = self.string[index::]
                break
        self.string = newstring
        self.curr = substring


if __name__ == "__main__":
    string ="""Clothier - (Tarble-in-Clothier All-Campus Space)

Start Date and TimeEvent Details

Wednesday, December 07, 2016

4:30 PM - 5:30 PM Collection - a Celebration of Light

Kohlberg - (Kohlberg 228)

Start Date and TimeEvent Details

Tuesday, December 06, 2016

All Day Law as a Tool for Social Justice and Conflict Resolution"""
    myscraper = SwatScraper(string)
    myscraper.findEvents()
    print(myscraper.events)
