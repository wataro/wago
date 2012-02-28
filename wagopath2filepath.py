#!/usr/bin/env python3
import os
import yaml

def wagopath2filepath (wagoValue):
    '''
    wagoパス data['wago'] 一つをファイルパスに変換する
    >>> tests = yaml.load(open('test/wagopath2filepath.yaml').read())
    >>> for t in tests:
    ...  actual = wagopath2filepath(t['test'])
    ...  assert actual == t['expected']
    '''
    path = wagoValue.split('.')
    if 'wago' == path[-1]:
        path.pop(-1)
    path = os.path.join(*path) + '.wago'
    return path
