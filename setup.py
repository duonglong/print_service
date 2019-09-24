from setuptools import setup

import re

__author__ = 'Long Duong <duongthanhlong93@gmail.com>'
__version__ = '1.0.1'


with open('README.md', 'rb') as f:
    long_desc = f.read().decode('utf-8')

setup(
    name='pdfprinter',
    packages=['app', 'tools'],
    entry_points={
        'console_scripts': ['start_pdfprinter = app.server:main', 'stop_pdfprinter = app.server:shutdown']
    },
    version=__version__,
    description='Print server to be run on machine which can connect to printers',
    long_description=long_desc,
    author=__author__
)
