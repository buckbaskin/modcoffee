'''
The modcoffee.graph subpackage

These methods and classes (modcoffee.graph.Graph) are used to manage the
application configuration via a logical graph of components
(modcoffee.graph.Component).
'''
class Graph(object):
    '''
    A class to represent the logical graph of application Components
    '''
    def __init__(self):
        self.components = {}

    def register_component(self, component_id, docker_run_args):
        '''
        Register an application component into the graph, with the arguments to
        run it as a docker instance
        '''
        self.components[component_id] = docker_run_args

    def build_master(self):
        '''
        Write the master application manager file

        Returns True if the master file was successfully written.
        '''
        return True

class Component(object):
    '''
    Individual executable within an application Graph
    '''
    def __init__(self):
        pass
