"""
Setup file for mimic
"""

from setuptools import setup, find_packages

setup(
    name='mimic',
    version='1.3.0',
    description='An API-compatible mock service',
    app=['mimic-bundle/start-app.py'],
    data_files=['mimic-bundle/gui/mimic.xib'],
    options={
        'py2app': {
            'includes': ['syslog', 'mimic.test.*'],
            'argv_emulation': True
        }
    }
)