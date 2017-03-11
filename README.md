# My first CS project

(worked on it during my time in the Intro to Computer Science class @ Swarthmore)

This project serves as the the backend for an Swarthmore event-tracking web app. The collection of scripts scrapes event information from the swarthmore calendar website and posts the event data (JSON) into firebase sorting them based on date and whether the event is currently occurring. Included is a manual event-adding tool, an event-approving tool for student-submitted events, and a microsoft excel writer to write in event details into an excel log.

Things gained:

Familiarity with JSON data format

Familiarity Firebase API

Familiarity with popular python packages such as requests, bs4, datetime, urllib, and more

Improved general python skills and development skills
# 
#
##############################################################################################################################

dupecheck: checks for duplicate events before adding to database
 
  eventadder: UI for approving pre-approved events, also write to xl file
  
  eventaddermanual: UI for adding events manually
 
  firebaseupdater: Used in scraperobject to update branches of firebase
 
  fixers: various util/ string formatters used
 
  locDic: Location and lat lng coords for specific campus locations
 
  nowevents: Find events that are happening now and adds into "now" branch, removes events if not now
 
  scraperobject: scrapes info and adds to firebase from long html string
 
  webscrape: does everything

##############################################################################################################################
#
#
