# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 22:03:32 2019

@author: lawle
"""

# sys.stdin = open("a.txt", "r")

'''
while문
'''

#10952번 A+B-5
import sys
while True:
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)
    if a==0 and b==0: break
    
# 10951 번 A+B-4
import sys
for line in sys.stdin:
    a, b = map(int, line.split())
    print(a+b)
    
# 10951 번 A+B-4 다른 풀이 : 예외 try-except
import sys
while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        print(a+b)
    except: break

# 1110번 더하기 사이클
mid = n = int(input())
count = 1
while True:
    a = mid%10
    b = (a+mid//10)%10
    mid = a*10+b
    if mid == n: break
    else:
        count += 1
print(count)