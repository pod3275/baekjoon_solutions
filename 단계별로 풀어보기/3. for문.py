# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 21:49:52 2019

@author: lawle
"""

'''
for문
'''

# 10950번 a+b 출력
t = int(input())
a = []
for i in range(t):
     a.append(sum(map(int, input().split())))
for i in range(t):
    print(a[i])
    
# 8393번 합
a = int(input())
print(sum(range(1,a+1)))

# 15552번 빠른 a+b
import sys
n = int(input())
for i in range(n):
    print(sum(map(int, sys.stdin.readline().split())))

# 2741번 n찍기
n = int(input())
for i in range(n):
    print(i+1)
    
# 2742번 기찍N
n = int(input())
for i in range(n, 0, -1):
    print(i)

# 11021번 A+B-7
import sys
n = int(input())
for i in range(n):
    print("Case #{0}:".format(i+1), sum(map(int,sys.stdin.readline().split())))
          
# 11022번 A+B-8
import sys
n = int(input())
for i in range(1,n+1):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #{0}: {1} + {2} = {3}".format(i, a, b, a+b))

# 1002번 터렛 문제
import sys, math
n = int(input())
for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    dist = math.sqrt(pow((x1-x2),2)+pow((y1-y2),2))
    if dist > r1+r2: print("0")
    elif dist == r1+r2: print("1")
    else:
        if dist == 0:
            if r1 == r2: print("-1")
            else: print("0")
        elif dist == abs(r1-r2): print("1")
        elif dist<abs(r1-r2): print("0")
        else: print("2")
        
# 2438번 별 찍기-1
import sys
n = int(input())
for i in range(1,n+1):
    print("*"*i)

#2439번 별 찍기-2
import sys
n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)

# 10871번 X보다 작은 수
n, x = map(int, input().split())
a = list(map(int, input().split()))

b = list(filter(lambda i: i<x, a))
b = [i for i in a if i<x] # 위와 같은 의미임

print(" ".join(str(i) for i in b))
