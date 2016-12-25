"""

"""

class SwatScraper():
    def __init__(self, string):
        self.string = string
        self.locations = ['Clothier','Kohlberg']
        self.days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        self.times = ['AM','PM']
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
        while len(self.string) > 0:
            line = self.readline()
            if self.checkTime(line) == True:
                event = [location,date,line]
                print(event)
            elif self.checkDay(line) == True:
                date = line
            elif self.checkLoc(line) == True:
                location = line
            else:
                pass  
            
    def readline(self): 
        """
        reads a line from string
        returns string
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
        return substring
        
        
if __name__ == "__main__":
    string ="""Clothier - (Tarble-in-Clothier All-Campus Space)

Start Date and TimeEvent Details

Wednesday, December 07, 2016

4:30 PM - 5:30 PM Collection - a Celebration of Light

Kohlberg - (Kohlberg 228)

Start Date and TimeEvent Details

Tuesday, December 06, 2016

4:30 PM - 6:00 PM Law as a Tool for Social Justice and Conflict Resolution"""
    myscraper = SwatScraper(string)
    #print(myscraper.string)
    myscraper.findEvents()
    #print(myscraper.events)
    #print(line)
    #print(string)
    #print(myscraper.string)