#!/usr/bin/env python
#
# The MIT License (MIT)
#
# Copyright (c) 2024 Steffen Nuessle
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

if __name__ == '__main__':
    import argparse
    import json
    import os
    import sys

    import updetect

    parser = argparse.ArgumentParser(
        description=(
            'Detect matching files and directories by ascending to the root '
            'directory'
        )
    )
    parser.add_argument(
        'path',
        help=(
            'A path specifying the starting point of the search. Default is '
            'the current working directory.'
        ),
        default=[os.getcwd()],
        nargs='*',
        metavar='Path',
        type=str
    )
    parser.add_argument(
        '--json',
        help='Generate JSON output',
        action='store_true',
        required=False,
        default=False
    )
    parser.add_argument(
        '--limit',
        help='Stop search after the specified limit of results is reached',
        metavar='Integer',
        default=-1,
        required=False,
        type=int
    )
    parser.add_argument(
        '--name',
        help='Search for files using the specified glob patterns.',
        nargs='+',
        metavar='Glob',
        required=True,
        type=str
    )
    parser.add_argument(
        '-o',
        help=(
            'Write the generated output to specified file. If no file is '
            'specified, the output will be written to standard output.'
        ),
        default=sys.stdout,
        metavar='File',
        required=False,
        type=lambda x: open(x, 'w'),
    )
    parser.add_argument(
        '--recursive', '-r',
        help='Recursively search parent directories',
        action='store_true',
        required=False,
        default=False
    )
    parser.add_argument(
        '--sort', '-s',
        help='Sort the generated output',
        action='store_true',
        required=False,
        default=False
    )

    args = parser.parse_args()

    result = updetect.find(args.path, args.name, args.recursive, args.limit)

    if args.sort:
        result = sorted(result)

    if args.json:
        dumper = lambda x: '{}\n'.format(json.dumps(x, indent=4))
    else:
        dumper = lambda x: '{}\n'.format('\n'.join(x)) if x else ''

    print(dumper(result), end='', file=args.o)

    if result:
        status = 0
    else:
        status = 1

    sys.exit(status)

