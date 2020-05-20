# -*- coding: utf-8 -*-
"""
Created on Wed May 20 14:48:06 2020

@author: rpnigam
"""

n=int(input())
#write your code here

depth = n*2 - 1

for i in range (n-1, 0, -1):
    print ('#'*(i-1) + \
           ('*' * (2* (n-i) - 1)) + \
           '#'*(i-1) )