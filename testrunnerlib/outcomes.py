"""
# Type: Python 3
# Author: Adam Szablya
# Date created: January 17th 2018 
# Filename: outcomes.py
# Description: results framework for the test hardness framework
"""


class Outcomes:
    def __init__(self):
        self.outcome = OutcomeParser

    def passed(self):
        out = {'status': 'PASS'}
        return self.outcome(info=out).logger()

    def failed(self, data):
        out = {'reason': data, 'status': 'FAIL'}
        return self.outcome(info=out).logger()

    def skiped(self):
        out = {'status': 'SKIP'}
        return self.outcome(info=out).logger()

    def aborted(self, exception=None):
        if exception:
            out = {'reason': exception, 'status': 'ABORT'}
        else:
            out = {'status': 'ABORT'}
        return self.outcome(info=out).logger()


class OutcomeParser:
    def __init__(self, info):
        self.info = info

    def logger(self):
        if self.info['status'] and self.info['reason']:
            # register the outcome in the model
            print(self.info['reason'])
        else:
            # register the status in the model
            print(self.info['status'])

    def results(self):
        return True

    def summary(self):
        return True