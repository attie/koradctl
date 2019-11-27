#!/usr/bin/env python

from setuptools import setup

setup(
    name='koradctl',
    version=0.1,
    description='Control utility for Korad / Tenma power supplies',
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
