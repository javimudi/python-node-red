#!/usr/bin/env python
#-*- coding: utf-8 -*-
from distutils.core import setup

setup(name='python-node-red',
      author='Javier Muñoz',
      author_email='javier.munoz.diaz@gmail.com',
      description='Python Node-RED HTTP API Bindings',
      version=u'0.1.1',
      packages=['nodered'],
      requires=['requests'],
      url='http://github.com/javimudi/python-node-red.git'
)

