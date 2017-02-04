from firebase import *
from fixers import *
from datetime import *
from dateutil.relativedelta import *
from locDic import locDic

firebase = firebase.FirebaseApplication('https://mapapp-2a84b.firebaseio.com/',None)

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
