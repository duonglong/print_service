from distutils.core import setup

setup(
    console=[{'script': 'server.py'}],
    options={'py2exe': {'bundle_files': 1}},
    zipfile=None,
)
