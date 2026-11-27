#!/usr/bin/env python

# -----------------------------------------------------------------------------
# Copyright (c) 2013, The Deblur Development Team.
#
# Distributed under the terms of the BSD 3-clause License.
#
# The full license is in the file LICENSE, distributed with this software.
# -----------------------------------------------------------------------------
from setuptools import setup
from glob import glob
import re
import ast

# version parsing from __init__ pulled from Flask's setup.py
# https://github.com/mitsuhiko/flask/blob/master/setup.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('deblur/__init__.py', 'rb') as f:
    hit = _version_re.search(f.read().decode('utf-8')).group(1)
    __version__ = str(ast.literal_eval(hit))


classes = """
    Development Status :: 4 - Beta
    License :: OSI Approved :: BSD License
    Topic :: Scientific/Engineering :: Bio-Informatics
    Topic :: Software Development :: Libraries :: Application Frameworks
    Topic :: Software Development :: Libraries :: Python Modules
    Programming Language :: Python
    Programming Language :: Python :: 3.8
    Programming Language :: Python :: Implementation :: CPython
    Operating System :: POSIX :: Linux
    Operating System :: MacOS :: MacOS X
"""

long_description = ("Deblur: a greedy deconvolution algorithm based on known "
                    "read error profiles")

classifiers = [s.strip() for s in classes.split('\n') if s]

setup(name='deblur',
      version=__version__,
      long_description=long_description,
      license="BSD",
      description='Deblur',
      author="Deblur development team",
      author_email="amnonim@gmail.com",
      url='https://github.com/biocore/deblur',
      test_suite='nose.collector',
      packages=['deblur', 'deblur.support_files', 'deblur.test'],
      package_data={
        'deblur.support_files': ['artifacts.fa', '88_otus.fasta'],
        'deblur.test.data': ['*'],
      },
      scripts=glob('scripts/*'),
      extras_require={'test': ["pytest", "pep8"],
                      'doc': ["Sphinx", "sphinx-bootstrap-theme"]},
      install_requires=['click', 'numpy',
                        'scikit-bio',
                        'biom-format',
                        'h5py', 'scipy'],
      classifiers=classifiers
      )
