#!/usr/bin/env python3
import os

def new (filename, keywords = []):
    '''
    あたらしくwagoファイルをつくる。
    wagoファイルは、相対パス名。
    フォルダの区切り文字は、OSの依存をなくすため、'.'(ピリオド)。
    '''
    text  = 'code : |\n'
    text += '  /* write code here */\n'
    for kw in keywords:
        assert (kw in filename)
        text += kw + ' : \n'
    else:
        text += 'キーワード : \n'
    pathList = filename.split('.')
    if '.wago' == filename[-len('.wago'):]:
        pathList = filename[:-len('.wago')].split('.')
    path = os.path.join(*pathList) + '.wago'
    print ('Create ' + path)
    open(path, 'w').write(text)
