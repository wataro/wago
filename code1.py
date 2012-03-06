#!/usr/bin/env python3
import os
import yaml
from wagopath2filepath import wagopath2filepath

class WagoItem: pass
class CodeItem: pass
def getItemType (item):
    '''
    wago: キーのある辞書なら WagoItem オブジェクトが返る。
    code: キーのある辞書なら CodeItem オブジェクトが返る。
    >>> tests = yaml.load(open('test/getItemType.yaml').read())
    >>> for t in tests:
    ...  actual = getItemType(t['test']).__class__.__name__
    ...  assert actual == t['expected']
    '''
    if 'wago' in item:
        assert (not 'code' in item)
        return WagoItem()
    else if 'code' in item:
        assert (not 'wago' in item)
        return CodeItem()
    else return None

def WagoItem2CodeItem (wagoItem):
    '''
    WagoItem を CodeItem に変換する
    >>> tests = yaml.load(open('test/WagoItem2CodeItem.yaml').read())
    >>> for t in tests:
    ...  actual = WagoItem2CodeItem(t['test']['wago'])
    ...  assert actual == t['expected']
    '''
    path = wagoValue2Path(wagoitem)
    assert(os.path.exists(path))
    wagoItemKeywords = [k for k in wagoItem if not 'wago' == k]
    srcWago = yaml.load(open(path).read())
    for i in srcWago:
        itemType = getItemType(i)
        if isinstance(itemType, CodeItem):
            keywords = [k for k in i if not 'code' == k]
            if wagoItemKeywords == keywords:
                for k in keywords:
                    i['code'] = i['code'].replace(k, wagoItem[k])
    return srcWago

def code1 (wagoData):
    '''
    1個の wago ファイルの wago: キーをできるだけ code: キーに変換する
    >>> srcWago = yaml.load(open('test/code1.wago').read())
    >>> actual = code1(srcWago)
    >>> expected = yaml.load(open('test/expected/code1.wago').read())
    >>> actual == expected
    True
    '''
    for i in wagoData:
        itemType = getItemType(i)
        if isinstance(itemType, WagoItem):
            path = wagopath2filepath(i)
            assert(os.path.exists(path))
            print (path)
            srcWago = yaml.load(open(path).read())

    wagoTarget = wagoData['wago']
    path = wagoTarget.split('.')
    path = os.path.join(*path) + '.wago'
    print (path)
    if os.path.exists(path):
        srcWago = yaml.load(open(path).read())
        print (srcWago)
        dstCode = srcWago['code']
        for keyword in wagoData:
            if keyword != 'wago':
                assert (keyword in srcWago)
                print (keyword, keyword in srcWago)
                dstCode = dstCode.replace(keyword, wagoData[keyword])
        result = [{'code': dstCode}]
        print (result)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
