#!/usr/bin/env python3

class CodeWriter:
    def __init__(self):
        self.result = ''
        self.indent = '   '

    def write(self, codedict, **kwargs):
        '''
        >>> import yaml
        >>> writer = CodeWriter()
        >>> tests = yaml.load(open('test/CodeWriter.write.yaml').read())
        >>> for t in tests:
        ...  writer.write(t['codedict'])
        ...  print (t['codedict'])
        ...  print (t['expected'])
        ...  #assert t['codedict'] == t['expected']
        '''
        pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
