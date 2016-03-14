"""
This package contains individual IAPIMock plugins for mimic.

It also loads any and all plugins located in your python's path.
"""
from twisted.plugin import pluginPackagePaths
__path__.extend(pluginPackagePaths('mimic-internal-plugins.plugins'))
