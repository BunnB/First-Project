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
        return [time,time,name]
    elif "PM" in string or "AM" in string:
        index1 = string.rfind("PM",0,20)
        index2 = string.rfind("AM",0,20)
        if index1 > index2:
	    if "End Time" in string:
		time = string[len("End Time "):index1+2]
		name = string[index1+3::]
		return ["",time,name]
            if index1*index2 <= 0 and index1 < 10:
                time = string[0:index1+2]
                name = string[index1+3::]
                return [time,name]
            else:
                time = string[0:index1 + 2]
                time = time.split(' - ')
                name = string[index1 + 3::]
                return [time[0],time[1],name]
        else:
            if index1*index2 <= 0 and index2 < 10:
                time = string[0:index2+ 2]
                name = string[index2+3::]
                return [time,name]
            else:
                time = string[0:index2 + 2]
                time = time.split(' - ')
                name = string[index2 + 3::]
                return [time[0],time[1],name]
    else:
	name = string
	time = "All Day"
	return [time,time,name]

def datefix(string):
    """
    Grabs proper date format from string of this type:
    Friday, February 03, 2017
    """
    now = datetime.today()
    months = {"January": "01","February": "02","March":"03","April":"04","May":"05","June":"06","July":"07","August":"08","September":"09","October":"10","November":"11","December":"12"}
    date = string.split(',')
    date = date[1::]
    for month, num in months.items(): #cleaning up date format and assiging day number(0,1,2)
        if month in string:
            now = datetime.today()
            day = months[month] + '-' + date[0][len(month)+2::] + '-'+date[1][1::]
            event_date = datetime(int(date[1][1::]),int(months[month]),int(date[0][len(month)+2::])) #usable for datetime
            event_date = event_date + relativedelta(days=+1) #end of day + 3 days ahead
            now = now + relativedelta(days=+1)
            i = 0
            while event_date > now:
                now = now + relativedelta(days=+1)
                i+=1
            return [day,"day" + str(i)]


if __name__ == "__main__":
    string = "Tuesday, January 31, 2017"
    datefix(string)
    string1 = "Tuesday, February 01, 2017"
    datefix(string1)
    string2 = "Tuesday, February 02, 2017"
    datefix(string2)
