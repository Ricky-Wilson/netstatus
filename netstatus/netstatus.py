#!/usr/bin/env python


'''
This module is for checking a networks status.
'''

import socket
from time import sleep as _sleep
from functools import wraps
import errno
import os
import signal

TIMEOUT = 2

class NetworkStatus(object):
    def timeout(seconds=1, error_message=os.strerror(errno.ETIME)):
        def decorator(func):
            def _handle_timeout(signum, frame):
                return
                signal.signal(signal.SIGALRM, _handle_timeout)
                signal.alarm(seconds)
            def wrapper(*args, **kwargs):
                try:
                    result = func(*args, **kwargs)
                finally:
                    signal.alarm(0)
                return result

            return wraps(func)(wrapper)

        return decorator


    def set_timeout(self, t_out):
        '''
        Update the global variable TIMEOUT.
        '''
        global TIMEOUT
        TIMEOUT = t_out

    def sleep(self,delay):
        '''
        Sleep function with cleanup.
        '''
        try:
            _sleep(delay)
        except KeyboardInterrupt:
            exit()


    @timeout(TIMEOUT)
    def check(self, **kw):
        '''
        Check if the network is up.
        '''
        self.sleep(TIMEOUT)
        try:
            socket.gethostbyname(kw.get('remote_server', 'www.google.com'))
            return True
        except Exception:
            return False


    def online(self, **kw):
        '''
        return True is the network is UP.
        '''
        return self.check(**kw) is True


    def offline(self, **kw):
        '''
        return False if the network is DOWN.
        '''
        return self.online(**kw) is False


    def if_online(self, func, *args, **kw):
        if self.online():
            func(*args, **kw)

    def if_offline(self, func, *args, **kw):
        if self.offline():
            func(*args,**kw)


    def mainloop(self):
        '''
        Continuously check if the network is UP or DOWN.
        '''
        while True:
            up = self.check()
            if up:
                print 'Network is up'
            else:
                print 'network is down.'


if __name__ == '__main__':
    NetworkStatus().mainloop()
