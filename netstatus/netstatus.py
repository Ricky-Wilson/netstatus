#!/usr/bin/env python

'''
This module is for checking a networks status.
'''

import socket
from time import sleep
from functools import wraps
import errno
import os
import signal

class AnonymousError(Exception):
    '''
    Same as except Exception.
    '''
    pass

class NetworkStatus(object):

    limit = 2

    def timeout(seconds=1, error_message=os.strerror(errno.ETIME)):
        '''
        If a function does not finish in a given time
        send an alarm signal.
        '''
        def decorator(func):
            '''
            func is the function that will get wraped.
            '''
            def _handle_timeout():
                '''
                Send alarm single.
                '''
                signal.signal(signal.SIGALRM, _handle_timeout)
                signal.alarm(seconds)

            def wrapper(*args, **kwargs):
                '''
                Try to return the result of the wraped
                function.
                '''
                try:
                    result = func(*args, **kwargs)
                finally:
                    signal.alarm(0)
                return result
            return wraps(func)(wrapper)
        return decorator


    def set_timeout(self, limit):
        '''
        Update limit
        '''
        self.limit = limit


    @timeout(limit)
    def check(self, **kw):
        '''
        Check if the network is up.
        '''
        sleep(self.limit - 1)
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
        '''
        Call a function if the network is up.
        '''
        if self.online():
            func(*args, **kw)

    def if_offline(self, func, *args, **kw):
        '''
        Call a function if the network is down.
        '''
        if self.offline():
            func(*args, **kw)


    def run_test(self):
        '''
        Continuously check if the network is UP or DOWN.
        '''
        while True:
            if self.online():
                print 'Network is up'
            else:
                print 'network is down.'

if __name__ == '__main__':
    NetworkStatus().run_test()
