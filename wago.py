#!/usr/bin/env python3
from new import new
from code import code

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    subparser = parser.add_subparsers()

    new_parser = subparser.add_parser('new',
                                      help=new.__doc__)
    new_parser.add_argument('newWagoFile', help='ファイル名')
    new_parser.set_defaults(func=new)

    code_parser = subparser.add_parser('code',
                                      help=code.__doc__)
    code_parser.add_argument('codeWagoFile', help='ファイル名')
    code_parser.set_defaults(func=code)

    args = parser.parse_args()

    print (args)

    if hasattr(args, 'newWagoFile'):
        args.func(args.newWagoFile)
    elif hasattr(args, 'codeWagoFile'):
        args.func(args.codeWagoFile)
