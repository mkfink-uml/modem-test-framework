# -*- coding: utf-8 -*-

import unittest
import compat
import sys

from plmn.network_checks import *

class NetworkRegisterAtnt(unittest.TestCase):
    def test_register_and_connect_on_atnt(self):
        NetworkChecks.network_register('WorldSim', 'mobiledata')
        NetworkChecks.network_connect('WorldSim', 'mobiledata')

if __name__ == '__main__':
    nargs = process_args()
    unittest.main(argv=sys.argv[nargs:], exit=False)
    Results.print_results()
