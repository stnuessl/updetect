#!/usr/bin/env bash

#
# Repository file layout:
#   .gitignore
#   LICENSE
#   Makefile
#   README.rst
#   pyproject.toml
#   src/updetect/__init__.py
#   src/updetect/__main__.py
#   tests/test-updetect.py
#   tests/test-updetect.sh
#

PYMODULE="python -m updetect"
PYMODPATH="src/updetect"

if [[ ! $(${PYMODULE} . --name ${PYMODPATH}/__main__.py | wc -l) -eq 1 ]]; then
    printf "error: test 1 failed\n"
    exit 1
fi

if [[ ! $(${PYMODULE} . --name ${PYMODPATH}/*.py --limit 1 | wc -l) -eq 1 ]]; then
    printf "error: test 2 failed\n"
    exit 1
fi

if [[ ! $(${PYMODULE} . --name src/updetect/*.py | wc -l) -eq 2 ]]; then
    printf "error: test 3 failed\n"
    exit 1
fi

if [[ ! $(${PYMODULE} . --name src/updetect/*.[!p][!y] | wc -l) -eq 0 ]]; then
    printf "error: test 4 failed\n"
    exit 1
fi

if [[ ! $(${PYMODULE} . --name * --limit 1 | wc -l) -eq 1 ]]; then
    printf "error: test 5 failed\n"
    exit 1
fi

if [[ ! $(${PYMODULE} . --name * --limit 3 | wc -l) -eq 3 ]]; then
    printf "error: test 6 failed\n"
    exit 1
fi

if [[ ! $(${PYMODULE} . --name "LICENSE") =~ .*/LICENSE ]]; then
    printf "error: test 7 failed\n"
    exit 1
fi

if [[ ! $(${PYMODULE} tests/ --name *.py *.rst --recursive | wc -l) -eq 2 ]]; then
    printf "error: test 8 failed\n"
    exit 1
fi

if [[ $(${PYMODULE} --name *.c) ]]; then
    printf "error: test 9 failed\n"
    exit 1
fi

if [[ $(${PYMODULE} --name main.c ) == '\n' ]]; then
    printf "error: test 10 failed\n"
    exit 1
fi

if [[ $(${PYMODULE} --name main.c --json) == '[]\n' ]]; then
    printf "error: test 11 failed\n"
    exit 1
fi
