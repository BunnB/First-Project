from firebase import *
from fixers import *
from datetime import *
from dateutil.relativedelta import *
from locDic import locDic

firebase = firebase.FirebaseApplication('***********************',None)

def adder():
    branch = "approved"
    date = raw_input("Date MM-DD-YYYY:")
    description = raw_input("Desc:")
    loc = raw_input("Location:")
    name = raw_input("Name:")
    starttime = raw_input("starttime 7:30 AM:")
    endtime = raw_input("endtime 8:40 PM:")
    rank = timesort(starttime)
    event = {"sorted_time": rank, "name":name, "start_time":starttime, "end_time":endtime, "location":loc, "lat":locDic[loc][0], "lng":locDic[loc][1], "date":date, "description":description, "count": 0, "id": idfixer(date,name)}
    firebase.post("/{}".format(branch),event)

def launchadder():
    while True:
        adder()

if __name__ == "__main__":
    adder()
