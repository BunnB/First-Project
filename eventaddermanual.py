from firebase import *
from fixers import *
from datetime import *
from dateutil.relativedelta import *
from locDic import locDic

firebase = firebase.FirebaseApplication('https://swatevents-2341b.firebaseio.com/',None)

def adder():
    branch = "approved"
    date = raw_input("Date MM-DD-YYYY:")
    description = "Test"#raw_input("Desc:")
    loc = "Clothier"#raw_input("Location:")
    name = "Test Event"#raw_input("Name:")
    starttime = "7:30 AM"#raw_input("starttime 7:30 AM:")
    endtime = "10:30 PM"#raw_input("endtime 8:40 PM:")
    rank = timesort(starttime)
    event = {"sorted_time": rank, "name":name, "start_time":starttime, "end_time":endtime, "location":loc, "lat":locDic[loc][0], "lng":locDic[loc][1], "date":date, "description":description, "count": 0, "id": idfixer(date,name)}
    firebase.post("/{}".format(branch),event)

def launchadder():
    while True:
        adder()

if __name__ == "__main__":
    adder()
