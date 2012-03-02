#!/usr/bin/env python3

def wagodict2codedict(wagodict, codedict):
    '''
    >>> import yaml
    >>> tests = yaml.load(open('test/wagodict2codedict.yaml').read())
    >>> for t in tests:
    ...  actual = wagodict2codedict(t['wagodict'], t['codedict'])
    ...  assert actual == t['expected']

    # ...  print (actual)
    # ...  print (t['expected'])
    '''
    replacementRules = {k:v for k,v in wagodict.items() if k != 'wago'}
    replacementTargets = [k for k in codedict if k != 'code']

    dstCodeDict = codedict.copy()
    for k, v in replacementRules.items():
        if k in replacementTargets:
            dstCodeDict['code'] = dstCodeDict['code'].replace(k, v)
            dstCodeDict.pop(k)
        else:
            pass
    return dstCodeDict

if __name__ == '__main__':
    import doctest
    doctest.testmod()
