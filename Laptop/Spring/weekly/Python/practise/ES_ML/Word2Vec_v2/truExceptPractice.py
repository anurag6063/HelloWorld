# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 16:00:22 2018

@author: anuryadav
"""

def tryCatch(inputs):    
    if inputs == True:
        try:
            result = 'Yes, true'
            print(result)           
        except ValueError:
            print('its false ', ValueError)
        