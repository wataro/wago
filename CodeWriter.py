#!/usr/bin/env python3

class CodeWriter:
    def write(self, wagodict, **kwargs):
        '''
        >>> import yaml
        >>> writer = CodeWriter()
        >>> tests = yaml.load(open('test/CodeWriter.write.yaml').read())
        >>> for t in tests:
        ...  writer.write(t['wagodict'])
        ...  print (t['wagodict'])
        ...  print (t['expected'])
        ...  #assert t['wagodict'] == t['expected']
        '''
        pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
