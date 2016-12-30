import modcoffee.profiling as mcp

def test_cpu_total():
    assert isinstance(mcp.cpu_total(), int)