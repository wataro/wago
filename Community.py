#!/usr/bin/env python3
import yaml
from wagopath2filepath import wagopath2filepath
from wagodict2codedict import wagodict2codedict

class Community:
    def bring_up(self, wagodict):
        '''
        >>> com = Community()
        >>> tests = yaml.load(open('test/Community.bring_up.yaml').read())
        >>> for t in tests:
        ...  com.bring_up(t['wagodict'])
        ...  assert t['wagodict'] == t['expected']

        #...  print (t['wagodict'])
        #...  print (t['expected'])
        '''
        filepath = wagopath2filepath(wagodict['wago'])
        code = yaml.load(open(filepath).read())
        assert code
        assert isinstance( code, list), str(code)
        codedict = code[0]
        wagodict2codedict(wagodict, codedict)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
