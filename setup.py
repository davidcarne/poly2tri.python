import os
from setuptools import setup
from distutils.extension import Extension
import Cython
import Cython.Build

import sys

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

from Cython.Distutils import build_ext as build_ext_c

CYTHON_SOURCES =  """src/p2t.pyx""".split("\n")

CPP_SOURCES = """poly2tri/common/shapes.cc
poly2tri/sweep/advancing_front.cc
poly2tri/sweep/cdt.cc
poly2tri/sweep/sweep.cc
poly2tri/sweep/sweep_context.cc""".split("\n")

ext = Extension(
    'p2t',
    sources= CYTHON_SOURCES + CPP_SOURCES,
    language='c++'
)
extensions = Cython.Build.cythonize(ext)

setup(
    name = "poly2tri",
    version = "0.3.3+dcpatch",
    author = "Mason Green",
    description = "A 2D constrained Delaunay triangulation library",
    long_description = read('README'),
    url = "http://code.google.com/p/poly2tri/",

    ext_modules = extensions,
)
