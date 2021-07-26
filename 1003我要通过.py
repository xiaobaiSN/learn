# -*- coding: utf-8 -*-
"""
Created on Sat May  8 09:31:09 2021

@author: lenovo
"""

a=int(input())
for i in range(a):
    b=input()
    if len(b)<3:
        print("NO")
    if b.count('P')!=1 or b.count('T'):
        print('NO')
    for i in b:
        if i not in ['P','A','T']: 
            print("NO")
    if 