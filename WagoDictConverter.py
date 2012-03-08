#!/usr/bin/env python3
import yaml
from wagodict2codedict import wagodict2codedict

class WagoDictConverter:
    def __init__(self, wagodict):
        self.wagodict = wagodict

    def do(self, codedict):
        '''
        >>> from walk import walk
        >>> import yaml
        >>> tests = yaml.load(open('test/WagoDictConverter.yaml').read())
        >>> for t in tests:
        ...  wc = WagoDictConverter(t['wagodict'])
        ...  walk(t['codedictlist'], wc.do)
        ...  assert t['wagodict'] == t['expected']

        # ...  print (t['wagodict'])
        # ...  print (t['expected'])
        '''
        wagodict2codedict(self.wagodict, codedict)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
