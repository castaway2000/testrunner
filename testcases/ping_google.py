from ping3 import ping
from testrunnerlib.test import HostInterface


def pinger(host):
    try:
        ping_google = ping(host)  # PASS
        # ping_google = ping('google54321example.com')  # FAIL
        print(ping_google)
        if ping_google:
            return 'PASS'
        return print(1, 'Fail')
    except Exception as e:
        print(e)
        return print(2, "FAIL")


if __name__ == '__main__':
    hosts = HostInterface()
    print(pinger(hosts.host()))