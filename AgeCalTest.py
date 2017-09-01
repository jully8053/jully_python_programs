# -*- coding: utf-8 -*-
"""
Created on Sat May 21 09:34:24 2016

@author: Radhe

"""

import datetime as dt

bd=dt.date(1994,9,21)
a=dt.date.today()
diff=a-bd
ans=diff.days/365
print(ans)


st="Serpentcs"

for i in st:
    print(i,'=',ord(i))