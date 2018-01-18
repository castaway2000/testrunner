"""
# Type: Python 3
# Author: Adam Szablya
# Date created: January 17th 2018 
# Filename: test.py
# Description: main test running harness framework. 
"""
from .outcomes import OutcomeParser
from testrunner.models import Hosts


class Hook:
    """
    use this as a point of reference for the testcases.
    """
    # TODO: get selected host, port and yaml file
    host = HostInterface()
    yaml = host.handle_yaml()
    OutcomeParser(yaml)


class HostInterface(object):
    def __init__(self, host, port, yaml):
        self.host = host
        self.port = port
        self.yaml = yaml

    def handle_yaml(self):
        # TODO: for line in yaml file run file and parse output
        return True
