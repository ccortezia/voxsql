import os
import importlib
import textwrap


HERE = os.path.normpath(os.path.join(os.path.abspath(__file__), os.path.pardir))


def load_case_modules(package, prefix, basedir=None):

    basedir = basedir if basedir is not None else HERE

    basenames = [
        os.path.splitext(f)[0]
        for f in os.listdir(basedir)
        if f.startswith(prefix)
    ]

    return {
        basename: importlib.import_module(f'.{basename}', package=package)
        for basename in basenames
    }


def codeblock(text):
    stripped = text.lstrip('\n')
    dedented = textwrap.dedent(stripped)
    return dedented
