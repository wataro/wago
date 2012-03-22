#!/usr/bin/env python3

# 入れ子になっているリストを再帰的にたどりながら何かする
def walkBody(data, func, depth = 0):
    for i in data:
        if isinstance(i, list):
            walkBody(i, func, depth + 1)
        else:
            func(i, depth=depth)

def walk(data, func):
    walkBody(data, func)

