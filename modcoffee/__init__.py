'''
Organize the modcoffee package.

Contains:
    modcoffee.graph (subpackage)
    modcoffee.component (subpackage)

    modcoffee.components (magic dictionary of registered components)
'''

import modcoffee.graph as graph
import modcoffee.profiling as profiling

import psutil
import requests

# pylint: disable=invalid-name

components = {}

def start_component():
    '''
    Create a component for the application to run.
    TODO do some magic to track the right information for registering the
        component into the Graph

    Usage: (within an application)

    mc.start_component()

    ... application code ...

    '''
    return graph.Component()
