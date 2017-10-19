#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/6 13:07
# @Author  : wangdechang 

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: a TreeNode, the root of the binary tree
    @return:
    """

    def flatten(self, root):
        self.tree = None
        if not root:
            self.tree = TreeNode(root.val)
            temp = self.tree
            self.pre_order(root.left)
            self.pre_order(root.right)
            # tree = TreeNode(root.val)
            # prev = tree
            # while not root:
            #     preTemp = root
            #     if not root.left:
            #         root = root.left
            #         tree.right = TreeNode(root.val)

    def pre_order(self, root):
        if not root:
            self.tree.right = TreeNode(root.val)
            self.tree = self.tree.right
            self.pre_order(root.left)
            self.pre_order(root.right)
