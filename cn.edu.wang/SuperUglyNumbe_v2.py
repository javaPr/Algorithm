#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/9 18:24
# @Author  : wangdechang


n = 22
primes = [17, 2, 3, 5, 7]
size = len(primes)
res = [0] * n
times = [0] * n
res[0] = 1
import sys

for i in range(1, n):
    min_val = sys.maxsize
    for j in range(size):
        min_val = min(min_val, primes[j]*res[times[j]])
    res[i] = min_val

    for j in range(size):
        if primes[j]*res[times[j]] == min_val:
            times[j] += 1



print(res[n-1])
