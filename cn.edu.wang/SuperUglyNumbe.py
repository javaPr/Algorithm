#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/9 18:24
# @Author  : wangdechang

'''
time out
'''
def find(arr, value):
    arr_size = len(arr)
    if arr_size == 0:
        return 0
    low, high = 0, arr_size - 1
    mid = (low + high) // 2
    while low < high:
        if arr[mid] < value:
            low = mid + 1
        elif arr[mid] > value:
            high = mid - 1
        elif arr[mid] == value:
            return -1
        mid = (low + high) // 2

    # if value < arr[low] and low - 1 >= 0 and value > arr[low - 1]:
    #     return low
    # if value > arr[low]:

    if arr[low] < value:
        return low + 1

    return low


n = 22
primes = [17, 2, 3, 5, 7]
primes.sort()

pos = 0
pre = 0
while pos < n:
    temp = primes[pos] * primes[pre]

    if temp not in primes:
        insert_loc = find(primes, temp)
        if insert_loc != -1:
            primes.insert(insert_loc, temp)
    if pos == pre:
        pos += 1
        pre = 0
    else:
        pre += 1

print(primes)
print(primes[n - 2])
