"""
Setup file for mimic
"""

from setuptools import setup, find_packages
from twisted.plugin import getPlugins, IPlugin
from py2app.build_app import py2app


NAME = 'mimic'
VERSION = '0.1'
ID = 'mimic'
SCRIPT='bundle/start-app.py'
TEST_SCRIPT='bundle/run-tests.py'
PLIST = dict(
    CFBundleName                = NAME,
    CFBundleShortVersionString  = ' '.join([NAME, VERSION]),
    CFBundleGetInfoString       = NAME,
    CFBundleExecutable          = NAME,
    CFBundleIdentifier          = 'com.yourdn.%s' % ID,
    LSUIElement                 = '1',
    LSMultipleInstancesProhibited = '1',
)

app_data = dict(
    script=SCRIPT,
    plist=PLIST,
    extra_scripts=[TEST_SCRIPT]
)

class BuildWithCache(py2app):
    """
    Before building the application rebuild the `dropin.cache` file that
    caches plugins.
    """
    def run(self):
        list(getPlugins(IPlugin))
        py2app.run(self)


setup(
    name='mimic',
    version='1.3.0',
    description='An API-compatible mock service',
    app=[app_data],
    cmdclass={
        'py2app': BuildWithCache
    },
    options={
        'py2app': {
            'includes': ['syslog', 'mimic.test.*', 'twisted.plugin'],
        }
    }
)
