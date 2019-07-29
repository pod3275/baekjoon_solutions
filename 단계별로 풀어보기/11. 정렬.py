# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 17:23:01 2019

@author: lawle
"""

# 2750번 수 정렬하기
import sys
sys.stdin = open("a.txt", "r")
n = int(sys.stdin.readline())
n_list = [int(sys.stdin.readline()) for i in range(n)]

n_list.sort()
for i in n_list:
    print(i)
    

# O(n^2)
# 1. Selection sort - 0~n index에 작은 수를 찾아 넣기 (위치가 정해짐)
import sys
sys.stdin = open("a.txt", "r")
n = int(sys.stdin.readline())
n_list = [int(sys.stdin.readline()) for i in range(n)]
count=0
for i in range(n):
    mini = n_list[i]
    index = i
    for j in range(i+1, n):
        count+=1
        if mini >= n_list[j]:
            index = j
    if index != i:
        n_list[i], n_list[index] = n_list[index], n_list[i]

for i in n_list:
    print(i)
print("Total count:", count)

# 2. Insertion Sort - 0~n index 숫자의 위치를 다시 재정의 (숫자가 정해짐)
import sys
sys.stdin = open("a.txt", "r")
n = int(sys.stdin.readline())
n_list = [int(sys.stdin.readline()) for i in range(n)]
count = 0
for i in range(n):
    start = i
    for j in range(i-1, -1, -1):
        count += 1
        if n_list[start] <= n_list[j]:
            n_list[start], n_list[j] = n_list[j], n_list[start]
            start = j
        else: break
    
for i in n_list:
    print(i)
print("Total count:", count)

# 3. Bubble Sort - 양옆을 비교하며 작은 걸 왼쪽으로 보내기
import sys
sys.stdin = open("a.txt", "r")
n = int(sys.stdin.readline())
n_list = [int(sys.stdin.readline()) for i in range(n)]
count = 0
for i in range(n):
    for j in range(n-i-1):
        count+=1
        if n_list[j+1] < n_list[j]:
            n_list[j], n_list[j+1] = n_list[j+1], n_list[j]
            
for i in n_list:
    print(i)
print("Total count:", count)

# O(nlogn)
# 4. Merge Sort - Divide and conquer 나누고 합병. 공간 O(2n)
import sys
sys.stdin = open("a.txt", "r")
n = int(sys.stdin.readline())
n_list = [int(sys.stdin.readline()) for i in range(n)]
count = 0

def merge(a, b):
    i=j=0
    answer = []
    while i != len(a) and j != len(b):
        if a[i] > b[j]:
            answer.append(b[j])
            j+=1
        elif a[i] <= b[j]:
            answer.append(a[i])
            i+=1
            
    while i != len(a):
        answer.append(a[i]); i+=1
    while j != len(b):
        answer.append(b[j]); j+=1
        
    return answer

def merge_sort(n_list):
    a = n_list[:int(len(n_list)/2)]
    b = n_list[int(len(n_list)/2):]
    if len(a) <= 1 and len(b) <= 1:
        return merge(a, b)
    else:
        return merge(merge_sort(a), merge_sort(b))
    
for i in merge_sort(n_list):
    print(i)

# 5. Quick Sort - Divide and conquer 나누는 것과 합병을 동시에. 공간 O(n)
import sys, random
sys.stdin = open("a.txt", "r")
n = int(sys.stdin.readline())
n_list = [int(sys.stdin.readline()) for i in range(n)]
count = 0

def quick_sort(a):
    if len(a) <= 1:
        return a
    
    n = len(a)
    pivot = int(random.random()*n)
    a[0], a[pivot] = a[pivot], a[0]
    l=1; r=n-1
    l_check=r_check=0
    
    while l<=r:
        if a[l] > a[0]: l_check = 1
        else: l+=1
        
        if a[r] < a[0]: r_check = 1
        else: r-=1
        
        if l_check == 1 and r_check == 1:
            a[l], a[r] = a[r], a[l]
            l+=1; r-=1
            l_check = r_check = 0
          
    a[r], a[0] = a[0], a[r]
    
    a[:r] = quick_sort(a[:r])
    a[r+1:] = quick_sort(a[r+1:])
    
    return a
            
for i in quick_sort(n_list):
    print(i)