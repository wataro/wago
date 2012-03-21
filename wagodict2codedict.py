#!/usr/bin/env python3

def wagodict2codedict(wagodict, codedict):
    '''
    >>> import yaml
    >>> tests = yaml.load(open('test/wagodict2codedict.yaml').read())
    >>> for t in tests:
    ...  wagodict2codedict(t['wagodict'], t['codedict'])
    ...  actual = t['wagodict']
    ...  print (actual)
    ...  print (t['expected'])
    ...  #assert actual == t['expected']

    '''
    replacementRules = {k:v for k,v in wagodict.items() if k != 'wago'}
    replacementTargets = [k for k in codedict if k != 'code']

    dstCodeDict = codedict.copy()
    for k, v in replacementRules.items():
        if k in replacementTargets:
            dstCodeDict['code'] = dstCodeDict['code'].replace(k, v)
            dstCodeDict.pop(k)
            wagodict.pop(k)
        else:
            pass
    print ('wagodict:', wagodict)
    print ('replacementRules:', replacementRules)
    if len(wagodict) < 1 + len(replacementRules):
        assert 1 == len(wagodict), str(wagodict)
        wagodict = dstCodeDict.copy()

if __name__ == '__main__':
    import doctest
    doctest.testmod()
