# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 19:19:54 2019

@author: NOTEBOOK
"""

def main():
    show_interest(principal=1000,period=10,rate=0.01)
    
def show_interest(principal,period,rate):
    interest = principal * period * rate
    print('The interest will be $', format(interest,',.2f'), sep='')
    
    
main()