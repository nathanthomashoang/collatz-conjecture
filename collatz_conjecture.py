# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 13:42:52 2019

@author: Nathan Hoang
"""

def collatz(num):
    #for num as input, function will return the number of steps to reach "1"
    x = num
    step_counter = 0

    if num > 1:
        print(x)
        while not x == 1:
            if x%2 == 0:
                x /= 2
                step_counter += 1
            else:
                x = (x*3)+1
                step_counter += 1
            print(int(x))
        print(f'\n number of steps to reach "1": {step_counter}')