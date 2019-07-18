# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 22:23:06 2019

@author: lawle
"""


# 11654번 아스키 코드
print(ord(input()))


# 11720번 숫자의 합
import sys
# sys.stdin = open("a.txt", "r")
n = int(sys.stdin.readline())
m = sys.stdin.readline().strip()
sum=0
for char in m: sum+=int(char)
print(sum)


# 10809번 알파벳 찾기 - for문 26 - index
import sys
# sys.stdin = open("a.txt", "r")
string = sys.stdin.readline().strip()

for i in range(ord('a'),ord('z')+1):
    try:
        sys.stdout.write(str(string.index(chr(i))) + " ")
    except:
        sys.stdout.write("-1 ")
        
# 10809번 알파벳 찾기 - for문 26 - index대신 find 가능
import sys
# sys.stdin = open("a.txt", "r")
string = sys.stdin.readline().strip()

for i in range(ord('a'),ord('z')+1):
    sys.stdout.write(str(string.find(chr(i))) + " ")

# 10809번 알파벳 찾기 - for문 len(string)
import sys
# sys.stdin = open("a.txt", "r")
answer = [-1 for i in range(26)]
string = sys.stdin.readline().strip()
for idx, char in enumerate(string):
    if answer[ord(char)-ord('a')] == -1:
        answer[ord(char)-ord('a')] = idx
print(" ".join(str(x) for x in answer))

# 10809번 알파벳 찾기 - for문 len(string) - 최소 시간 달성 : range, enum은 느리다
answer = [-1 for i in range(26)]
string = input()
i = 0
while i < len(string):
    if answer[ord(string[i])-97] == -1:
        answer[ord(string[i])-97] = i
    i += 1
print(" ".join(str(x) for x in answer))
