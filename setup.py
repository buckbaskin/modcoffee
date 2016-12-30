#!/usr/bin/env python

# Based on the setup.py from the requests package

import os
import re
import sys

from codecs import open

from setuptools import setup
from setuptools.command.test import test as TestCommand

packages = [
    'modcoffee',
    'modcoffee.graph'
]

requires = []
test_requirements = ['pytest>=2.8.0', 'pytest-cov']

version = '0.0.1'

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()
with open('HISTORY.md', 'r', 'utf-8') as f:
    history = f.read()

setup(
    name='modcoffee',
    version=version,
    description='Application Management for minimizing total failure risk',
    long_description=readme + '\n\n' + history,
    author='Buck Baskin',
    author_email='mobile.wbaskin@gmail.com',
    url='https://github.com/buckbaskin/modcoffee',
    packages=packages,
    package_data={'': ['LICENSE']},
    package_dir={
        'modcoffee': 'modcoffee',
        'modcoffee.graph': 'modcoffee/graph'
    },
    include_package_data=True,
    install_requires=requires,
    license='MIT',
    classifiers=(
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        # 'Programming Language :: Python :: 2.6',
        # 'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.3',
        # 'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
        # 'Programming Language :: Python :: Implementation :: CPython',
        # 'Programming Language :: Python :: Implementation :: PyPy'
    ),
    tests_require=test_requirements
)
