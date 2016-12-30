import modcoffee.profiling as mcp

def test_cpu():
    assert mcp.cpu_total() >= mcp.cpu_available()

def test_mem():
    assert mcp.mem_total() >= mcp.mem_available()

def test_disk():
    assert mcp.disk_total() >= mcp.disk_available()