from firebase import *
from fixers import *
from datetime import *
from dateutil.relativedelta import *

firebase = firebase.FirebaseApplication('https://mapapp-2a84b.firebaseio.com/',None)
locDic = {"Clothier": (39.904258,-75.354876),
          "Bond Complex": (39.905395,-75.350844),
          "Black Cultural Center": (39.906952,-75.351481),
          "Kohlberg": (39.905830,-75.354873),
          "Lang Music Building": (39.905500,-75.356115),
          "Lang Performing Arts Center": (39.905377,-75.355310),
          "McCabe Library": (39.905361,-75.352797),
          "Friends Meeting House": (39.907342,-75.353221),
          "Parrish": (39.905188,-75.354202),
          "Matchbox": (39.901394,-75.355239),
          "Lamb-Miller Fieldhouse": (39.901279,-75.354112),
          "Trotter": (39.906415,-75.353912),
          "Science Center": (39.906859,-75.355855),
	      "No Location": (39.904321,-75.351434)}

while True:
    now = datetime.today()
    childnum = raw_input("childnum:")
    child = "day" + childnum
    if childnum == "0":
        ret = datetime.today()
        ret = "{}".format(ret.month) + "-" + "{}".format(ret.day) + "-" + "{}".format(ret.year)
    elif childnum == "1":
        now = datetime.today()
        ret = now + relativedelta(days=+1)
        ret = "{}".format(ret.month) + "-" + "{}".format(ret.day) + "-" + "{}".format(ret.year)
    elif childnum == "2":
        now = datetime.today()
        ret = now + relativedelta(days=+2)
        ret = "{}".format(ret.month) + "-" + "{}".format(ret.day) + "-" + "{}".format(ret.year)
    print ret
    description = raw_input("Desc:")
    loc = raw_input("Location:")
    name = raw_input("Name:")
    starttime = raw_input("starttime 7:30 AM:")
    endtime = raw_input("endtime 8:40 PM:")


    rank = timesort(starttime)
    event = {"sorted_time": rank, "name":name, "start_time":starttime, "end_time":endtime, "location":loc, "lat":locDic[loc][0], "lng":locDic[loc][1], "date":ret, "description":description, "count": 0, "message": " people are attending"}
    firebase.post("/events/" + child,event)
