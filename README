ctypes-snappy
===================

This module provides an interface to the lightweight snappy compression
library:

http://code.google.com/p/snappy/

As it uses ctypes to provide a Python interface, rather then the Python API,
it is suitable for use with PyPy.  If you don't need to use PyPy, then you
will likely be just as happy using the python-snappy library:

http://pypi.python.org/pypi/python-snappy

The usage is a straightfoward copy of the gzip package:

import snappy
compressed = snappy.compress('abba' * 100)
uncompressed = snappy.uncompress(compressed)
 
