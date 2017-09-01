# -*- coding: utf-8 -*-
"""
Created on Tue May 24 17:52:52 2016

@author: Radhe
"""

class abc():
    
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def addition(self):
        return self.a+self.b
    
class child(abc):
    
    def __init__(self,x,y,z):
        super(child,self).__init__(x,y)
        self.c=z
        
    def addition(self):
        ans= super(child,self).addition()
        return self.c+ans