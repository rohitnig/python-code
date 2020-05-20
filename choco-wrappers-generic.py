# -*- coding: utf-8 -*-
"""
Created on Wed May 20 16:39:20 2020

@author: rpnigam
"""

''' Recall that in the last live coding session, you solved the chocolate problem where Sanjay had m 
    rupees and cost of each chocolate was c rupees. Shopkeeper gave away one chocolate for three wrappers. 
    In this problem lets generalise the question saying, Sanjay has m rupees, each chocolate costs c rupees, 
    shopkeeper will give away k chocolates for w wrappers. 
    Can you find now how many chocolates Sanjay will be able to eat?

Sample input:  15, 2, 3, 1
Sample output: 10
Explanation:
    - Sanjay has 15 rupees, buys 7 chocolates for 2 rupees each.
    - Sanjay now has 7 wrappers, exchanges 6 of them for 2 more chocolates.
    - Sanjay now has 3 wrappers and exchanges them for 1 more chocolate making a total of 10 chocolates
'''

ip = input()
(m, c, w, k) = tuple([int(i) for i in ip.split(',')])

total_choc = 0
wrappers   = 0

while True:
    chocs_money   = (m // c)
    chocs_wrapper = (wrappers // w) * k
    m -= chocs_money * c
    wrappers -= (wrappers // w) * w
    wrappers += chocs_money + chocs_wrapper
    total_choc += chocs_money + chocs_wrapper 
    if chocs_money + chocs_wrapper == 0:
        break

print (total_choc)    

