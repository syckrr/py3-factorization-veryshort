#!/usr/bin/env python
#-*- coding: cp1254 -*-

a = int(input("Enter a number: "))
b = 2 #start with 2
while 1 < a:                #if process ends..
    while a % b == 0:       #i use while why? cuz for exmp: 4/2=2 2/2=1 there's two 2 number for b,this loop will control it
        a= a/b 
        print(b,'\n')       #print b
    b=b+1                   #when while ends,b will +
        
        
        
