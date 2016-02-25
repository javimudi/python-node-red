#!/usr/bin/env python
#-*- coding: utf-8 -*-

import re
import requests
import json
from flows import Flows
from nodes import Nodes
from auth import LoginStrategy

class RED(object):

    def __init__(self, host="http://localhost:1880", strategy=None):

        self.strategy = strategy
        self.host = host
        self.flows = Flows(host)
        self.nodes = Nodes(host)


    def __iter__(self):
        return self.flows.__iter__()


def main():

    red = RED()

    # Generator 
    for flow in red.flows:
        for node in red.nodes:
            if flow.get('id') is not None and \
                flow.get('id') == node.get('z'):
                print flow, node


if __name__ == '__main__':
    main()



