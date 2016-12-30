import modcoffee.profiling as mcp

def test_cpu():
    mcp.cpu_total() >= mcp.cpu_available()

def test_mem():
    mcp.mem_total() >= mcp.mem_available()

def test_disk():
    mcp.disk_total() >= mcp.disk_available()