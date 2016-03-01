#!/usr/bin/env python
#-*- coding: utf-8 -*-

# from functools import partial

COLORS = {
    'nc': '\033[0m',
    'orange': '\033[0;33m',
    'green': '\033[0;32m',
    'red': '\033[0;31m',
    'blue': '\033[0;34m',
    'grey': '\033[0;90m'
}

def colorize(text, color):
    return "{0}{1}{2}".\
        format(
            COLORS.get(color),
            text,
            COLORS.get('nc')
        )

for k, v in COLORS.iteritems():
    definition = "def {0}(text): return colorize(text, \'{0}\')".format(k)
    exec definition