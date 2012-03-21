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
        ...  writer.write(t['codedict'], depth=t['depth'])
        ...  print (t['codedict'])
        ...  print (t['expected'])
        ...  #assert t['codedict'] == t['expected']
        '''
        assert 'depth' in kwargs
        indent = kwargs['depth'] * '    '
        assert 'code' in codedict
        assert 1 == len(codedict), str(codedict)
        self.result += indent + codedict['code'].replace('\n', '\n' + indent)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
