#!/usr/bin/env python3
import yaml
from Community import Community
from walk import walk
from wagopath2filepath import wagopath2filepath

def code(wagofile):
    '''
    >>> tests = yaml.load(open('test/code.yaml').read())
    >>> for t in tests:
    ...  actual = code(t['wagofile'])
    ...  print (actual)
    ...  print (t['expected'])
    #...  assert actual == t['expected']
    '''
    com = Community()
    filepath = wagopath2filepath(wagofile)
    baby = yaml.load(open(filepath).read())
    walk(baby, com.bring_up)
    return baby

if __name__ == '__main__':
    import doctest
    doctest.testmod()
