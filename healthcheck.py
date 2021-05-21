import os
import signal
import sys
import time

import requests


def signal_handler(signum, frame):
    signame = signal.Signals(signum).name
    description = signal.strsignal(signum)
    print(f'Signal handler called with {signame} ({signum}) {description}')
    sys.exit(0)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    print(f'requests version = {requests.__version__}')
    loglevel = 0

    while True:
        response = requests.get('https://thecleancoder.dev/healthcheck')
        if response.status_code == 200:
            res = response.json()
            date = res['date']
            rss = res['mem']['rss']
            print(f'<{loglevel}>{date} rss={rss}', flush=True)
            loglevel = (loglevel + 1) % 8
        else:
            print(f'<3>status_code = {response.status_code}')
        time.sleep(5)
