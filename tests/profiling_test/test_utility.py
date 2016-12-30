import modcoffee.profiling as mcp

def test_cpu_total():
    assert isinstance(mcp.cpu_total(), int)

def test_cpu_available():
    assert isinstance(mcp.cpu_available(), int)

def test_mem_total():
    assert isinstance(mcp.mem_total(), int)

def test_mem_available():
    assert isinstance(mcp.mem_available(), int)

def test_disk_total():
    assert isinstance(mcp.disk_total(), int)

def test_disk_available():
    assert isinstance(mcp.disk_available(), int)