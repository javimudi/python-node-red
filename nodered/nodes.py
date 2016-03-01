#!/usr/bin/env python
#-*- coding: utf-8 -*-

import requests

class Nodes(object):
    def __init__(self, host):
        self.host = host

    def __iter__(self):
        url = "{0}/flows".format(self.host)
        response = requests.get(url)
        if response.status_code == 200:
            for node in response.json():
                yield node


    def __get__(self, value):
        for _tab in self:
            if _tab['id'] == value:
                yield _tab
            elif _tab['label'] == value:
                yield _tab
            else:
                yield list()
