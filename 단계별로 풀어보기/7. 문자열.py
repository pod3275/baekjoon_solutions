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
        
# 10809번 알파벳 찾기 - for문 26 - index 대신 find 가능
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

# 10809번 알파벳 찾기 - for문 len(string) - 최소 시간 달성 : range, enum은 메모리 비효율적임
answer = [-1 for i in range(26)]
string = input()
i = 0
while i < len(string):
    if answer[ord(string[i])-97] == -1:
        answer[ord(string[i])-97] = i
    i += 1
print(" ".join(str(x) for x in answer))


# 1152번 단어의 개수 - empty string + specified split --> return ['']
string = input().strip()
if string=='':
    print('0')
else:
    print(len(string.split(' ')))
    
    
# 2675번 문자열 반복
import sys
# sys.stdin = open("a.txt.", "r")
n = int(sys.stdin.readline())
i=0
while i != n:
    r, string = map(str, sys.stdin.readline().split())
    for char in string:
        print(char* int(r), end="")
    print("")
    i+=1
    
    
# 1157번 단어 공부
import sys
sys.stdin = open("a.txt", "r")
string = sys.stdin.readline().strip()
count_alpha = [0]*26
for char in string:
    count_alpha[ord(char.upper())-ord('A')] += 1
ans = [i for i in range(len(count_alpha)) if count_alpha[i] == max(count_alpha)]
if len(ans) > 1 : print("?")
else: print(chr(count_alpha.index(max(count_alpha))+ord('A')))

# 1157번 단어 공부 - short coding - 문자열 내에 포함된 문자는 set을 이용
string = sys.stdin.readline().strip().upper()
m=0
for char in set(string):
    c = string.count(char)
    if c == m: out = '?'
    elif c > m:
        m, out = c, char
print(out)


# 2908번 상수
import sys
sys.stdin = open("a.txt", "r")
a, b = map(str, sys.stdin.readline().split())
c, d = int(a[::-1]), int(b[::-1])
if c>d: sys.stdout.write(c)
elif c<d: sys.stdout.write(d)


# 5622번 다이얼
string = input()
d = {}
d['A'] = d['B'] = d['C'] = 2
d['D'] = d['E'] = d['F'] = 3
d['G'] = d['H'] = d['I'] = 4
d['J'] = d['K'] = d['L'] = 5
d['M'] = d['N'] = d['O'] = 6
d['P'] = d['Q'] = d['R'] = d['S'] = 7
d['T'] = d['U'] = d['V'] = 8
d['W'] = d['X'] = d['Y'] = d['Z'] = 9
time = 0
for char in string:
    time += d[char]+ 1
print(time)


# 2941번 크로아티아 알파벳
import sys
# sys.stdin = open("a.txt", "r")
string = sys.stdin.readline().strip()
print(len(string)-string.count("c=")-string.count("c-")-string.count("dz=")-string.count("d-")-string.count("lj")-string.count("nj")-string.count("s=")-string.count("z="))

# 2941번 길어지지 않게 하기 - map 사용
import sys
string = sys.stdin.readline().strip()
print(len(string)-sum(map(string.count, ["c=","c-","dz=","d-","lj","nj","s=","z="])))


# 1316번 그룹 단어 체커
import sys
# sys.stdin = open("a.txt", "r")
n = int(sys.stdin.readline())
i, count = 0, 0
while i != n:
    string = sys.stdin.readline().strip()
    no = 0
    for char in set(string):
        if len(string)-string[::-1].find(char)-string.find(char) != string.count(char):
            no = 1
    if not no:
        count +=1
    i+=1
print(count)

# 좀 강력한 코드
import sys
# sys.stdin = open("a.txt", "r")
n = int(sys.stdin.readline())
i, count = 0, 0
while i != n:
    string = sys.stdin.readline().strip()
    if list(string) == sorted(string, key=string.find):
        count += 1
    i+=1
print(count)