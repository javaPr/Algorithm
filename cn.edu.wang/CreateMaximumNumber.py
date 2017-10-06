#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/30 15:07
# @Author  : wangdechang
import sys


def get_max(nums, k):
    res = [-sys.maxsize - 1] * k
    i = 0
    size = len(nums)
    if size == 0:
        return []
    for j in range(size):
        while size - j + i > k and i > 0 and res[i - 1] < nums[j]:
            i -= 1
        if i < k:
            res[i] = nums[j]
            i += 1
    return res


def is_greater(num1, i, num2, j):
    size = len(num1)

    while i < size and j < len(num2):
        if num1[i] > num2[j]:
            return True
        if num1[i] < num2[j]:
            return False
        i += 1
        j += 1
    return not i == size


def merge(num1, num2, k):
    res = [0] * k
    i = 0
    j = 0
    if len(num1) == 0:
        return num2
    if len(num2) == 0:
        return num1

    for pos in range(k):
        if is_greater(num1, i, num2, j):
            res[pos] = num1[i]
            i += 1
        else:
            res[pos] = num2[j]
            j += 1
    return res


nums1 = [1,2,3,4]
nums2 = []
k = 2



m = len(nums1)
n = len(nums2)

if m == 0:
    print(get_max(nums2,k))
if n == 0:
    print(get_max(nums1,k))
if n + m == k:
    print(merge(nums1,nums2,k))

max = m if k >= m else k
min = 0 if n >= k else k - n

if max == min and min > 0:
    print(get_max(nums1,k))

res_data = [-sys.maxsize - 1] * k
for i in range(min, max):
    temp = merge(get_max(nums1, i), get_max(nums2, k - i), k)
    res_data = temp if is_greater(temp, 0, res_data, 0) else res_data

print(res_data)
