#!/usr/bin/env python3
from wagopath2filepath import wagopath2filepath
from wagodict2codedict import wagodict2codedict

def wagodict2codedict_find(wagodict):
    '''
    >>> import yaml
    >>> tests = yaml.load(open('test/wagodict2codedict_find.yaml').read())
    >>> for t in tests:
    ...  actual = wagodict2codedict_find(t['wagodict'])
    ...  assert actual == t['expected']

    # ...  print (actual)
    # ...  print (t['expected'])
    '''
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
