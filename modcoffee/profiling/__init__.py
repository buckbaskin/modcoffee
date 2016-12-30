import psutil

# TODO check to see how this works with docker allocation

def cpu_total():
    '''
    Returns the number of logical cpus in the system

    >>> isinstance(cpu_total(), int)
    True
    '''
    return psutil.cpu_count(logical=True)

def cpu_available():
    '''
    Equivalent to modcoffee.profiling.cpu_total
    '''
    # This is the same as total because of process switching. It might make
    #   sense to have this track the Docker cpu allocation
    return psutil.cpu_count()

def mem_total():
    return psutil.virtual_memory().total

def mem_available():
    return psutil.virtual_memory().available

def disk_total():
    return psutil.disk_usage('/').total

def disk_available():
    return psutil.disk_usage('/').free