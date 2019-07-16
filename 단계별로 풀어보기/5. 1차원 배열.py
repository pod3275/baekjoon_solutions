# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 22:04:06 2019

@author: lawle
"""

# sys.stdin = open("a.txt", "r")

'''
1차원 배열
'''

# 10818번 최소,최대
import sys
n = int(input())
num = list(map(int, sys.stdin.readline().split()))
print(min(num), max(num))
    
# 2562번 최댓값
import sys
v = [int(i.rstrip()) for i in sys.stdin.readlines()]
print(max(v))
print(v.index(max(v))+1)

# 2920번 음계
import sys
music = list(map(int, sys.stdin.readline().split()))
music2 = sorted(music, reverse=False)
music3 = sorted(music, reverse=True)
if music == music2: print("ascending")
elif music == music3: print("descending")
else: print("mixed")

# 2577번 숫자의 개수
import sys
numbers = [int(i.strip()) for i in sys.stdin.readlines()]
result = str(numbers[0]*numbers[1]*numbers[2])
for i in range(0,10):
    print(result.count(str(i)))
#숏코딩
a=input; result=str(int(a())*int(a())*int(a()))
for i in range(10): print(result.count(str(i)))

# 3052번 나머지
import sys
num = [int(i.rstrip())%42 for i in sys.stdin.readlines()]
print(len(list(set(num))))

# 1546번 평균
n = int(input())
exam = list(map(int, input().split()))
print(sum([i/max(exam)*100 for i in exam])/len(exam))

# 8958번 OX퀴즈 - 리스트
import sys
n = int(input())
for i in range(n):
    OX = list(map(str, sys.stdin.readline().strip().split('X'))) # readline + split --> strip 필수
    print(sum([sum(range(1,len(i)+1)) for i in OX if i != '']))

# 8958번 OX퀴즈 - 스택
import sys
n = int(sys.stdin.readline())
for i in range(n):
    stack = []
    score = 0
    OX = sys.stdin.readline()
    for char in OX:
        if char == 'O':
            if len(stack) == 0: stack.append(1)
            else: stack.append(stack[-1]+1)
        else:
            score += sum(stack)
            stack = []
    if len(stack) != 0: score += sum(stack)
    print(score)

# 4344번 평균은 넘겠지
import sys
n = int(input())
for i in range(n):
    a = list(map(int, input().split(" ")))
    print("%.3f%%" % (len([i for i in a[1:] if i> sum(a[1:])/a[0]])/a[0]*100) )