"""
BUNNB 2k17
MY SWARTHMORE EVENT WEBSCRAPER
"""

import urllib2
from bs4 import BeautifulSoup
from scraperobject import *
from datetime import *
from dateutil.relativedelta import *
import json
import calendar
from firebase import *

"""
TODAYS DATE AND NEXT'S WEEK DATE
"""
now = datetime.today()
later = now + relativedelta(days=+7)
day = now.day
n_day = later.day
month = now.month
n_month = later.month
year = now.year
n_year = later.year

"""
"""

def grabstring(url):
    """
    grabs and returns a string of the html of the calender
    page which contains locations and their times and such
    """
    page = urllib2.urlopen(url)
    html = page.read()
    soup = BeautifulSoup(html,'lxml')
    textsoup = soup.get_text()
    start = textsoup.rfind('Location View')
    end = textsoup.find('Calendar Software')
    mydoc = (textsoup[start:end])
    mydoc = mydoc.encode("utf-8")
    return mydoc 

def graburl():
    """
    returns proper URL for the page
    """
    url = "http://calendar.swarthmore.edu/calendar/EventList.aspx?fromdate={}%2f{}%2f{}&todate={}%2f{}%2f{}&display=Week&view=Location#".format(month,day,year,n_month,n_day,n_year)
    return url

def scrape():
    """
    grabs events from string of parsed html from the page
    """
    url = graburl()
    mydoc = grabstring(url)
    scraper = SwatScraper(mydoc)
    scraper.findEvents()
    return scraper.events
    
if __name__ == "__main__":
    list_of_events = scrape()
    print list_of_events
    #firebase = firebase.FirebaseApplication('https://mapapp-2a84b.firebaseio.com/',None)
    #sent = json.dumps(list_of_events)
    #result = firebase.post("/events",sent)
    #with open('data.json','w') as outfile:
        #json.dump(list_of_events,outfile,indent=4)

