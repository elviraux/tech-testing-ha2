#!/usr/bin/env python2

import sys
import unittest
from tests import TestMakeGroup


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(TestMakeGroup.TestTarget),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())


