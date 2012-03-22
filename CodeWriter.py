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
        ...  #print (writer.result)
        ...  #print (t['expected'])
        ...  assert writer.result == t['expected'], (writer.result, t['expected'])
        '''
        assert 'depth' in kwargs
        indent = kwargs['depth'] * '    '
        assert 'code' in codedict
        assert 1 == len(codedict), str(codedict)
        code = indent + codedict['code'].replace('\n', '\n' + indent)
        code = code.rstrip(' ')
        self.result += code

if __name__ == '__main__':
    import doctest
    doctest.testmod()
