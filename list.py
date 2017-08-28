#!/usr/bin/env python
# -*- coding: utf-8 -*-
def list1():
    """2个元素的list - 取 -1"""
    list = ['a','b']
    a = list[-1]

    print(a) #输出'b'，最后一个


def list2():
    """3个元素的list - 取 -1"""
    list = ['a','b','c']
    a = list[-1]

    print(a) #输出'c'，最后一个

list2()#得出结论 - list[-1] ==> 取出list列表中的最后一个元素