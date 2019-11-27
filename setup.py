#!/usr/bin/env python

from setuptools import setup

import koradctl as me

long_description = (
    "koradctl is a simple command line utility and python library for "
    "controlling Korad / Tenma power supplies via their RS232 or USB "
    "interfaces."
)

setup(
    name=me.__proj_name__,
    version=me.__version__,
    description='Control utility for Korad / Tenma power supplies',
    long_description=long_description,
    author='Attie Grande',
    author_email='attie@attie.co.uk',
    url='https://github.com/attie/koradctl',
    packages=[ 'koradctl' ],
    install_requires=[
        'pyserial',
    ],
    entry_points={
        'console_scripts': [
            'koradctl = koradctl.__main__:cli',
        ]
    },
    python_requires='>=3.5',
)
