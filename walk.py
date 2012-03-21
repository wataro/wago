#!/usr/bin/env python3

# 入れ子になっているリストを再帰的にたどりながら何かする
def walkBody(data, func):
    for i in data:
        if isinstance(i, list):
            walkBody(i, func)
        else:
            func(i)

def walk(data, func):
    walkBody(data, func)

