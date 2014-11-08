"""
Setup file for mimic
"""

from setuptools import setup, find_packages

INSTALL_REQUIRES = [
    "characteristic==14.1.0",
    "klein==0.2.1",
    "twisted>=13.2.0",
    "jsonschema==2.0",
    "treq",
    "six"
]

setup(
    name='mimic',
    version='1.3.0',
    description='An API-compatible mock service',
    packages=find_packages(exclude=[]) + ["twisted.plugins"],
    package_dir={'mimic': 'mimic'},
    include_package_data=True,
    license="Apache License, Version 2.0",
    # for py2app
    app=['start-app.py'],
    setup_requires=['py2app'] + INSTALL_REQUIRES
)
