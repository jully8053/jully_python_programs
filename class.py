# -*- coding: utf-8 -*-
"""
Created on Thu May 19 11:56:49 2016

@author: Radhe
"""
class test:
    def __init__(self,name):
        self.name=name
        
    def dis(self):
        print(self.name)
        
    def testy(self,address,age):
        print(address)
        print(age)
        
obj=test("Hiren")
obj.dis()

obj.testy("JND",22)