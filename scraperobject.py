"""
BunnB 2k17
Happy new year nerds HEHheHEheHhEhE

"""

import json
from sortedcollections import OrderedDict
from stringfixer import stringfix

class SwatScraper():
    def __init__(self, string):
        """
        contains master string and current "reading" string
        contains keywords to identify Locations, Days, and Times
        """
        self.string = string
        self.curr = None
        self.locations = ['Clothier','Black Cultural Center','Kohlberg','No Location','Lang Music Buiding','Lang Performing Arts Center','McCabe Library','Parrish','Matchbox','Lamb-Miller Fieldhouse','Trotter','Science Center']
        self.days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday',]
        self.times = ['AM','PM','All Day']
        self.events = []
        
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
        __id = 0
        while len(self.string) > 0:
            self.readline()
            if self.checkLoc(self.curr) == True:
                location = self.curr
            elif self.checkDay(self.curr) == True:
                day = self.curr
            elif self.checkTime(self.curr) == True:
                if "Application Deadline" in self.curr:
                    pass
                else:
                    print self.curr
                    time_name = stringfix(self.curr)
                    event = OrderedDict([("id",__id), ("name",time_name[2]), ("start_time",time_name[0]), ("end_time",time_name[1]), ("location",location), ("lat",37.5), ("lng",75), ("description",day)])
                    self.events.append(event)
                    __id += 1
            else:
                pass
        self.events = json.dumps(self.events, indent = 4)
        return self.events  
            
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