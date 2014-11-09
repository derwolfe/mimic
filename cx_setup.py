"""
cx_Freeze setup file for mimic
"""
from setuptools import find_packages
from cx_Freeze import setup, Executable

OPTIONS = {
    'build_dmg': {
        'namespace_packages': ['zope', 'six'],
        'includes': [
            'treq',
            'klein',
            'jsonschema',
            'six',
            'characteristic',
            'twisted.syslog'
        ]
    },
}

EXECUTABLES = [
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
    install_requires=[
        "characteristic==14.1.0",
        "klein==0.2.1",
        "twisted>=13.2.0",
        "jsonschema==2.0",
        "treq",
        "six"
    ],
    options=OPTIONS,
    executables=EXECUTABLES
)
