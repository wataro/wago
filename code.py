#!/usr/bin/env python3
import yaml
from Community import Community
from walk import walk
from wagopath2filepath import wagopath2filepath
from CodeWriter import CodeWriter

def code(wagofile, **kwargs):
    '''
    >>> tests = yaml.load(open('test/code.yaml').read())
    >>> for t in tests:
    ...  actual = code(t['wagofile'])
    ... # print (actual)
    ... # print (t['expected'])
    ...  assert actual == t['expected']
    '''
    com = Community()
    filepath = wagopath2filepath(wagofile)
    baby = yaml.load(open(filepath).read())
    walk(baby, com.bring_up)
    writer = CodeWriter()
    walk(baby, writer.write)
    if 'verbose' in kwargs and kwargs['verbose']:
        print (yaml.dump(baby))
        print (writer.result)
    if 'output_file' in kwargs:
        fp = open(kwargs['output_file'], 'w')
        print (writer.result, file=fp)
        fp.close()
        print ('WRITE: %s' % kwargs['output_file'])

    return baby

if __name__ == '__main__':
    import doctest
    doctest.testmod()
