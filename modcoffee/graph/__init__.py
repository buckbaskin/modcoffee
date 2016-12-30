'''
The modcoffee.graph subpackage

These methods and classes (modcoffee.graph.Graph) are used to manage the
application configuration via a logical graph of components
(modcoffee.graph.Component).
'''

class Graph(object):
    def __init__(self):
        pass

    def register_component(self, component_id, docker_run_args):
        pass

    def build_master(self):
        return True

class Component(object):
    def __init__(self):
        pass
