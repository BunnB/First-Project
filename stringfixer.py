"""
BonB
used to grab start time and end time and name from a string
where the string is formatted as such,
4:30 PM - 5:30 PM Collection - a Celebration of Light
"""

def stringfix(string):
    if "All Day" in string:
        index = string.find("All Day")
        name = string[index+len("All Day")+1::]
        time = "All Day"
        return [time,time,name]
    elif "PM" in string or "AM" in string:
        index1 = string.rfind("PM",0,20)
        index2 = string.rfind("AM",0,20)
        if index1 > index2:
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
        
    
        
        
if __name__ == "__main__":
    string = "6:30 PM - 10:30 PM Swag Money Party YOLOSWAG"
    print stringfix(string)