# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 21:59:14 2019

@author: lawle
"""

# 2798번 블랙잭
import sys
sys.stdin = open("a.txt", "r")
n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort(reverse=False)
ans = 0
is_end = False
for i in range(n):
    if nums[i] <= m/3:
        for j in range(i+1, n):
            for k in range(j+1, n):
                if nums[i]+nums[j]+nums[k] > ans and nums[i]+nums[j]+nums[k]<= m:
                    ans = nums[i]+nums[j]+nums[k]
                if ans == m:
                    is_end = True
                    break
            if is_end:
                break
    if is_end:
        break
print(ans)


# 2231번 분해합
