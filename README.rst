==============================
updetect - Upwards File Search
==============================

.. contents::


Motivation
==========

Some automation tasks requires the user to detect a specific file in one of the
parent directories of a given path. The **updetect** package provides a flexible
and reusable solution to this kind of problem.


Examples
========

Search a **compile_commands.json** file within a **build** directory in
the current working directory and any of its parent directories with python:

.. code-block:: python

    import json
    import updetect

    files = updetect.find('.', 'build/compile_commands.json', limit=1)
    if files:
        data = json.load(files[0])

        # ...

And with a terminal:

.. code-block:: sh

   file="$(python -m updetect --name build/compile_commands.json --limit 1)"
   echo "${file}"











