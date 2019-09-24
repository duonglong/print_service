from setuptools import setup

import re

version = False
with open('app/server.py', 'r') as f:
    version = re.search(
        r"^__version__\s*=\s*'(.*)'",
        f.read(),
        re.M).group(1)

with open('README.md', 'rb') as f:
    long_desc = f.read().decode('utf-8')

setup(
    name='pdfprinter',
    packages=['app', 'tools'],
    entry_points={
        'console_scripts': ['start_printservice = app.server:main']
    },
    version=version,
    description='Print server to be run on machine which can connect to printers',
    long_description=long_desc,
    author='LongDT'
)
