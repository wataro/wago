#!/usr/bin/env python3
import os
from wagopath2filepath import wagopath2filepath

def new (filename):
    '''
    あたらしくwagoファイルをつくる。
    wagoファイルは、相対パス名。
    フォルダの区切り文字は、OSの依存をなくすため、'.'(ピリオド)。
    '''
    text  = 'code : |\n'
    text += '  /* write code here */\n'
    text += 'wagoキー : \n'
    text += 'wago : path.to.wagoファイル\n'
    text += 'wagoキー : 値\n'
    path = wagopath2filepath(filename)
    if os.path.exists(path) :
        print ('NOT CREATE')
        print ('    ' + path + ' : already exists')
    else:
        open(path, 'w').write(text)
        print ('CREATE ')
        print ('    ' + path)
