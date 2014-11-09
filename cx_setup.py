"""
Setup file for mimic
"""

# if you are wanting to build using py2app, you basically have to use
# the brew installed version of python. py2app will not create a package
# using the system python insalled on os x. To use it, (especially if you
# using pyenv), the brewed python should have the highest precendence
# in your PATH.
# e.g. export PATH=/usr/local/bin:/usr/bin

from setuptools import setup, find_packages
from cx_freeze import setup, Executable

INSTALL_REQUIRES = [
    "characteristic==14.1.0",
    "klein==0.2.1",
    "twisted>=13.2.0",
    "jsonschema==2.0",
    "treq",
    "six"
]

executables = [
    Executable('start-app.py'),
]

setup(
    name='mimic',
    version='1.3.0',
    description='An API-compatible mock service',
    packages=find_packages(exclude=[]) + ["twisted.plugins"],
    package_dir={'mimic': 'mimic'},
    include_package_data=True,
    license="Apache License, Version 2.0",
    install_requires=INSTALL_REQUIRES,
)
