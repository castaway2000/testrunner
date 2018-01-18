"""
# Type: Python 3
# Author: Adam Szablya
# Date created: January 17th 2018 
# Filename: outcomes.py
# Description: results framework for the test hardness framework
"""


class Outcomes(object):
    def __init__(self):
        PASS = self.passed()
        FAIL = self.failed()
        SKIP = self.skiped()
        ABORT = self.aborted()

    def passed(self):
        return 'PASS'

    def failed(self):
        return 'FAIL'

    def skiped(self):
        return 'SKIP'

    def aborted(self):
        return 'ABORT'


class OutcomeParser(object):
    def __init__(self):
        self.details = self.logger()
        self.results = self.results()
        self.summary = self.summary()

    def logger(self, object):
        return True

    def results(self, object):
        return True

    def summary(self, object):
        return True