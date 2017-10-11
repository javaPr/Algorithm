#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/11 23:04
# @Author  : wangdechang

s = "()[]{}"

stack = []
for s1 in s:
    if len(stack) == 0:
        stack.append(s1)
    else:
        if s1 == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(s1)

        elif s1 == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                stack.append(s1)
        elif s1 == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                stack.append(s1)
        else:
            stack.append(s1)

if len(stack) == 0:
    print(True)



