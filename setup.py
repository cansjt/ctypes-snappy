#!/usr/bin/env python

from distutils.core import setup

setup(
    name="ctypes-snappy",
    description="Python ctypes interface to Google's libsnappy compression.",
    long_description="""
About ctypes-snappy
===================

This module provides an interface to the lightweight snappy compression
library:

http://code.google.com/p/snappy/

As it uses ctypes to provide a Python interface, rather then the Python API,
it is suitable for use with PyPy.  If you don't need to use PyPy, then you
will likely be just as happy using the python-snappy library:

http://pypi.python.org/pypi/python-snappy

The usage is a straightfoward copy of the gzip package:

| import snappy
| compressed = snappy.compress('abba' * 100)
| uncompressed = snappy.uncompress(compressed)
 
""",
    classifiers=['Development Status :: 5 - Production/Stable',
                 'Topic :: Software Development :: Libraries',
                 'Topic :: System :: Archiving :: Compression',
                 'License :: OSI Approved :: BSD License',
                 'Intended Audience :: Developers',
                 'Intended Audience :: System Administrators',
                 'Operating System :: POSIX',
                 'Programming Language :: Python :: 2.5',
                 'Programming Language :: Python :: 2.6',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.0',
                 'Programming Language :: Python :: 3.1',
                 'Programming Language :: Python :: 3.2',
                 ],
    author="Russell Power",
    author_email="power@cs.nyu.edu",
    license="BSD",
    version="1.02",
    url="http://rjpower.org/browse.cgi/ctypes-snappy",
    py_modules=['snappy'],
)
