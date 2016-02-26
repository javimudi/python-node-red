#!/usr/bin/env python
#-*- coding: utf-8 -*-

from functools import partial

COLOURS = {
    'nc': '\033[0m',
    'orange': '\033[0;33m',
    'green': '\033[0;32m',
    'red': '\033[0;31m',
    'blue': '\033[0;34m',
    'grey': '\033[0;90m'
}

def colourize(text):
    __colour__ = inspect.stack()[0][3]
    return "{0}{1}{2}".\
        format(
            COLOURS.get(__colour__),
            text,
            COLOURS.get('nc')
        )

for k, v in COLOURS.iteritems():
    pass

orange = blue = red = grey = colourize

