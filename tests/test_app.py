import modcoffee as mc
import modcoffee.graph as mcg

import pytest

def test_pass():
    assert True

def test_raises():
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_modcoffee_app():
    app = mc.graph.Graph()
    assert app.build_master()

def test_add_component():
    app = mc.graph.Graph()
    app.register_component('load balancer', {})
    assert 'load balancer' in mc.components

def test_start_component():
    app = mc.graph.Graph()
    assert mc.start_component(app, 'test')
