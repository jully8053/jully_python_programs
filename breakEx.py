# -*- coding: utf-8 -*-
"""
Created on Fri May 20 11:32:34 2016

@author: Radhe
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
c=0
for i in range(1,50):
    if i%2==0:
        c=c+1
        print("Even no is",i)
    if c>=10:
        print(c)
        break