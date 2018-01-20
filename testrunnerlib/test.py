"""
# Type: Python 3
# Author: Adam Szablya
# Date created: January 17th 2018 
# Filename: test.py
# Description: main test running harness framework. 
"""
from .outcomes import OutcomeParser
from testrunner.models import Hosts


class HostInterface:

    def host(self):
        # TODO: get selected host info from frontend.
        return 'google.com'

    def port(self):
        # TODO: get selected port info from frontend.
        return 'google.com'


class YamlInterface:

    def handle_yaml(self):
        # TODO: for line in yaml file run file and parse output
        return True
