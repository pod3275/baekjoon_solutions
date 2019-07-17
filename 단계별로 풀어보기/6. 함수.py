# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 22:13:18 2019

@author: lawle
"""


# 15596번 정수 N개의 합
def solve(a: list):
    return sum(a)


# 4673번 셀프 넘버 - 재귀함수, 스택
def self_num(n, visited):
    next_num = n
    next_num += sum(list(map(int, " ".join(str(n)).split())))
    if next_num <= 10000 and next_num not in visited:
        visited.append(next_num)
        self_num(next_num, visited)
    else: return
    
visited = []
stack = [i for i in range(10000,0,-1)]
while True:
    self_num(stack.pop(), visited)
    if len(stack) == 0: break
for i in range(1,10001):
    if i not in visited:
        print(i)


# 4673번 셀프 넘버 - for문 1번
def self_num(n):    
    next_num = n
    next_num += sum(list(map(int, " ".join(str(n)).split())))
    return next_num
    
visited = set()
for i in range(1,10001):
    visited.add(self_num(i))

for i in range(1,10001):
    if i not in visited:
        print(i)


# 1065번 한수
def is_hansu(n: int):
    hansu_check = 1
    jarisu = list(map(int, " ".join(str(n)).split()))
    if len(jarisu) == 1 or len(jarisu) == 2:
        return True
    else:
        chai = jarisu[1] - jarisu[0]
        for i in range(1, len(jarisu)-1):
            if jarisu[i+1]-jarisu[i] != chai:
                hansu_check = 0
        if hansu_check == 1:
            return True
        else:
            return False

n = int(input())
count = 0
for i in range(1, n+1):
    if is_hansu(i): count+=1
print(count)
    

# 10872번 팩토리얼
def factorial(n):
    if n <= 1: return 1
    else: return n*factorial(n-1)
    
n = int(input())
print(factorial(n))


# 2447번 별 찍기-10 - 재귀 시간초과 떠서 dp로 하려고 했으나 메모리 에러
dp = dict()
def star(x, y, n):
    if n == 1: 
        sys.stdout.write("*")
        return "*"
        
    elif x // int(n/3) == 1 and y // int(n/3) == 1:
        sys.stdout.write(" ")
        return " "
    
    elif (x%int(n/3),y%int(n/3)) in dp.keys():
        sys.stdout.write(dp[(x%int(n/3),y%int(n/3))])
        return dp[(x%int(n/3),y%int(n/3))]
        
    else:
        return star(x%int(n/3), y%int(n/3), int(n/3))

n = int(input())
for i in range(n):
    for j in range(n):
        dp[(i,j)] = star(i, j, n)
    print("\n", end="")

# 문제는 print --> sys.stdout.write 로 수정
import sys
def star(x, y, n):
    if n == 1: 
        sys.stdout.write("*")
        return
        
    elif x // int(n/3) == 1 and y // int(n/3) == 1:
        sys.stdout.write(" ")
        return
        
    else:
        return star(x%int(n/3), y%int(n/3), int(n/3))

n = int(input())
for i in range(n):
    for j in range(n):
        star(i, j, n)
    sys.stdout.write("\n")

# 최적화--> 재귀를 안쓰는게 빠름
import sys

def star(x, y):
    while x != 0:
        if x%3 == 1 and y%3 == 1:
            sys.stdout.write(" ")
            return
        x = x//3
        y = y//3
    sys.stdout.write("*")

n = int(input())
for i in range(n):
    for j in range(n):
        star(i, j)
    sys.stdout.write("\n")
    

# 11729번 하노이 탑 이동 순서
import sys

def print_hanoi(max, src, dst, mid):
    if max == 1:
        sys.stdout.write("{0} {1}\n".format(src, dst))
    else:
        print_hanoi(max-1, src, mid, dst)
        sys.stdout.write("{0} {1}\n".format(src, dst))
        print_hanoi(max-1, mid, dst, src)
        
#sys.stdin = open("a.txt", "r")
n = int(sys.stdin.readline().rstrip())
sys.stdout.write("{0}\n".format(pow(2,n)-1))
print_hanoi(n, 1, 3, 2)