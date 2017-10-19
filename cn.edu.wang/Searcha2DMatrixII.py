#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/19
# @Author  : wangdechang


class Solution:
    """
    @param: matrix: A list of lists of integers
    @param: target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """

    def searchMatrix(self, matrix, target):
        # write your code here
        size = len(matrix)
        if size == 0:
            return 0
        rows = size
        columns = len(matrix[0])
        count = 0

        # for i in range(columns):
        #     if matrix[0][i] == target:
        #         count += 1
        #         if i == 0:
        #             columns = 0
        #         else:
        #             columns = i - 1
        #     if matrix[0][i] > target:
        #         if i == 0:
        #             columns = 0
        #         else:
        #             columns = i - 1

        # for i in range(size):
        #     if matrix[i][0] == target:
        #         count += 1
        #         if i == 0:
        #             rows = 0
        #         else:
        #             columns = i - 1
        #     if matrix[0][i] > target:
        #         if i == 0:
        #             rows = 0
        #         else:
        #             rows = i - 1


        for row in range(size):
            if row <= rows:
                for column in range(columns):
                    if matrix[row][column] == target:
                        count += 1
                        columns = column
                        break
                    elif matrix[row][column] > target:
                        columns = column
                        break
            else:
                break
        return count

matrix = [
    [1,3,5,7],
    [3,11,16,20],
    [23,30,34,50]
]
target = 3

solution = Solution()
res = solution.searchMatrix(matrix,3)
print(res)


# size = len(matrix)
# rows = size
# columns = len(matrix[0])
# count = 0
#
# # for i in range(columns):
# #     if matrix[0][i] == target:
# #         count += 1
# #         if i == 0:
# #             columns = 0
# #         else:
# #             columns = i - 1
# #     if matrix[0][i] > target:
# #         if i == 0:
# #             columns = 0
# #         else:
# #             columns = i - 1
# #
# # for i in range(size):
# #     if matrix[i][0] == target:
# #         count += 1
# #         if i == 0:
# #             rows = 0
# #         else:
# #             columns = i - 1
# #     if matrix[0][i] > target:
# #         if i == 0:
# #             rows = 0
# #         else:
# #             rows = i - 1
#
# for row in range(size):
#     if row <= rows:
#         for column in range(columns):
#             if matrix[row][column] == target:
#                 count += 1
#                 columns = column - 1
#                 break
#     else:
#         break
#
# print(count)
