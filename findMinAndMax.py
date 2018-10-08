#!/usr/bin/env python3
#-*-coding:utf8-*-
#findMinAndMax
#
def findMinAndMax(L):
    if L != []:
        max=L[0]
        min=L[0]
        for i in L:
                if i>max:
                        max=i
                if i<min:
                        min=i
        return(min,max)
    else:
        return(NONE,NONE)
L=(1.3,6,11,5,8,4,13,-1)
print(findMinAndMax(L))
