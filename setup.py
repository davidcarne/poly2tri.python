import os
from setuptools import setup
from distutils.extension import Extension

import sys
if 'setuptools.extension' in sys.modules:
    m = sys.modules['setuptools.extension']
    m.Extension.__dict__ = m._Extension.__dict__

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


CYTHON_SOURCES =  """src/p2t.pyx""".split("\n")

CPP_SOURCES = """poly2tri/common/shapes.cc
poly2tri/sweep/advancing_front.cc
poly2tri/sweep/cdt.cc
poly2tri/sweep/sweep.cc
poly2tri/sweep/sweep_context.cc""".split("\n")

mod_math = Extension(
    "p2t",
    CYTHON_SOURCES + CPP_SOURCES,
    language = "c++"
)

setup(
    name = "poly2tri",
    version = "0.3.3",
    author = "Mason Green",
    description = "A 2D constrained Delaunay triangulation library",
    long_description = read('README'),
    url = "http://code.google.com/p/poly2tri/",

    ext_modules = [mod_math],
    setup_requires = ["cython==0.14.1", "setuptools_cython==0.2.1"],
    install_requires = ["cython==0.14.1"],
)
