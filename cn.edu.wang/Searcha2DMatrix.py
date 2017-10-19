#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/19
# @Author  : wangdechang

matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
target = 3

is_have = False

size = len(matrix)
for i in range(size):
    if matrix[i][0] > target:
        is_have = False
        break
    elif matrix[i][0] == target:
        is_have = True
        break
    else:
        temp_size = len(matrix[i])
        if matrix[i][temp_size-1] > target:
            for value in matrix[i]:
                if value == target:
                    is_have = True
                    break
            if is_have:
                break

print(is_have)
