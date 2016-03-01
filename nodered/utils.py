#!/usr/bin/env python
#-*- coding: utf-8 -*-

def idstripped(node):
    _id = node.get('id')
    if _id:
        del node['id']
        _nodes = node.get('nodes')
        if _nodes:
            for innernode in _nodes:
                innernode = idstripped(innernode)
    else:
        return node
