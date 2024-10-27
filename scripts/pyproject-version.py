#!/usr/bin/env python

import sys
import tomllib
import updetect

if __name__ == '__main__':
    files = updetect.find('.', 'pyproject.toml', recursive=False, limit=1)
    if not files:
        print('error: failed to detect "pyproject.toml" file', file=sys.stderr)
        sys.exit(1)

    with open(files[0], 'rb') as tomlfile:
        data = tomllib.load(tomlfile)

        version = data['project']['version']
        print(f'{version}', file=sys.stdout)

    sys.exit(0)

