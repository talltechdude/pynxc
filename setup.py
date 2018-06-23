#!/usr/bin/env python
# -*- coding: utf8 -*-

from setuptools import setup

setup(name='pynxc',
    version='0.1.7',
    description='A Python to NXC Converter for programming '
                  'LEGO MINDSTORMS Robots',
    author='Brian Blais',
    author_email='bblais@bryant.edu',
    maintainer='Marek Šuppa',
    maintainer_email='marek@suppa.sk',
    url='https://github.com/xlcteam/pynxc',
    packages=['pynxc'],

    data_files=[
        ('tests', ['pynxc/tests/tests.py']),
		('pynxc', ['pynxc/defs.h']),
        ('pynxc/nxc/darwin', ['pynxc/nxc/darwin/nbc']),
        ('pynxc/nxc/darwin', ['pynxc/nxc/darwin/nxtcom'])
        ],

    entry_points = {
        'console_scripts': [
          'pynxc = pynxc:main'
        ]
    }
)
