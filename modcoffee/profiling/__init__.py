'''
The modcoffee.profiling subpackage

These methods are used to identify system properties in order to help run
applications.
'''

import psutil

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

    >>> isinstance(cpu_available(), int)
    True
    '''
    # This is the same as total because of process switching. It might make
    #   sense to have this track the Docker cpu allocation
    return psutil.cpu_count()

def mem_total():
    '''
    Returns the total (used + free) number of bytes available in memory

    >>> isinstance(mem_total(), int)
    True
    '''
    return psutil.virtual_memory().total

def mem_available():
    '''
    Returns the available (free) number of bytes available in memory

    >>> isinstance(mem_available(), int)
    True
    '''
    return psutil.virtual_memory().available

def disk_total():
    '''
    Returns the total (used + free) number of bytes available on disk

    >>> isinstance(disk_total(), int)
    True
    '''
    return psutil.disk_usage('/').total

def disk_available():
    '''
    Returns the available (free) number of bytes available in disk

    >>> isinstance(disk_available(), int)
    True
    '''
    return psutil.disk_usage('/').free
