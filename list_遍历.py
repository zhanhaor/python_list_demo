#!/usr/bin/env python
# -*- coding: utf-8 -*-

def test1():
    """for in list"""
    mylist = [1,2,3,4,5]

    for i in mylist:
        print i

mylist = ['A','2','A3','E4','D5']
def test2():
    """for in list"""
    
    for i in mylist:
        print i
# test2()


def error_test():
    """for in len(list)"""
    for i in len(mylist):

        print i
    '''error : 'int' object is not iterable'''
# error_test()


def error_test2():
   """for in range(list)""" 

   for i in range(mylist):
       print i
    '''error: range() integer end argument expected, got list.'''
# error_test2()
