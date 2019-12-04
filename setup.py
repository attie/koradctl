#!/usr/bin/env python

import re
from setuptools import setup

class PackageMeta:
    def __init__(self):
        self.load_long_description()
        self.load_package_info()

    def read_file(self, filename: str) -> str:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()

    def load_long_description(self):
        self.long_description = self.read_file('./README.md')

    def load_package_info(self):
        f = self.read_file('./koradctl/package.py')
        d = {}

        for line in f.split('\n'):
            # match all top level assignments (no indentation)
            match = re.search(r'^(?P<k>[^ =]+) *= *[\'"](?P<v>.+)[\'"] *$', line, re.M)

            if match is None:
                continue

            match = match.groupdict()

            k, v = match['k'], match['v']
            d[k] = v

        self.package_info = d

m = PackageMeta()

setup(
    name=m.package_info['proj_name'],
    version=m.package_info['version'],
    description='Control utility for Korad / Tenma power supplies',
    long_description=m.long_description,
    long_description_content_type='text/markdown',
    author='Attie Grande',
    author_email='attie@attie.co.uk',
    url='https://github.com/attie/koradctl',
    license='BSD-3-Clause',
    packages=[ 'koradctl' ],
    install_requires=[
        'pyserial',
    ],
    entry_points={
        'console_scripts': [
            'koradctl = koradctl.__main__:cli',
        ]
    },
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Manufacturing',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'License :: Freely Distributable',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Embedded Systems',
        'Topic :: Utilities',
    ],
)
