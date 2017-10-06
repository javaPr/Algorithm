#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
k = 4
nums = [-1, -2, -3, -100, -1, -50]
size = len(nums)
maxValue = -sys.maxsize - 1

for i in range(0, size - k + 1):
    temp = sum(nums[i:i + k]) * 1.0 / k
    # print(nums[i:i+k])
    if temp > maxValue:
        maxValue = temp
        if i <= size - k:
            for j in range(i + k, size + 1):
                temp = sum(nums[i:j]) * 1.0 / (j - i)
                if temp > maxValue:
                    maxValue = temp

print(maxValue)
