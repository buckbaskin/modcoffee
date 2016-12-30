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

from contextlib import contextmanager

# pylint: disable=invalid-name

components = {}

@contextmanager
def start_component(graph, component_id):
    '''
    Create a component for the application to run.
    TODO do some magic to track the right information for registering the
        component into the Graph

    Usage: (within an application)

    with mc.start_component():

        ... application code ...

    '''
    # __enter__ code
    print('Start building the component')
    docker_parameters = {}

    components = graph.components

    yield docker_parameters
    # __exit__ code
    print('Complete building the component')
    print('start_component(): post-parameters %s' % (docker_parameters,))
    graph.register_component(component_id, docker_parameters)

print('end of import modcoffee')