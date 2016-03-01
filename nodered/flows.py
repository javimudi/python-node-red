#!/usr/bin/env python
#-*- coding: utf-8 -*-

import requests
import json
from utils import naked, pretty

class Flows(object):
    def __init__(self, host, strategy):
        self.host = host
        self.strategy = strategy

    def __iter__(self):
        url = "{0}/flows".format(self.host)
        response = requests.get(url)
        if response.status_code == 200:
            for node in response.json():
                if "type" in node.keys():
                    if node['type'] == 'tab':
                        yield self[node.get('id')]
        
        elif response.status_code == 401:
            raise NotImplementedError("NotAuthorized")
        else:
            raise NotImplementedError()

    @property
    def sheets(self):
        for sheet in self:
            yield sheet['label']

    def __getitem__(self, value):
        url = "{0}/flow/{1}".format(self.host, value)
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            raise KeyError(value)
        elif response.status_code == 401:
            raise NotImplementedError("NotAuthorized")
        else:
            raise NotImplementedError()


    def update(self, flow):
        baseurl = "{0}/flow".format(self.host)
        _label = flow.get('label')    

        if _label:
            if _label in self.sheets:
                # First delete
                url = baseurl + "/{0}".format(flow.get('id'))
                response = requests.delete(
                    url=url,
                    headers={"content-type": "application/json"})
            
            # Then add
            response = requests.post(
                url=baseurl, 
                json=naked(flow),
                headers={"content-type": "application/json"})

            return int(response.status_code/100) % 2 == 0


        else:
            exceptionmsg = "label not in {0}".format(pretty(flow))
            raise KeyError(exceptionmsg)



    def __add__(self, node):
        self.update(node)

    def __str__(self):
        return pretty(self)


