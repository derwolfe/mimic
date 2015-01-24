"""
Setup file for mimic
"""

from setuptools import setup, find_packages
from py2app.build_app import py2app
from twisted.plugin import getPlugins, IPlugin
from mimic import plugins


NAME = 'mimic'
VERSION = '1.3.0'
ID = 'mimic'
SCRIPT='bundle/start-app.py'
TEST_SCRIPT='bundle/run-tests.py'
PLIST = dict(
    CFBundleName                = NAME,
    CFBundleShortVersionString  = ' '.join([NAME, VERSION]),
    CFBundleGetInfoString       = NAME,
    CFBundleExecutable          = NAME,
    CFBundleIdentifier          = 'com.mimic.%s' % ID,
    LSUIElement                 = '1',
    LSMultipleInstancesProhibited = '1',
)

APP_DATA = dict(
    script=SCRIPT,
    plist=PLIST,
    extra_scripts=[TEST_SCRIPT]
)


class BuildWithCache(py2app):
    """
    Before building the application rebuild the `dropin.cache` files.
    """

    def run(self):
        """
        This generates `dropin.cache` files for mimic's plugins.
        """
        list(getPlugins(IPlugin))
        list(getPlugins(IPlugin, package=plugins))
        py2app.run(self)


setup(
    name=NAME,
    version=VERSION,
    description='An API-compatible mock service',
    app=[APP_DATA],
    packages=find_packages(exclude=[]) + ["twisted.plugins"],
    package_dir={'mimic': 'mimic'},
    setup_requires=[
        "klein==0.2.1",
        "twisted==14.0.0",
        "jsonschema==2.0",
        "treq==0.2.0",
        "characteristic==14.2.0",
        "six==1.6.1",
        "unittest2==0.5.1",
        # py2app has had a few bugs that need to be resolved
        # this combination of dependencies seem to work.
        "altgraph==0.12",
        "macholib==1.5.1",
        "modulegraph==0.11.1",
        "py2app==0.8.1",
        "pyobjc-framework-Cocoa==3.0.4",
        "pyobjc-framework-CFNetwork==3.0.4"
    ],
    cmdclass={
        'py2app': BuildWithCache
    },
    options={
        'py2app': {
            'includes': ['syslog', 'mimic.test.*', 'twisted.plugin'],
        }
    }
)
