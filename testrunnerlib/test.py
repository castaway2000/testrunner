"""
# Type: Python 3
# Author: Adam Szablya
# Date created: January 17th 2018 
# Filename: test.py
# Description: main test running harness framework. 
"""
import yaml
import subprocess, os

from testrunner.models import Host, TestSuite


class HostInterface(object):
    def __init__(self):
        self._target = 'not set'

    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, value):
        print("setter of target called", value)
        self._target = value

    @target.deleter
    def target(self):
        print("deleter of target called")
        del self._target

    def host(self):
        out = Host.objects.get(id=self.target).name
        return out


class YamlInterface:
    def __init__(self, yamlfile):
        self.file = yamlfile

    def handle_yaml(self):
        data = TestSuite.objects.get(id=self.file)
        yamldata = yaml.safe_load(data.text)
        for i in yamldata['testsuite']:
            print(i)
            os.system('python3 %s' % i)
            # subprocess.call('pwd', shell=True)
            # subprocess.call('python %s' % i, shell=True)


def run_tests(host, yaml):
    h_interface = HostInterface()
    h_interface.target = host
    h_interface.host()
    yaml = YamlInterface(yaml)
    yaml.handle_yaml()
