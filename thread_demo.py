"""
A simple demo of a thread worker
Threads are similar to multiprocesses but threads share memory space
"""

import threading


def worker():
    print('worker')

t = threading.Thread(target=worker)
t.start()
