""" A simple demo of a thread worker """

import threading


def worker():
    print 'worker'

t = threading.Thread(target=worker)
t.start()
