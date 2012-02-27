#!/usr/bin/env python3
import os
import yaml

def wagoValue2Path (wagoValue):
    '''
    wago: キーの値 data['wago'] 一つをファイルパスに変換する
    >>> actual = wagoValue2Path('test.code1')
    >>> expected = 'test/code1.wago'
    >>> actual == expected
    True
    >>> actual = wagoValue2Path('test.code1.wago')
    >>> expected = 'test/code1.wago'
    >>> actual == expected
    True
    '''
    path = wagoValue.split('.')
    if 'wago' == path[-1]:
        path.pop(-1)
    path = os.path.join(*path) + '.wago'
    return path

def code1 (wagoData):
    '''
    1個の wago ファイルの wago: キーをできるだけ code: キーに変換する
    >>> srcWago = yaml.load(open('test/code1.wago').read())
    >>> actual = code1(srcWago)
    >>> expected = yaml.load(open('test/expected/code1.wago').read())
    >>> actual == expected
    True
    '''
    wagoTarget = wagoData['wago']
    path = wagoTarget.split('.')
    path = os.path.join(*path) + '.wago'
    print (path)
    if os.path.exists(path):
        srcWago = yaml.load(open(path).read())
        print (srcWago)
        dstCode = srcWago['code']
        for keyword in wagoData:
            if keyword != 'wago':
                assert (keyword in srcWago)
                print (keyword, keyword in srcWago)
                dstCode = dstCode.replace(keyword, wagoData[keyword])
        result = [{'code': dstCode}]
        print (result)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
