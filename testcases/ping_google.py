from ping3 import ping


def pinger():
    try:
        ping_google = ping('google.com')  # PASS
        # ping_google = ping('google54321example.com')  # FAIL
        print(ping_google)
        if ping_google:
            return 'PASS'
        return print(1, 'Fail')
    except Exception as e:
        print(e)
        return print(2, "FAIL")


if __name__ == '__main__':
    print(pinger())