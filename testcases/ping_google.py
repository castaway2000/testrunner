from ping3 import ping
from testrunnerlib.test import HostInterface
from testrunnerlib.outcomes import Outcomes


def pinger(host):
    result = Outcomes()
    try:
        ping_google = ping(host)  # PASS
        # ping_google = ping('google54321example.com')  # FAIL
        print(ping_google)
        if ping_google:
            return result.passed()
        return print(1, result.failed())
    except Exception as e:
        print(e)
        return print(2, result.aborted())


if __name__ == '__main__':
    hosts = HostInterface()
    print(pinger(hosts.host()))