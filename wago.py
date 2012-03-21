#!/usr/bin/env python3
from new import new

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    subparser = parser.add_subparsers()

    new_parser = subparser.add_parser('new',
                                      help=new.__doc__)
    new_parser.add_argument('newWagoFile', help='ファイル名')
    new_parser.set_defaults(func=new)

    args = parser.parse_args()
    args.func(args.newWagoFile)
