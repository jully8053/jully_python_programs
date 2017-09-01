# -*- coding: utf-8 -*-
"""
Created on Thu May 19 10:45:16 2016

@author: Radhe
"""
from datetime import datetime as dt

current=dt.now()
print("Current date and Time:-",current)
time=current.time()
print("Current time:-",time)
today=current.today()
print("Today:-",today)
date=current.date()
print("Current Date:-",date)

month=current.month
print("Current month:-",month)
year=current.year
print("Current Year:-",year)
hour=current.hour
print("Current Hour:-",hour)
minute=current.minute
print("Minute is:-",minute)
second=current.second
print("Second is:-",second)
micor=current.microsecond
print("Microsecond is:-",micor)
weekday=current.weekday()
print("Weekday is:-",weekday)
