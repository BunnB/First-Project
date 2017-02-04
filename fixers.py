from datetime import *
from dateutil.relativedelta import *

def stringfix(string):
    """
    BonB
    used to grab start time and end time and name from a string
    where the string is formatted as such,
    4:30 PM - 5:30 PM Collection - a Celebration of Light
    """
    if "All Day" in string:
        index = string.find("All Day")
        name = string[index+len("All Day")+1::]
        time = "All Day"
        return [time,time,name,timesort(time)]
    elif "PM" in string or "AM" in string:
        index1 = string.rfind("PM",0,20)
        index2 = string.rfind("AM",0,20)
        if index1 > index2: #PM and AM exists, PM is the later time; AM doesn't exist
            if "End Time" in string:   #weird cases where an event start and end time are split into 2 time instances
                time = string[len("End Time "):index1+2]
                name = string[index1+3::]
                return ["",time,name,timesort(time)]
            if index1*index2 <= 0 and index1 < 10: #If AM is missing, grab's just PM
                time = string[0:index1+2]
                name = string[index1+3::]
                return [time,name,timesort(time)]
            else:
                time = string[0:index1 + 2]
                time = time.split(' - ')
                name = string[index1 + 3::]
                return [time[0],time[1],name,timesort(time[0])]
        elif index2 > index1: #PM and AM exists, AM is the later time; PM doesn't exist
            if "End Time" in string:
                time = string[len("End Time "):index2+2]
                name = string[index2+3::]
            	return ["",time,name,timesort(time)]
            if index1*index2 <= 0 and index2 < 10:
                time = string[0:index2+ 2]
                name = string[index2+3::]
                return [time,name,timesort(time)]
            else:
                time = string[0:index2 + 2]
                time = time.split(' - ')
                name = string[index2 + 3::]
                return [time[0],time[1],name,timesort(time[0])]
    else: #no time info
	       name = string
	       time = "All Day"
	       return [time,time,name]

def timesort(time):
    """
    Used in string fix, generates ranking based on start time
    "4:30 AM", "All Day"

    """
    if time == "All Day":
        rank = 0
        return rank
    else:
        if "AM" in time:
            index = time.rfind("AM") - 1
            rank = time[:index]
            rank = rank.split(":")
            if rank[0] == "12":
                rank[0] = 0
            rank = (int(rank[0])*60) + (int(rank[1]))
            return rank
        elif "PM" in time:
            index = time.rfind("PM") -1
            rank = time[:index]
            rank = rank.split(':')
            if rank[0] == "12":
                rank[0] = 0
            rank = (int(rank[0])*60) + (int(rank[1])) + (12*60)
            return rank



def dateformat(string):
    """
    Grabs proper date format from string of this type:
    Friday, February 03, 2017
    returns [formatted date,daybranch]
    """
    now = datetime.today()
    months = {"January": "01","February": "02","March":"03","April":"04","May":"05","June":"06","July":"07","August":"08","September":"09","October":"10","November":"11","December":"12"}
    date = string.split(',')
    date = date[1::]
    for month, num in months.items(): #cleaning up date format and assiging day number(0,1,2)
        if month in string:
            now = datetime.today()
            day = months[month] + '-' + date[0][len(month)+2::] + '-'+date[1][1::]
            branch = getbranch(day)
            return [day,branch] #[]

def getbranch(day):
    """
    returns branch name from formatted event date
    """
    now = datetime.today()
    day = day.split("-")
    event_date = datetime(int(day[2]),int(day[0]),int(day[1])) #usable for datetime
    event_date = event_date + relativedelta(days=+1) #end of day + 3 days ahead
    now = now + relativedelta(days=+1)
    i = 0
    while event_date > now:
        now = now + relativedelta(days=+1)
        i+=1
    branch = "day" + str(i)
    return branch


if __name__ == "__main__":
    string = "2-16-2017"
    print(getbranch(string))
