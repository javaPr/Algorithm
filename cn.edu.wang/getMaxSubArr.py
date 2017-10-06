#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/5 15:50
# @Author  : wangdechang
import sys

# nums = [9, 1, 2, 5, 8]
nums = [4, 3, 8, 6, 5, 9, 9]
k = 3
result = [-sys.maxsize - 1] * k

i = 0
size = len(nums)

for j in range(size):
    while size - j + i > k and i > 0 and result[i - 1] < nums[j]:
        i -= 1

    if i < k:
        result[i] = nums[j]
        i += 1
print(result)
