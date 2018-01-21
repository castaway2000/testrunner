from testrunnerlib.test import HostInterface
from testrunnerlib.outcomes import Outcomes

from ping3 import ping


def pinger(host):
    result = Outcomes()
    try:
        ping_google = ping(host)
        print(ping_google)
        if ping_google:
            return result.passed()
        msg = 'ping had an issue, the following is all we know %s' % ping_google
        return result.failed(msg)
    except Exception as e:
        return result.aborted(exception=e)

if __name__ == '__main__':
    pinger(HostInterface().target)
