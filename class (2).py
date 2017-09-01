# -*- coding: utf-8 -*-
"""
Created on Mon May  9 10:57:17 2016

@author: Radhe
"""

class main:
    
    def __init__(self):
        print("tha ia under main class")
        
    def dis(self):
        print("THis is main calss method")
        
class child(main):
    
    def __init__(self):
        print("you are a under child class")
        
    def dis(self):
        print("This is child class method")
    
obj =child()
obj.dis()