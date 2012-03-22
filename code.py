#!/usr/bin/env python3
import yaml
from Community import Community
from walk import walk
from wagopath2filepath import wagopath2filepath
from CodeWriter import CodeWriter

def code(wagofile):
    '''
    >>> tests = yaml.load(open('test/code.yaml').read())
    >>> for t in tests:
    ...  actual = code(t['wagofile'])
    ...  assert actual == t['expected']

    #...  print (actual)
    #...  print (t['expected'])

    '''
    com = Community()
    filepath = wagopath2filepath(wagofile)
    baby = yaml.load(open(filepath).read())
    walk(baby, com.bring_up)
    print (yaml.dump(baby))
    writer = CodeWriter()
    walk(baby, writer.write)
    print (writer.result)
    return baby

if __name__ == '__main__':
    import doctest
    doctest.testmod()
