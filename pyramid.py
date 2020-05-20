# -*- coding: utf-8 -*-
"""
Created on Wed May 20 15:00:58 2020

@author: rpnigam
"""

n=int(input())
#write your code here

for i in range (0, n):
    print ('#'  * (i) + \
           ('*' * (2*(n-i) - 1)) + \
           '#'  * (i) )