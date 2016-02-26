#!/usr/bin/env python
#-*- coding: utf-8 -*-

import requests
import json
from utils import idstripped


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


    def update(self, node):
        url = "{0}/flow".format(self.host)
        _label = node.get('label')
        if _label:
            if _label in self:
                # Update
                url += "/{0}".format(node.get('id'))
                response = requests.post(url, 
                    data=json.dumps(idstripped(node)),
                    headers={"content-type": "application/json"})
            else:
                # Add
                print idstripped(node)
                response = requests.post(url, 
                    data=json.dumps(idstripped(node)),
                    headers={"content-type": "application/json"})

            # print response.__dict__

        else:
            exceptionmsg = "id not in {0}".format(node)
            raise KeyError(exceptionmsg)



    def __add__(self, node):
        self.update(node)



