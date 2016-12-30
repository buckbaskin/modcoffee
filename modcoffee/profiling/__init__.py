import psutil

# TODO check to see how this works with docker allocation

def cpu_total():
    return psutil.cpu_count()

def cpu_available():
    # TODO: check if this is right
    return psutil.cpu_count()

def mem_total():
    return psutil.virtual_memory().total

def mem_available():
    return psutil.virtual_memory().available

def disk_total():
    return psutil.disk_usage('/').total

def disk_available():
    return psutil.disk_usage('/').available