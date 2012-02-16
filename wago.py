#!/usr/bin/env python3
import yaml

EXTENSION = '.wago'

def load (filename):
    contents = '%YAML 1.1\n'
    contents += '---\n'
    contents += open(filename).read()
    return yaml.load(contents)

def showlist ():
    import os
    filelist = [f for f in os.listdir('.') if EXTENSION == f[-len(EXTENSION):]]
    for f in filelist:
        print (f)
        print (load (f))

# 一つの ctkl ファイルとその名前の辞書をもらって、解釈する
def interpret (ctklFile, nameDict):
#    print (ctklFile, nameDict) # for debug
    whole = yaml.load(open(ctklFile).read())
    pseudonym = whole.get('仮名') # if '仮名' is not exist, return None
    code = whole['コード']
    if not pseudonym:
        return code
    assert (len(nameDict.keys()) == len(pseudonym))
    for n in nameDict:
        assert(n in pseudonym)
        code = code.replace(n, nameDict[n])
    return code
        
# 一つの yaml のノードとオプションでインデント幅をもらって、解釈する
def interpretNode (node, indent=''):
    result = ''
    if isinstance(node, dict):
        assert(len(node.keys()) == 1)
        for ctklFile, nameDict in node.items():
            result = interpret(ctklFile, node[ctklFile])
    else:
        result = interpret(node, {})
    return indent + result.replace('\n', '\n' + indent)

class Interpreter:
    def __init__(self):
        self.result = ''
        self.indent = '   '
    def do(self, node, depth):
        self.result += interpretNode(node, self.indent * depth) + '\n'

# 入れ子になっている辞書のリストを再帰的にたどりながら何かする
def walkBody(yamlCode, func, depth=0):
    for i in yamlCode:
        if isinstance(i, list):
            walkBody(i, func, depth+1)
        else:
            func(i, depth)

def walk(yamlData, func):
    walkBody(yamlData['コード'], func)

TEMPLATE = '''
仮名 :
  -
コード : |
    
'''
def generate_ctkl(new_ctkl_file):
    'ctkl のテンプレートを生成する'
    open(new_ctkl_file, 'w').write(TEMPLATE[1:])

def main(ctklFile):
    'ctkl のメイン処理'
    i = Interpreter()
    walk(load(ctklFile), i.do)
    return i.result

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    subparser = parser.add_subparsers()

    run_parser = subparser.add_parser('run')
    run_parser.add_argument('ctkl_file')

    gen_parser = subparser.add_parser('generate')
    gen_parser.add_argument('new_ctkl_file')

    results = parser.parse_args()
    if hasattr(results, 'ctkl_file'):
        print (main(results.ctkl_file))
    if hasattr(results, 'new_ctkl_file'):
        generate_ctkl(results.new_ctkl_file)

