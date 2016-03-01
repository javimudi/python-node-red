#!/usr/bin/env python
#-*- coding: utf-8 -*-

import re
import requests
import json
from flows import Flows
from nodes import Nodes
from auth import LoginStrategy
from colours import orange, blue
from utils import pretty

class RED(object):

    def __init__(self, host="http://localhost:1880", strategy=None):

        self.strategy = strategy
        self.host = host
        self.flows = Flows(host, strategy)

    def __str__(self):
        response = ""
        for flow in self.flows:
            response += "\"{0}\" ({1}) -> {2}\n\n".\
                format(blue(flow.get('label')),\
                    orange(flow.get('id')), 
                    pretty(flow.get('nodes'))
                )
        return response

    def update(self, node):
        self.flows.update(node)

def main():
    red = RED()
    for i, flow in enumerate(red.flows):
        if i == 3:
            red.flows.update(flow)
            
    



if __name__ == '__main__':
    main()



