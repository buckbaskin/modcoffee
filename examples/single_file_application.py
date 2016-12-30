import modcoffee as mc

from modcoffee import start_component
from modcoffee.graph import Graph

app = Graph()

with start_component(app, 'load balancer') as parameters:
    print('Within context')
    print('Parameters v1: %s' % (parameters,))
    parameters['name'] = 'abc/loader'
    print('Parameters v2: %s' % (parameters,))

with start_component(app, 'web server') as parameters:
    parameters['name'] = 'abc/server'

print('Components: %s' % (mc.components,))