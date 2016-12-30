import modcoffee as mc

def test_pass():
    assert True

def test_modcoffee_app():
    app = mc.graph.Graph()
    assert app.build_master()
