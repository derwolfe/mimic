from __future__ import absolute_import, division, unicode_literals

import sys

from twisted.trial.unittest import SynchronousTestCase
from twisted.python.filepath import FilePath

from mimic.core import MimicCore


class CoreBuildingTests(SynchronousTestCase):

    def test_loads_external_plugins(self):
        """
        Mimic loads plugins that are present in a `mimic-internal-plugins`
        module under a `plugins` directory
        """
        # make a plugins dir for `mimic-internal-plugins`
        # make sure that the plugin implements mimic specific interface
        # append it to the path
        # see if it is there
        # clean up: remove, delete, pop from path
