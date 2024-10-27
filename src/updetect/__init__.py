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

import glob
import os

def find(paths: list[str] | str,
         names: list[str] | str,
         recursive: bool=True,
         limit: int=-1) -> list[str]:
    """Detect matching files and directories by ascending to the root directory

    Parameters
    ----------
    paths : list[str], str
        Paths used as entry points for starting the search.

    names : list[str], str
        File name patterns used for searching matching elements.

    recursive : bool
        Walk the file tree upwards searching every directory encountered
        for matching elements.

    limit : int
        The maximum amount of elements returned by the search.


    Returns
    -------
    list
        A list of strings with matching file system elements.


    Raises
    ------
        No exceptions are raised by this function
    """

    result = []

    if not isinstance(paths, list):
        paths = [paths]

    if not isinstance(names, list):
        names = [names]

    if limit < 0:
        limit = -1

    for item in paths:
        path = os.path.abspath(item)

        if not os.path.isdir(path):
            path = os.path.dirname(path)

        while path:
            for name in names:
                pattern = os.path.join(path, name)
                values = glob.glob(pattern, include_hidden=True)

                result.extend(values)

            if limit >= 0 and len(result) >= limit:
                return result[0:limit]

            if not recursive:
                break

            # The root directory is its own parent
            parent = os.path.dirname(path)
            if parent == path:
                break

            path = parent


    return result

