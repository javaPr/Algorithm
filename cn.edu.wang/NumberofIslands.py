#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/10 21:11
# @Author  : wangdechang 
class Solution:
    """
    @param: grid: a boolean 2D matrix
    @return: an integer
    """

    def numIslands(self, grid):
        grid = [
            [1, 1, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1]
        ]

        size = len(grid)
        count = 0
        for i in range(size):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:

                    self.adjacent(grid, i, j, 1)
                    self.adjacent(grid, i, j, 2)
                    self.adjacent(grid, i, j, 3)
                    count += 1
                    grid[i][j] = 0
        print(count)

    '''
    direction 0:up , 1:right, 2:down, 3:left
    '''

    def adjacent(self, grid, i, j, direction):
        row = len(grid)
        column = len(grid[0])
        if direction == 1:
            if j + 1 < column and grid[i][j + 1] == 1:
                j += 1
                grid[i][j] = 0
                self.adjacent(grid, i, j, 1)
                self.adjacent(grid, i, j, 2)
                self.adjacent(grid, i, j, 3)


        elif direction == 2:
            if i + 1 < row and grid[i + 1][j] == 1:
                i += 1
                grid[i][j] = 0
                self.adjacent(grid, i, j, 1)
                self.adjacent(grid, i, j, 2)
                self.adjacent(grid, i, j, 3)

        elif direction == 3:
            if j - 1 >= 0 and grid[i][j-1] == 1:
                j -= 1
                grid[i][j] = 0
                self.adjacent(grid, i, j, 1)
                self.adjacent(grid, i, j, 2)
                self.adjacent(grid, i, j, 3)



solution = Solution()
solution.numIslands([])
