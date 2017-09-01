# -*- coding: utf-8 -*-
"""
Created on Tue May 24 17:50:26 2016

@author: Radhe
"""



import datetime as dt

bd=dt.date(1994,6,13)
current=dt.date.today()
diff=current-bd
ans= diff.days/365
print(ans)